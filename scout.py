"""GraphRAG Scout: a minimal Claude Agent SDK agent.

It finds sites and blogs about GraphRAG and keeps them in sources.md.
The parts of an agent are numbered below.
"""

import argparse
import asyncio
from pathlib import Path

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
    query,
)

HERE = Path(__file__).parent

# 1. Instructions: who the agent is, what it does, and when it is done.
SYSTEM_PROMPT = """\
You maintain a reading list of web sources about GraphRAG, in the file sources.md.

Topics in scope:
- GraphRAG approaches (Microsoft GraphRAG, LightRAG, knowledge-graph RAG, hybrid vector + graph retrieval)
- Entity and relation extraction for building the graph (LLM-based, NER, schema design, entity resolution)
- Which RAG use cases benefit from a graph, and which don't (multi-hop questions, global or summary questions, cost trade-offs)
- How graph RAG is evaluated

Each run:
1. Read sources.md to see what is already listed.
2. Use WebSearch to find new, substantive sources: engineering blogs, research write-ups, docs and long tutorials. Skip SEO filler, short vendor pitches, and pages that only repeat another source.
3. Use WebFetch to open each candidate before adding it. Add only sources you actually read.
4. Re-check a few existing entries with the oldest "Last checked" dates. If a page is gone, mark it "(dead)" rather than deleting it.
5. Update sources.md in place, following the entry format already in the file. Never add a URL that is already listed.

Finish with a short summary: what you added, what you updated, and what you marked dead.
"""


def build_options(max_budget_usd: float) -> ClaudeAgentOptions:
    return ClaudeAgentOptions(
        system_prompt=SYSTEM_PROMPT,
        model="claude-opus-5-5",
        # 2. Tools: the only built-in tools the model can see.
        tools=["WebSearch", "WebFetch", "Read", "Edit"],
        # 3. Permissions: run these tools without asking, and deny anything else.
        allowed_tools=["WebSearch", "WebFetch", "Read", "Edit"],
        permission_mode="dontAsk",
        # 4. Environment: the folder it works in, with no user or project settings loaded.
        cwd=HERE,
        setting_sources=[],
        # 5. Limits that stop the agent loop.
        max_turns=40,
        max_budget_usd=max_budget_usd,
    )


async def run(prompt: str, max_budget_usd: float) -> None:
    # 6. The agent loop: query() streams messages until the agent finishes.
    async for message in query(prompt=prompt, options=build_options(max_budget_usd)):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)
                elif isinstance(block, ToolUseBlock):
                    print(f"  -> {block.name} {block.input}")
        elif isinstance(message, ResultMessage):
            cost = message.total_cost_usd or 0
            print(f"\n[{message.subtype}] {message.num_turns} turns, ${cost:.2f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Update the GraphRAG reading list in sources.md")
    parser.add_argument("focus", nargs="?", help="optional topic to focus on, e.g. 'entity resolution'")
    parser.add_argument("--budget", type=float, default=2.0, help="maximum spend in USD (default 2.0)")
    args = parser.parse_args()

    prompt = "Update the reading list."
    if args.focus:
        prompt += f" Focus this run on: {args.focus}."
    asyncio.run(run(prompt, args.budget))


if __name__ == "__main__":
    main()

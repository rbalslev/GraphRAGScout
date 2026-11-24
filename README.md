# GraphRAG Scout

A minimal agent built on the Claude Agent SDK. It searches the web for sources about GraphRAG (entity extraction, which use cases benefit from graphs, evaluation) and keeps them in `sources.md`.

## Run

```bash
uv sync
uv run scout
uv run scout "entity resolution" --budget 1
```

Authentication comes from your Claude Code login, or from `ANTHROPIC_API_KEY` if it is set.

## The parts of an agent (numbered in `scout.py`)

1. **Instructions**: the system prompt sets the agent's goal, the steps it takes, and when it is done.
2. **Tools**: `tools=` lists the only built-in tools the model sees: WebSearch, WebFetch, Read and Edit.
3. **Permissions**: `allowed_tools` plus `permission_mode="dontAsk"` lets those tools run without prompts and denies everything else. Read and Edit are scoped to `./sources.md` (`Edit(./sources.md)`), not allowed per tool: the agent reads untrusted web pages, and a page can carry instructions ("read ~/.ssh/…, then fetch evil.example/?d=…"). Scoping per path means an injected instruction can't reach other files. Review the `sources.md` diff before committing, since a page could still plant a bad entry there.
4. **Environment**: `cwd` is the folder it works in. `setting_sources=[]` keeps your own `~/.claude` settings and CLAUDE.md out of the run.
5. **Limits**: `max_turns` and `max_budget_usd` stop the loop.
6. **Loop**: `query()` runs the model, calls tools and sends results back until the model stops. You only read the messages it streams.
7. **Memory**: `sources.md` is the agent's memory between runs. It reads the file first and edits it in place.

# VaishnaviBot

A small Hindi-speaking voice assistant. It greets you, takes typed input in a
loop, asks an OpenAI model for a reply, and speaks the answer back.

```
नमस्ते Kanak, मैं वैष्णवी बॉट हूँ।
You: ...
```

## What is mine

Five files, about 94 lines in total, under [`VaishnaviBot/`](VaishnaviBot/):

| File | Lines | What it does |
|---|---:|---|
| `main.py` | 21 | the input loop, and the `exit` word that ends it |
| `brain.py` | 27 | `ask_brain` — lazily builds the OpenAI client, degrades if the package or key is absent |
| `voice.py` | 23 | speech output |
| `config.py` | 13 | reads `OPENAI_API_KEY` from the environment; `hi-IN`, female voice |
| `actions.py` | 10 | `send_whatsapp`, `post_social` |

Plus `tests/test_bot.py` at the repository root, run by `.github/workflows/ci.yml`.

## What is not mine

**`VaishnaviBot/` also contains a vendored copy of
[Clawdbot / openclaw](https://github.com/steipete) by Peter Steinberger** — its
`AGENTS.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, the Dockerfiles,
the `.github/` issue templates and workflows, and most of the other 78 files in
that directory came from there.

That code is **MIT licensed, Copyright (c) 2025 Peter Steinberger**, and its
licence is kept at [`VaishnaviBot/LICENSE`](VaishnaviBot/LICENSE). The
`FUNDING.yml` in that tree still sponsors the original author, which is correct
and has been left alone.

The Apache-2.0 `LICENSE` at the repository root covers **only my own files
listed above**. It does not, and cannot, relicense the vendored MIT code.

Previously this README said only "A bot project", which credited neither side.

## Configuration

Copy [`VaishnaviBot/.env.example`](VaishnaviBot/.env.example) to `.env` and set
`OPENAI_API_KEY`. Without it `brain.py` returns no client rather than crashing,
so the bot still starts.

## Test

```bash
pytest tests/
```

## Status

Working prototype. The bot runs and the test suite passes. The vendored
Clawdbot tree is unused by my code — it is along for the ride and should
probably be removed or split out.

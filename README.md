# VaishnaviBot

A Hindi-speaking conversational assistant. It greets you, takes what you type,
asks a model for a reply, and speaks the answer back.

```
$ python -m vaishnavibot
[VOICE]: नमस्ते Kanak, मैं वैष्णवी बॉट हूँ।
You: exit
[VOICE]: फिर मिलेंगे।
```

## Design

Everything optional degrades instead of crashing. The bot runs with no API key
and no speech engine installed:

| Module | What it does | Without its optional dependency |
|---|---|---|
| `main.py` | the input loop; `exit` ends it | — |
| `brain.py` | `ask_brain` — builds the OpenAI client lazily | echoes the input back instead of calling out |
| `voice.py` | speech via `pyttsx3`, picking a female voice | prints `[VOICE]: …` to stdout |
| `config.py` | reads `OPENAI_API_KEY`; `hi-IN`, female | — |
| `actions.py` | `send_whatsapp`, `post_social` hooks | — |

That is why the test suite runs headless in CI with neither `openai` nor
`pyttsx3` present.

## Install

```bash
pip install -e .            # bot only
pip install -e ".[llm]"     # + openai, for real replies
pip install -e ".[voice]"   # + pyttsx3, for spoken output
```

Copy `.env.example` to `.env` and set `OPENAI_API_KEY` if you want real
replies. Without it the bot still starts.

## Run

```bash
python -m vaishnavibot
# or, after install:
vaishnavibot
```

## Test

```bash
pytest
```

Seven tests: config constants, both action hooks, the headless voice fallback,
the no-key brain fallback, the brain delegating to a mocked client, and the
loop exiting cleanly.

## Status

Working. Small on purpose — the loop, the model call and the voice layer are
each one short file, so any of them can be swapped without touching the others.

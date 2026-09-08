"""VaishnaviBot — a Hindi-speaking conversational assistant."""

from .actions import post_social, send_whatsapp
from .brain import ask_brain
from .config import BOT_NAME, LANGUAGE, VOICE_GENDER
from .main import run
from .voice import speak

__all__ = [
    "run",
    "ask_brain",
    "speak",
    "send_whatsapp",
    "post_social",
    "BOT_NAME",
    "LANGUAGE",
    "VOICE_GENDER",
]

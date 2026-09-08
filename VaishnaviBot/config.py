import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BOT_NAME = "VaishnaviBot"
VOICE_GENDER = "female"
LANGUAGE = "hi-IN"

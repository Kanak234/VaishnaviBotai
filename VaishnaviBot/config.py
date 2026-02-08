import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BOT_NAME = "VaishnaviBot"
VOICE_GENDER = "female"
LANGUAGE = "hi-IN"

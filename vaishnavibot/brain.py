from .config import OPENAI_API_KEY

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

client = None


def get_client():
    global client
    if client is None and OpenAI is not None and OPENAI_API_KEY:
        client = OpenAI(api_key=OPENAI_API_KEY)
    return client


def ask_brain(text, client_override=None):
    c = client_override or get_client()
    if c is None:
        return f"VaishnaviBot response: {text}"

    response = c.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content

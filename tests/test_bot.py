"""Unit test suite for VaishnaviBot."""

from unittest.mock import MagicMock

import config
from actions import post_social, send_whatsapp
from brain import ask_brain
from main import run as bot_run
from voice import speak


def test_config():
    """Verify bot configuration constants."""
    assert config.BOT_NAME == "VaishnaviBot"
    assert config.VOICE_GENDER == "female"
    assert config.LANGUAGE == "hi-IN"


def test_actions_whatsapp(capsys):
    """Verify WhatsApp hook formatting."""
    msg = "Urgent: Firewall anomaly detected"
    res = send_whatsapp(msg)
    captured = capsys.readouterr()

    assert "[HOOK] WhatsApp message: Urgent: Firewall anomaly detected" in res
    assert "[HOOK] WhatsApp message: Urgent: Firewall anomaly detected" in captured.out


def test_actions_social(capsys):
    """Verify Social post hook formatting."""
    post = "VaishnaviBot is online and monitoring systems."
    res = post_social(post)
    captured = capsys.readouterr()

    assert "[HOOK] Social Post: VaishnaviBot is online and monitoring systems." in res
    assert "[HOOK] Social Post: VaishnaviBot is online and monitoring systems." in captured.out


def test_voice_speak(capsys):
    """Verify speak function runs gracefully in headless environment."""
    speak("Testing voice synthesis engine.")
    # In headless environments, fallback prints [VOICE]: text
    captured = capsys.readouterr()
    assert (
        "Testing voice synthesis engine." in captured.out
        or "[VOICE]: Testing voice synthesis engine." in captured.out
    )


def test_brain_default_fallback():
    """Verify brain returns safe response when OpenAI API key is unset."""
    query = "Tell me the status of network nodes"
    reply = ask_brain(query)
    assert "VaishnaviBot" in reply
    assert query in reply


def test_brain_with_mock_client():
    """Verify brain delegates to OpenAI client when present."""
    mock_client = MagicMock()
    mock_choice = MagicMock()
    mock_choice.message.content = "All systems operating normally."
    mock_client.chat.completions.create.return_value.choices = [mock_choice]

    reply = ask_brain("Check health", client_override=mock_client)
    assert reply == "All systems operating normally."

    mock_client.chat.completions.create.assert_called_once()
    args, kwargs = mock_client.chat.completions.create.call_args
    assert kwargs["model"] == "gpt-4o-mini"
    assert kwargs["messages"] == [{"role": "user", "content": "Check health"}]


def test_interactive_run_exit(capsys):
    """Verify main loop terminates cleanly on 'exit'."""
    inputs = ["exit"]

    def fake_input(prompt):
        return inputs.pop(0)

    bot_run(input_source=fake_input)
    captured = capsys.readouterr()
    assert "फिर मिलेंगे" in captured.out or "[VOICE]" in captured.out

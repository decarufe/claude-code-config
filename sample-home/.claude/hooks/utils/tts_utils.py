#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "python-dotenv",
# ]
# ///

"""
Shared TTS utility functions for Claude hooks.
Centralizes TTS script selection logic to avoid duplication.
"""

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional


def get_tts_script_path():
    """
    Determine which TTS script to use based on available API keys and systems.
    Priority order: Piper (UPMC French) > ElevenLabs > OpenAI > pyttsx3
    
    Returns:
        str: Path to the TTS script to use, or None if no TTS scripts are available
    """
    # Get current script directory and construct utils/tts path
    script_dir = Path(__file__).parent
    tts_dir = script_dir / "tts"
    
    # Check for Piper TTS with UPMC voice (highest priority - no API key needed)
    piper_script = tts_dir / "piper_tts.py"
    if piper_script.exists():
        # Check if the UPMC model exists
        model_path = "/home/eric/piper-voices/fr/fr_FR/upmc/medium/fr_FR-upmc-medium.onnx"
        if os.path.exists(model_path):
            return str(piper_script)
    
    # Check for ElevenLabs API key (second priority)
    if os.getenv('ELEVENLABS_API_KEY'):
        elevenlabs_script = tts_dir / "elevenlabs_tts.py"
        if elevenlabs_script.exists():
            return str(elevenlabs_script)
    
    # Check for OpenAI API key (third priority)
    if os.getenv('OPENAI_API_KEY'):
        openai_script = tts_dir / "openai_tts.py"
        if openai_script.exists():
            return str(openai_script)
    
    # Fall back to pyttsx3 (no API key required)
    pyttsx3_script = tts_dir / "pyttsx3_tts.py"
    if pyttsx3_script.exists():
        return str(pyttsx3_script)
    
    return None


def is_using_piper_tts():
    """
    Check if we're using Piper TTS (to determine message language).
    
    Returns:
        bool: True if using Piper TTS, False otherwise
    """
    tts_script = get_tts_script_path()
    return tts_script and str(tts_script).endswith('piper_tts.py')


def get_localized_message(english_message, french_message=None):
    """
    Get a localized message based on the TTS engine in use.
    
    Args:
        english_message (str): Message in English
        french_message (str, optional): Message in French. If not provided, uses English message.
    
    Returns:
        str: Localized message based on TTS engine
    """
    if is_using_piper_tts() and french_message:
        return french_message
    return english_message
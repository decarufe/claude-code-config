#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///

import sys
import random
import subprocess
import tempfile
import os
from pathlib import Path

def main():
    """
    Piper TTS Script with UPMC French Voice
    
    Uses piper for high-quality text-to-speech synthesis with French UPMC voice.
    Accepts optional text prompt as command-line argument.
    
    Usage:
    - ./piper_tts.py                    # Uses default text
    - ./piper_tts.py "Your custom text" # Uses provided text
    
    Features:
    - High-quality UPMC French voice
    - Offline TTS (no API key required)
    - Uses piper + aplay for audio playback
    """
    
    # Path to the UPMC French voice model
    model_path = "/home/eric/piper-voices/fr/fr_FR/upmc/medium/fr_FR-upmc-medium.onnx"
    
    # Check if model exists
    if not os.path.exists(model_path):
        print("❌ Error: UPMC French voice model not found")
        print(f"Expected at: {model_path}")
        sys.exit(1)
    
    # Check if piper is available
    try:
        subprocess.run(["piper", "--help"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Error: piper command not found")
        sys.exit(1)
    
    # Check if aplay is available
    try:
        subprocess.run(["aplay", "--help"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Error: aplay command not found")
        sys.exit(1)
    
    print("🎙️  Piper TTS (UPMC French)")
    print("=" * 25)
    
    try:
        # Get text from command line argument or use default
        if len(sys.argv) > 1:
            text = " ".join(sys.argv[1:])  # Join all arguments as text
        else:
            # Default completion messages in French
            completion_messages = [
                "Travail terminé!",
                "Tout est fini!",
                "Tâche accomplie!",
                "Travail accompli!",
                "Prêt pour la prochaine tâche!"
            ]
            text = random.choice(completion_messages)
        
        print(f"🎯 Texte: {text}")
        print("🔊 Génération audio...")
        
        # Create temporary file for audio output
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            temp_audio_path = temp_file.name
        
        try:
            # Generate speech using piper
            process = subprocess.run([
                "piper",
                "--model", model_path,
                "--output_file", temp_audio_path
            ], 
            input=text,
            text=True,
            capture_output=True,
            check=True
            )
            
            print("🔊 Lecture audio...")
            
            # Play the audio using aplay
            subprocess.run([
                "aplay", temp_audio_path
            ], 
            capture_output=False,
            check=False
            )
            
            print("✅ Lecture terminée!")
            
        finally:
            # Clean up temporary file
            if os.path.exists(temp_audio_path):
                os.unlink(temp_audio_path)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la génération/lecture audio: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///

import sys
import random
import subprocess
import os
import re
import unicodedata
from pathlib import Path

def normalize_filename(text, max_length=50):
    """
    Normalise le texte pour créer un nom de fichier valide.
    
    Args:
        text (str): Le texte à normaliser
        max_length (int): Longueur maximale du nom de fichier
    
    Returns:
        str: Nom de fichier normalisé
    """
    # Supprimer les accents
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    
    # Convertir en minuscules
    text = text.lower()
    
    # Remplacer les espaces et caractères spéciaux par des underscores
    text = re.sub(r'[^\w\s-]', '', text)  # Garder seulement lettres, chiffres, espaces et tirets
    text = re.sub(r'[\s-]+', '_', text)   # Remplacer espaces et tirets par underscores
    
    # Supprimer les underscores en début/fin
    text = text.strip('_')
    
    # Limiter la longueur
    if len(text) > max_length:
        text = text[:max_length].rstrip('_')
    
    # S'assurer qu'il reste au moins quelque chose
    if not text:
        text = "audio"
    
    return text

def get_cached_audio_path(text):
    """
    Génère le chemin vers le fichier audio mis en cache pour un texte donné.
    
    Args:
        text (str): Le texte à synthétiser
    
    Returns:
        str: Chemin vers le fichier audio (existant ou à créer)
    """
    # Créer le dossier de cache s'il n'existe pas
    script_dir = Path(__file__).parent
    cache_dir = script_dir / "audio_cache"
    cache_dir.mkdir(exist_ok=True)
    
    # Générer le nom de fichier normalisé
    filename = normalize_filename(text) + ".wav"
    
    return str(cache_dir / filename)

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
        
        # Obtenir le chemin vers le fichier audio en cache
        audio_path = get_cached_audio_path(text)
        
        # Vérifier si le fichier existe déjà en cache
        if os.path.exists(audio_path):
            print("♻️  Réutilisation du fichier en cache...")
        else:
            print("🔊 Génération audio...")
            
            # Generate speech using piper
            process = subprocess.run([
                "piper",
                "--model", model_path,
                "--volume", "0.2",
                "--output_file", audio_path
            ], 
            input=text,
            text=True,
            capture_output=True,
            check=True
            )
            
            print(f"💾 Audio sauvegardé: {os.path.basename(audio_path)}")
        
        print("🔊 Lecture audio...")
        
        # Play the audio using aplay
        subprocess.run([
            "aplay", "--nonblock", audio_path
        ], 
        capture_output=False,
        check=False
        )
        
        print("✅ Lecture terminée!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la génération/lecture audio: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
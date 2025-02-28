from gtts import gTTS
from playsound import playsound
import os
import re

# Get the Documents folder
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

# Prompt user for text input
text = input("Enter the text you want to convert to speech: ").strip()
if not text:
    print("Error: No text entered! Please try again.")
    exit()

# Voice options
voices = {
    "1": ("en", "com"),        # English (Default - American)
    "2": ("es", "com"),        # Spanish
    "3": ("fr", "com"),        # French
    "4": ("de", "com"),        # German
    "5": ("ja", "co.jp"),      # Japanese
}

# Display voice options
print("\nChoose a voice:")
print("1. English (US)")
print("2. Spanish")
print("3. French")
print("4. German")
print("5. Japanese")

# Get user choice
choice = input("Enter the number of the voice you want: ").strip()
lang, tld = voices.get(choice, ("en", "com"))  # Default to English (US) if invalid choice

# Create a safe filename
safe_filename = re.sub(r'[\\/*?:"<>|]', "", text[:20]).strip()
if not safe_filename:
    safe_filename = "speech"

# Define file path
file_path = os.path.join(documents_folder, f"{safe_filename}.mp3")

# Generate speech with selected voice
tts = gTTS(text, lang=lang, tld=tld)
tts.save(file_path)

# Play the generated MP3
print(f"\n MP3 file saved to: {file_path}")
print("🔊 Playing audio...")
playsound(file_path)

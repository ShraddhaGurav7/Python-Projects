# import pyttsx3

# def speak(text, accent='Hindi'):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
    
#     # Find the voice with the specified accent (Hindi)
#     selected_voice = None
#     for voice in voices:
#         if accent.lower() in voice.languages[0].lower():
#             selected_voice = voice
#             break

#     if selected_voice:
#         engine.setProperty('voice', selected_voice.id)
#     else:
#         print(f"No voice with the {accent} accent found.")
#         return

#     engine.say(text)
#     engine.runAndWait()

# # Example usage:
# text_to_speak = "नमस्ते, मैं आपकी सहायता कैसे कर सकता हूँ?"
# speak(text_to_speak, accent='Hindi')

# from gtts import gTTS

# text = "नमस्ते, मैं आपकी सहायता कैसे कर सकता हूँ?"
# language = 'hi'  # Hindi language code

# tts = gTTS(text, lang=language)

# # Save the generated speech to a file or play it
# tts.save("indian_accent_hindi.mp3")

from gtts import gTTS
import pygame.mixer
pygame.mixer.init()
pygame.mixer.music.load("indian_accent_response.mp3")
pygame.mixer.music.play()

def generate_indian_accent_speech(text, language='en-in'):
    tts = gTTS(text, lang=language)
    tts.save("indian_accent_response.mp3")

# Example usage
text_to_speak = "How can I assist you today?"
generate_indian_accent_speech(text_to_speak)
try:
    generate_indian_accent_speech(text_to_speak)
except Exception as e:
    print("An error occurred:", str(e))
    
# import pyttsx3

# def text_to_speech(text):
#     try:
#         # Initialize the TTS engine
#         engine = pyttsx3.init()

#         # Set properties (optional)
#         engine.setProperty('rate', 150)  # Speed of speech
#         engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

#         # Speak the text
#         print(f"Speaking: {text}")
#         engine.say(text)

#         # Wait until speaking is complete
#         engine.runAndWait()
#     except Exception as e:
#         print(f"Error in Text-to-Speech: {e}")

# # Main program
# if __name__ == "__main__":
#     text = input("Enter the text to convert to speech: ")
#     text_to_speech(text)



# Using the another Library *********************************************************************************************************
from gtts import gTTS
import os
import sounddevice as sd
import soundfile as sf

def text_to_speech(text, filename="temp.mp3"):
    try:
        # Convert text to speech and save as a temporary MP3 file
        temp_mp3 = "temp.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(temp_mp3)
        print("Text-to-Speech conversion successful.")

        # Convert MP3 to WAV
        os.system(f"ffmpeg -i {temp_mp3} {filename} -y")

        # Play the WAV file
        data, samplerate = sf.read("temp.mp3")
        print("Playing the audio...")
        sd.play(data, samplerate)
        sd.wait()

        # Cleanup temporary files
        os.remove(temp_mp3)
        os.remove(filename)
        print("Playback complete.")
    except Exception as e:
        print(f"Error in Text-to-Speech: {e}")

# Main program
if __name__ == "__main__":
    text = input("Enter the text to convert to speech: ")
    text_to_speech(text)

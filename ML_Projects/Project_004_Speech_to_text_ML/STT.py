import whisper
import sounddevice as sd
import numpy as np
import os

# Record audio
def record_audio(duration=5, samplerate=16000, filename="input.wav"):
    print(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    print("Recording complete. Saving file...")
    
    # Save audio file
    import soundfile as sf
    sf.write(filename, audio_data, samplerate)
    print(f"Audio saved to {filename}")

# Speech-to-text using Whisper
def speech_to_text(filename="input.wav"):
    print("Loading Whisper model...")
    model = whisper.load_model("base")  # Load the base Whisper model
    print("Converting speech to text...")
    result = model.transcribe(filename)
    return result["text"]

# Main function
if __name__ == "__main__":
    audio_file = "input.wav"
    duration = int(input("Enter recording duration (in seconds): "))
    record_audio(duration, filename=audio_file)
    try:
        transcription = speech_to_text(audio_file)
        print("\nTranscription:")
        print(transcription)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)  #Clean up the recorded file

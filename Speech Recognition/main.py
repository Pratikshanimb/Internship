import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Load an audio file (replace 'filename.wav' with your actual file)
filename = 'path/to/your/audio/file.wav'
with sr.AudioFile(filename) as source:
    # Listen for the data (load audio to memory)
    audio_data = r.record(source)

    # Recognize (convert from speech to text)
    try:
        text = r.recognize_google(audio_data)
        print(f"Recognized text: {text}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error: {e}")


m = sr.Microphone()

# Capture microphone input
with m as source:
    print("Speak something:")
    audio_data = r.listen(source)

    # Recognize speech
    try:
        text = r.recognize_google(audio_data)
        print(f"Recognized text: {text}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error: {e}")

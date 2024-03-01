import speech_recognition as sr


class RecognizerWithGoogle(sr.Recognizer):
    def recognize_google(self, audio):
        try:
            # Use Google Web Speech API to recognize the speech
            text = self.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand audio."
        except sr.RequestError as e:
            return f"Error with the speech recognition service; {e}"


def recognize_speech() -> object:
    # Initialize the custom recognizer
    custom_recognizer = RecognizerWithGoogle()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something:")
        # Adjust for ambient noise before listening
        custom_recognizer.adjust_for_ambient_noise(source)

        # Listen to the audio
        audio = custom_recognizer.listen(source)

        print("Processing...")

        # Call the custom recognize_google method
        text = custom_recognizer.recognize_google(audio)
        print("You said:", text)


if __name__ == "_main_":
    recognize_speech()

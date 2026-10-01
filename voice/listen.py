import speech_recognition as sr
from .speak import Speak


class Listen:
    def __init__(self):
        self.speaker = Speak() 

        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 0.3
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.dynamic_energy_adjustment_damping = 0.15
        self.recognizer.dynamic_energy_ratio = 1.5
        self.recognizer.non_speaking_duration = 0.3

    def listen(self, ambient_duration=1):
        try:
            with sr.Microphone() as source:
                self.speaker.say(
                    "Listening. Please remain silent for ambient noise adjustment."
                )
                self.recognizer.adjust_for_ambient_noise(
                    source, duration=ambient_duration
                )

                self.speaker.say("You can speak now.")
                audio = self.recognizer.listen(source)

        except OSError as e:
            self.speaker.say("Microphone error.")
            print(f"Microphone Error: {e}")
            return None

        try:
            text = self.recognizer.recognize_google(
                audio, language="en-IN"
            )
            print("You said:", text)
            return text

        except sr.UnknownValueError:
            self.speaker.say("Sorry, I could not understand.")
            return None

        except sr.RequestError:
            self.speaker.say("Speech recognition service error.")
            return None

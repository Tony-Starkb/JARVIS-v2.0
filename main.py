from core.brain import Brain
from voice.listen import Listen
from voice.speak import Speak
from voice.wakeWordDetection import WakeWordDetector
import re


SHUTDOWN_COMMAND = re.compile(r"\b(shut ?down|exit|quit|goodbye|power off)\b")
PAUSE_COMMAND = re.compile(
    r"\b(take a break|pause(?: listening)?|stop listening|stop listen|sleep)\b"
)



"""
the flow will be like:
program starts -> wake word detection -> jarvis gives introduction -> user speaks -> execute task -> and stay in the activ listening mode until the user said take a break

take a break -> jarvis is running but the jarvis is in passive listening mode -> if want to use then use the wake word and above loop continues
shutdown -> program ends    
"""




def main():
    jarvis = Brain()
    listener = Listen()
    wake_word_detector = WakeWordDetector()
    speaker = Speak()

    try:
        while True:
            wake_word = wake_word_detector.listen_for_wake_word()
            if wake_word != "WAKE WORD DETECTED":
                continue

            wake_word_detector.stop_stream()
            greeting = "Hello! How can I help you?"
            print(f"JARVIS: {greeting}")
            speaker.say(greeting)

            while True:
                user_input = listener.listen()
                if not user_input:
                    continue

                command = user_input.lower().strip(" .!?,")

                if SHUTDOWN_COMMAND.search(command):
                    farewell = "Goodbye. Powering down."
                    print(f"JARVIS: {farewell}")
                    speaker.say(farewell)
                    return

                if PAUSE_COMMAND.search(command):
                    pause_message = "Taking a break. Say the wake word to resume."
                    print(f"JARVIS: {pause_message}")
                    speaker.say(pause_message)
                    wake_word_detector.start_stream()
                    break

                response = jarvis.process(command)
                print(f"JARVIS: {response}")
                speaker.say(response)
    finally:
        wake_word_detector.close()
if __name__ == "__main__":
    main()
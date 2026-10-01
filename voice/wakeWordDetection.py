import pyaudio
import numpy as np
import openwakeword
from openwakeword.model import Model


MODEL_PATH = "hey_jarvis.onnx"

RATE = 16000
CHANNELS = 1
CHUNK = 1280

THRESHOLD = 0.3


class WakeWordDetector:

    def __init__(self, model_path=MODEL_PATH):

        self.model = Model(
            wakeword_models=[model_path],
            inference_framework="onnx"
        )

        self.audio = pyaudio.PyAudio()

        self.stream = None

        self.start_stream()

    def start_stream(self):

        if self.stream is not None:
            return

        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )

    def listen_for_wake_word(self):

        print("\nListening for wake word...")

        self.start_stream()

        while True:

            data = self.stream.read(
                CHUNK,
                exception_on_overflow=False
            )

            audio_data = np.frombuffer(
                data,
                dtype=np.int16
            )

            prediction = self.model.predict(audio_data)

            score = prediction.get("hey_jarvis", 0)

            print(
                f"\rWake word score: {score:.4f}",
                end=""
            )

            if score >= THRESHOLD:

                print("\n🔥 WAKE WORD DETECTED!")
                self.model.reset()

                return "WAKE WORD DETECTED"

    def stop_stream(self):
        if self.stream is None:
            return

        if self.stream.is_active():
            self.stream.stop_stream()

        self.stream.close()
        self.stream = None

    def close(self):
        self.stop_stream()
        self.audio.terminate()
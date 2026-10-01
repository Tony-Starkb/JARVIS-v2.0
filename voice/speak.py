import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

class Speak:
	def say(self, text):
		audio = " "
		for i in text:
			audio += str(i)

		print(audio)
		engine.say(audio)
		engine.runAndWait()

'''
if __name__ == "__main__":
	Speak("Hello Sir! I am jarvis, the version 1.o created to assist and automate this Machine")
'''
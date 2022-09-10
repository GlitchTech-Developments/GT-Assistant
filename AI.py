import pyttsx3
import speech_recognition as sr

class AI():
    __name = ""
    __skills = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.recognize = sr.Recognizer()
        self.mic = sr.Microphone()

        if name is not None:
            self.__name = name

        print("Listening")

        with self.mic as source:
            self.recognize.adjust_for_ambient_noise(source)

    @property
    def name(self):
        return self.__name

    @name.setter 
    def name(self, value):
        welcome = "Hello, my name is " + self.__name 
        self.__name = value
        self.engine.say(welcome)
        self.engine.runAndWait()

    def Say(self, message):
        self.engine.say(message)
        self.engine.runAndWait()
    
    def Listen(self):
        print("I'm listening")
        with self.mic as source:
            audio = self.recognize.listen(source)
        print("Understood")
        try:
            phrase = self.recognize.recognize_google(audio, show_all=False, language="en-US")
            sentence = "Got it, you said " + phrase
            self.engine.say(sentence)
            self.engine.runAndWait()
        except e as error:
            print("Sorry, dind't catch that", error)
            self.engine.say("Sorry didn't catch that")
            self.engine.runAndWait()
        print("You said", phrase)
        return phrase

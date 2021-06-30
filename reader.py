import pyttsx3

class Reader:
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.luciana')

    def say_something(self, phrase):

        self.engine.say(phrase)
        self.engine.runAndWait()

        # for l in phrase:
        #     engine.say(l)
        #     engine.runAndWait()

        self.engine.stop()

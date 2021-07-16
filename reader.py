import pyttsx3


class Reader:
    engine = pyttsx3.init()
    engine.setProperty("voice", "com.apple.speech.synthesis.voice.luciana")
    engine.setProperty("rate", 50000)
    engine.setProperty("volume", 0.2)

    def say_something(self, phrase):

        self.engine.say(phrase)
        self.engine.runAndWait()

        # for l in phrase:
        #     engine.say(l)
        #     engine.runAndWait()

        self.engine.stop()

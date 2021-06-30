import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.luciana')

frase = ""

while frase != "/exit":
    frase = input("Digite aqui:")
    for l in frase:
        engine.say(l)
        engine.runAndWait()

engine.stop()

import pyttsx3

frase = input("Digite aqui:")
while frase != "/exit":
    frase = input("Digite aqui:")
    engine = pyttsx3.init()
    engine.say(frase)
    engine.runAndWait()
    engine.stop()







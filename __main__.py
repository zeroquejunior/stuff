from reader import Reader
from string_tools import StringTools

reader = Reader()
frase = ""
trolha = "teste"

while frase != "/exit":
    frase = input("digite algo: ")
    reversed_phrase = string_tools.reverse(frase)
    reader.say_something(
        string_tools.add_something_in_the_end(frase, "rola") + " " + reversed_phrase
    )

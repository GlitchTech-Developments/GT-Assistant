# External imports
import pyjokes
# Local Imports
from AI import AI

SAM = AI()

def Joke():
    funny = pyjokes.get_joke()
    print(funny)
    SAM.Say(funny)

command = ""

while True and command != "goodbye":
    command = SAM.Listen()
    print("Command was: " + command)

    if command == "tell me a joke":
        Joke()

SAM.Say("Goodbye, I'm going offline now")

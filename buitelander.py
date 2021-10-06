import time
from os import system, name

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _=system("clear")

def start():
    clear()
    print("je bent net wakker en je hoort een explosie naast je wat ga je doen.\nA. rennen\nB. je blijft staan\nC. je gaat verstoppen")
    vraag1=input()
    if vraag1=='A':
        andwoord1()
    elif vraag1=='B'or'C':
        dood1()
    else:
        print("incorrect input")
        start()

def andwoord1():
    print("hallo")

def dood1():
    print("er is een bom op je huis geland\nEn je hebt het niet overleefd")
    restart=input("opnieuw spelen? Y/N: ")
    if restart=='y'or'Y':
        start()
    elif restart=='n'or'N':
        print()

start()
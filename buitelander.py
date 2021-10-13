import time
from os import system, name
import random

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _=system("clear")
leven=1
def vraag1():
    clear()
    print("je bent net wakker en je hoort een explosie naast je wat ga je doen.\nA. rennen\nB. je blijft staan\nC. je gaat verstoppen")
    v1=input()
    if v1=='A':
        vraag2()
    elif v1=='B'or'C':
        print("er is een bom op je huis geland\nEn je hebt het niet overleefd")
        dood()
    else:
        print("incorrect input")
        vraag1()

def vraag2():
    print("je hoort een explosie naast je maar je overleeft het wel\nJe denkt snel na en weet dat het niet veilig is waar ga je naar toe.\nA. naar de zee\nB. naar het vliegveld\nC. naar een safe house")
    v2=input()
    if v2=='A':
        vraag3()
    elif v2=='B':
        vraag4()
    elif v2=='C':
        vraag5()
    else:
        print("incorrect input")
        vraag2()

def vraag3():
    print("Je kiest ervoor om naar de zee te gaan. Er zijn 2 schepen een groot schip maar met veel man of een klein schip met minder man.\n1. groot schip\n2. klein schip")
    v2=input()
    if v2=='1':
        vraag6()
    elif v2=='2':
        vraag7()
    else:
        print("incorrect input")
        vraag3()
def vraag4():
    print("Je kiest ervoor om naar de zee te gaan. Er zijn 2 schepen een groot schip maar met veel man of een klein schip met minder man.\n1. groot schip\n2. klein schip")
    v2=input()
    if v2=='1':
        vraag6()
    elif v2=='2':
        vraag7()
    else:
        print("incorrect input")
        vraag4()
def vraag5():
    print()

def dood():
    restart=input("opnieuw spelen? Y/N: ")
    if restart=='Y':
        vraag1()
    elif restart=='N':
        leven = 0
    else:
        print("incorrect input")
        dood()
if leven==1:
    vraag1()
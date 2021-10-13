import time
from os import system, name
import random

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _=system("clear")

leven=1
kans=1
stemmen=0

def stem():
    print("Je bent een kandidaat")
    if kans==1:
        stemmen=random.randint(40, 70)
    elif kans==0:
        stemmen=random.randint(20, 60)
    if stemmen>50:
        print("Je hebt "+str(stemmen)+"% van de stemmen")
        vraag15()
    elif stemmen==50:
        print("Je hebt 50% van de stemmen")
        vraag15()
    elif stemmen<50:
        print("Je hebt "+str(stemmen)+"% van de stemmen")
        vraag19()


def vraag1():
    stemmen=0
    kans=1
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
    print("Je kiest ervoor om naar de zee te gaan. Er zijn 2 schepen een groot schip maar met veel man \nof een klein schip met minder man.\n1. groot schip\n2. klein schip")
    v3=input()
    if v3=='1':
        vraag6()
    elif v3=='2':
        print("het is misschien een kleine boot maar")
        vraag7()
    else:
        print("incorrect input")
        vraag3()

def vraag4():
    print("Je komt aan bij het vlieg veld \n er zijn nog maar 2 vliegtuigen, maar ze zijn allebei druk welke ga je kiezen\nA. vliegtuig dat nu gaat vertrekken\nB. vliegtuig waar je nog tijd voor hebt\nC. wacht tot er een beter vliegtuig komt ")
    v4=input()
    if v4=='A':
        print("")
        vraag7()
    elif v4=='B':
        print("de terroristen hebben het vliegtuig neer geschoten")
        dood()
    elif v4=='C':
        vraag8()
    else:
        print("incorrect input")
        vraag4()

def vraag5():
    print("Je komt aan bij de safe house en er zijn een paar anderen mensen\nna een paar dagen horen jullie een explosie buiten wat gaan jullie doen\nA. kijk zelf naar buiten\nB. vraag iemand anders om te kijken\nC. wacht er is waarschijnlijk niets aan de hand")
    v5=input()
    if v5=='A':
        print("Je loopt naar buiten en word verbrand door de explosie")
        dood()
    elif v5=='B':
        vraag9()
    elif v5=='C':
        vraag10()
    else:
        print("incorrect input")
        vraag5()

def vraag6():
    print("Je bent op het grote schip gegaan er zijn veel mensen, maar na een paar dagen zijn er veel dood\nOmdat het een groot schip zijn er piraten gekomen om al het geld te stelen dus wat ga je doen\nA. AANVALLEN!\nB. spring van het dek")
    v6=input()
    if v6=='A':
        print("Je probeert de piraten aantevallen maar ze hebben geweren dus je wordt neergeschoten")
        dood()
    elif v6=='B':
        print("Je springt van het dek maar je zit op het midden van de oceaan dus je verdrinkt")
        dood()
    elif v6=='C':
        vraag11()
    else:
        print("incorrect input")
        vraag6()

def vraag7():
    print("je komt veilig aan in Nederland en probeert kennis te maken met de locals waar ga je naar toe\nA. museum\nB. een bar")
    v7=input()
    if v7=='A':
        print("Je bent naar een museum gegaan en hebt veel van de cultuur geleerd ook heb je wat mensen ontmoet")
        einden1()
    elif v7=='B':
        print("Je bent naar een bar gegaan en ookal kan je de taal niet heb je het nog steeds leuk\nnadat je uit de bar komt komt er iemand naar je toe hij vraagt je om geld ")
        vraag12()
    else:
        print("incorrect input")
        vraag7()

def vraag8():
    print("Je bent op het vlieg veld aan het wachten wanner je het 2e vliegtuig ziet neerstorten gelukkig heb je gekozen om hier te blijven\nNa een paar uur wachten zie je de terroristen iemand gavangen houden wat ga je doen?\nA. val de terroristen aan\nB. maak een afleiding\nC. ren weg")
    v8=input()
    if v8=='A':
        print("Je valt de terroristen aan maar je wordt neergeschoten")
        dood()
    elif v8=='B':
        vraag13()
    elif v8=='C':
        vraag5()
    else:
        print("incorrect input")
        vraag8()

def vraag9():
    print("Iedereen kijkt je aan met bozen ogen ze zeggen dat jij de reden bent dat hij dood is\nWat ga je doen om hun beter te laten voelen\nA. zeg dat je niks fout hebt gedaan\nB. zeg dat je je schuldig vind en dat je het recht gaat zeggen\nC. zeg niks")
    v9=input()
    if v9=='A':
        print("Je moet weg en gaat dood door de radio actiefe stralingen")
        dood()
    elif v9=='B':
        kans=0
        print("Je geeft een goed punt dus je mag weer in de groep\n maar niet iedereen denkt dat je vertrouwbaar bent")
        vraag10()
    elif v9=='C':
        vraag14()
    else:
        print("incorrect input")
        vraag9()

def vraag10():
    print("Iedereen gaat stemmen wie de baas wordt van de bunker wordt wat ga je doen?\nA. word een kandidaat\nB. doe niets\nC. stem voor wie jij denkt ")
    v10=input()
    if v10=='A':
        stem()        
    elif v10=='B':
        vraag16()
    elif v10=='C':
        vraag17()
    else:
        print("incorrect input")
        vraag10()

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
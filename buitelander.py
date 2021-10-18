import time
from os import system, name
import random

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _=system("clear")

eind1=0
eind2='niet gehaald'
eind3='niet gehaald'
eind4='niet gehaald'
eind5='niet gehaald'
eind6='niet gehaald'

leven=1
kans=0
stemmen=0

def menu(eind1, eind2, eind3, eind4, eind5, eind6):
    print(str(eind1)+" keer dood gegaan\nNederland einde1 "+eind2+"\nNederland einde2 "+eind3+"\nSlechte baas "+eind4+"\nBoer einde "+eind5+"\nBaas einde "+eind6)
    verder=input()

def stem():
    print("Je bent een kandidaat")
    if kans==0:
        stemmen=random.randint(40, 70)
    elif kans==1:
        stemmen=random.randint(30, 60)
    elif kans==2:
        stemmen=random.randint(20, 50)
    print("Je hebt "+str(stemmen)+"% van de stemmen")
    if stemmen>50:
        vraag15()
    elif stemmen==50:
        vraag15()
    elif stemmen<50:
        vraag19()


def vraag1():
    stemmen=0
    kans=1
    clear()
    print("Je kan op elk moment M invullen bij een vraag om naar de eindingen te kijken die je hebt gehaalt")
    print("je bent net wakker en je hoort een explosie naast je wat ga je doen.\nA. rennen\nB. je blijft staan\nC. je gaat verstoppen")
    v1=input()
    if v1=='A':
        vraag2()
    elif v1=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag1()
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
    elif v2=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag2()
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
    elif v3=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag3()
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
    elif v4=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag4()
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
    elif v5=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag5()
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
    elif v6=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag6()
    else:
        print("incorrect input")
        vraag6()

def vraag7():
    print("je komt veilig aan in Nederland en probeert kennis te maken met de locals waar ga je naar toe\nA. museum\nB. een bar")
    v7=input()
    if v7=='A':
        print("Je bent naar een museum gegaan en hebt veel van de cultuur geleerd ook heb je wat mensen ontmoet")
        einden2()
    elif v7=='B':
        vraag12()
    elif v7=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag7()
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
    elif v8=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag8()
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
        kans=1
        print("Je geeft een goed punt dus je mag weer in de groep\n maar niet iedereen denkt dat je vertrouwbaar bent")
        vraag10()
    elif v9=='C':
        vraag14()
    elif v9=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag9()
    else:
        print("incorrect input")
        vraag9()

def vraag10():
    print("Iedereen gaat stemmen wie de baas wordt van de bunker wordt wat ga je doen?\nA. word een kandidaat\nB. doe niets\nC. stem voor wie jij denkt ")
    v10=input()
    if v10=='A':
        stem(kans)        
    elif v10=='B':
        vraag16()
    elif v10=='C':
        vraag17()
    elif v10=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag10()
    else:
        print("incorrect input")
        vraag10()

def vraag11():
    print("Je hebt een goede verstop plaats gevonden en je wordt niet gevonden\nNa een tijdje hoor je niets meer wat ga je doen\nA. ga zoeken voor de kapitein\nB. wacht tot iedereen weg is\nC. sneak attack")
    v11=input()
    if v11=='A':
        print("Nadat je de kapitein hebt gevonden zijn jullie bijden naar nederland gegaan")
        vraag7()        
    elif v11=='B':
        print("Iedereen is weg maar ook de kapitein dus je zit vast op de boot\nen na een paar dagen ga je van het dek en verdrink je")
        dood()
    elif v11=='C':
        print("Je valt de piraten aan en wordt dood geschoten")
        dood()
    elif v11=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag11()
    else:
        print("incorrect input")
        vraag11()

def vraag12():
    print("Je bent naar een bar gegaan en ookal kan je de taal niet heb je het nog steeds leuk\nnadat je uit de bar komt komt er iemand naar je toe hij vraagt je om geld\nA. geef je geld\nB. val hem aan")
    v12=input()
    if v12=='A':
        print("Je hebt geen geld dus je word neer geschoten")
        dood()        
    elif v12=='B':
        print("Je hebt hem aangevallen en bent weg gaan rennen\n na een tijdje zie je hem niet meer en ben je veilig weg")
        einden2()
    elif v12=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag12()
    else:
        print("incorrect input")
        vraag12()

def vraag13():
    print("Je hebt een afleiding gemaakt en word naar een gevangenis gebracht maar je hebt wel de persoon gered\nNa een paar dagen heb je meerdere ontsnappings plannen maar welke ga je kiezen?\nA. ga va het gat\nB. ga graven onder de muur\nC. ga over het hek ")
    v13=input()
    if v13=='A':
        vraag18()        
    elif v13=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag13()
    elif v13=='B'or'C':
        print("Je bent gesnapt en neergeschoten")
        dood()
    else:
        print("incorrect input")
        vraag13()

def vraag14():
    print("Je hebt niets gezecht dus wat ga je nu doen\nA. zeg weer niks\nB. sorry?")
    v14=input()
    if v14=='A':
        print("De groep vindt dat je weg moet")
        dood()        
    elif v14=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag14()
    elif v14=='B':
        print("Goed gezet?")
        kans=2
        vraag10()
    else:
        print("incorrect input")
        vraag14()

def vraag15():
    print("Je hebt de electies gewonnen maar wat ga je nu doen?\nA. vecht tegen de terroristen\nB. maak een plan om te emigreren\nC. find meer mensen")
    v15=input()
    if v15=='A':
        print("Ook al waren jullie met minder man\nJullie hebben alsnog gewonnen\nJe bent later de president geworden en je leeft een goed leven ")
        einden6()        
    elif v15=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag15()
    elif v15=='B'or'C':
        vraag20()
    else:
        print("incorrect input")
        vraag15()

def vraag16():
    print("Je hebt niets gedaan en de baas van de bunker is een slecht persoon\nHij maakt het zodat je moet werken om weg to komen\n wat ga je doen\nA. doe wat hij zegt\nB. vecht voor je vrijheid")
    v16=input()
    if v16=='A':
        einden4()        
    elif v16=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag16()
    elif v16=='B':
        print("Hij had meer man dan jij en je werd naar buiten gezet en je ging dood")
        dood()
    else:
        print("incorrect input")
        vraag16()

def vraag17():
    print("Je stem heeft geteld en je werkt samen met de baas dus wat ga je nu doen?\nA. vecht tegen de terroristen\nB. maak een plan om te emigreren\nC. find meer mensen")
    v17=input()
    if v17=='A':
        print("Ook al waren jullie met minder man\nJullie hebben alsnog gewonnen\nJe bent later de vice president geworden en je leeft een goed leven ")
        einden6()        
    elif v17=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag17()
    elif v17=='B'or'C':
        vraag20()
    else:
        print("incorrect input")
        vraag17()

def vraag18():
    print("Je bent uit de gevangenis gesnapt en bent terug in de stad wat ga je nu doen\nA. naar de stad\nB. naar het platte land")
    v18=input()
    if v18=='B':
        einden5()        
    elif v18=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag18()
    elif v18=='A':
        print("Je blijft in de stad zoeken en er zijn 3 mogenlijke plaatsen waar je je familie kan vinden waar ga je naar toe\nA. je huis\nB. het gemeentehuis\nC. de signaaltoren")
        vraag21()
    else:
        print("incorrect input")
        vraag18()

def vraag19():
    print("Je hebt de electies niet gewonnen en de baas van de bunker is een slecht persoon\nHij maakt het zodat je moet werken om weg to komen\n wat ga je doen\nA. doe wat hij zegt\nB. vecht voor je vrijheid")
    v19=input()
    if v19=='A':
        einden4()        
    elif v19=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag19()
    elif v19=='B':
        print("Hij had meer man dan jij en je werd naar buiten gezet en je ging dood")
        dood()
    else:
        print("incorrect input")
        vraag19()

def vraag20():
    print("Nudat je de baas bent van de groep ga je zoeken naar meer mensen in de stad\nna een paar uur zoeken vind je je familie en vrienden\niemand van je familie is gewond dus de groep is opgesplitst maar met welke groep ga je\nA. familie\nB. vrienden")
    v20=input()
    if v20=='A':
        vraag22()      
    elif v20=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag20()
    elif v20=='B':
        vraag23()
    else:
        print("incorrect input")
        vraag20()

def vraag21():
    v21=input()
    if v21=='A':
        print("Er zijn terroristen bij je huis en je wordt neer geschoten")
        dood()
    elif v21=='C':
        print("Je hebt ze niet gevonden waar ga je nu naar toe\nA. je huis\nB. het gemeentehuis")
        vraag21      
    elif v21=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag21()
    elif v21=='B':
        vraag24()
    else:
        print("incorrect input")
        vraag21()

def vraag22():
    print("Je bent met je familie naar het ziekenhuis gegaan en hebt medicijn gekregen voor de verwonde familie lid\nje ziet dat je vrienden al weg zijn dus nu moet je zelf een uitzoeken hoe je gaat ontsnappen\nA. met een truck\nB. met een boot")
    v22=input()
    if v22=='A':
        print("De truck werd onderzocht en je bent gepakt")
        dood()
    elif v22=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag22()
    elif v22=='B':
        einden3()
    else:
        print("incorrect input")
        vraag22()

def vraag23():
    print("Jouw familie is naar het ziekenhuis gegaan en waneer ze uit het huis zijn gaan jullie weg\nje hebt twee keuzes om uit te kiezen\nA. met een truck\nB. met een boot")
    v23=input()
    if v23=='B':
        print("De boot werd onderzocht en je bent gepakt")
        dood()
    elif v23=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag22()
    elif v23=='A':
        einden3()
    else:
        print("incorrect input")
        vraag23()

def vraag24():
    print("Nadat je je familie en vrienden vindt in het gemeentehuis\nmaken jullie een plan om naar Nederland te gaan\nA. met een truck\nB. met een boot")
    v24=input()
    if v24=='A':
        print("De truck werd onderzocht en je bent gepakt")
        dood()
    elif v24=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag22()
    elif v24=='B':
        einden3()
    else:
        print("incorrect input")
        vraag22()

def einden2():
    print("Na een paar jaar heb je in Nederland een familie gemaakt en leef je een leuk leven")
    eind2='gehaald'
    eind()

def einden3():
    print("Je komt veilig aan in Nederland en leeft een lang en leuk leven")
    eind3='gehaald'
    eind()

def einden4():
    print("Je zit in een werk kamp van de bunker baas\n3 jaar nadat je bent begonnen ben je vrij\nje bent buiten waar alles anders is en je begint met een familie oprichten")
    eind4='gehaald'
    eind()

def einden5():
    print("Je bent een boer op het platteland\nJe leeft van je eigen planten en hebt niet veel te maken met iedereen anders")
    eind5='gehaald'
    eind()

def einden6():
    eind6='gehaald'
    eind()

def eind():
    restart=input("opnieuw spelen? Y/N: ")
    if restart=='Y':
        vraag1()
    elif restart=='N':
        leven = 0
    elif restart=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag1()
    else:
        print("incorrect input")
        eind()

def dood():
    restart=input("opnieuw spelen? Y/N: ")
    eind1=+1
    if restart=='Y':
        vraag1()
    elif restart=='N':
        leven = 0
    elif restart=='M':
        menu(eind1, eind2, eind3, eind4, eind5, eind6)
        vraag1()
    else:
        print("incorrect input")
        dood()

if leven==1:
    vraag1()
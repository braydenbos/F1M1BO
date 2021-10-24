#Imports
import time
from os import system, name
import random

#Variable junk
kans=0
eind1=0
eind2='niet gehaald'
eind3='niet gehaald'
eind4='niet gehaald'
eind5='niet gehaald'
eind6='niet gehaald'

#Other defs
def menu():
    print(str(eind1)+" keer dood gegaan\nNederland einde1 "+eind2+"\nNederland einde2 "+eind3+"\nSlechte baas "+eind4+"\nBoer einde "+eind5+"\nBaas einde "+eind6)
    input()

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _=system("clear")

def stem():
    clear()
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

def start():
    clear()
    print("Je kan op elk moment M invullen bij een vraag om naar de eindingen te kijken die je hebt gehaalt\nJe kan ook S invullen om het spel stop te zetten")
    input()
    vraag1()

#vragen
def vraag1():
    listOfGlobals = globals()
    listOfGlobals['kans'] =0
    clear()
    print("Je bent net wakker en je hoort een explosie naast je wat ga je doen.\nA. rennen\nB. je blijft staan\nC. je gaat verstoppen")
    v1=input()
    if v1=='A':
        vraag2()
    elif v1=='M':
        menu()
        vraag1()
    elif v1=='S':
        ()
    elif v1=='B':
        clear()
        print("Er is een bom op je huis geland\nEn je hebt het niet overleefd")
        einden1()
    elif v1=='C':
        clear()
        print("Er is een bom op je huis geland\nEn je hebt het niet overleefd")
        einden1()
    else:
        print("Incorrect input")
        input()
        vraag1()

def vraag2():
    clear()
    print("Je hoort een explosie naast je maar je overleeft het wel\nJe denkt snel na en weet dat het niet veilig is waar je nu bent\nDus waar ga je naar toe.\nA. naar de zee\nB. naar het vliegveld\nC. naar een safe house")
    v2=input()
    if v2=='A':
        vraag3()
    elif v2=='B':
        vraag4()
    elif v2=='C':
        vraag5()
    elif v2=='M':
        menu()
        vraag2()
    elif v2=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag2()

def vraag3():
    clear()
    print("Je kiest ervoor om naar de zee te gaan. Er zijn 2 schepen een groot schip maar met veel man \nof een klein schip met minder man.\n1. groot schip\n2. klein schip")
    v3=input()
    if v3=='1':
        vraag6()
    elif v3=='2':
        print("het is misschien een kleine boot maar")
        vraag7()
    elif v3=='M':
        menu()
        vraag3()
    elif v3=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag3()

def vraag4():
    clear()
    print("Je komt aan bij het vlieg veld \n er zijn nog maar 2 vliegtuigen, maar ze zijn allebei druk welke ga je kiezen\nA. vliegtuig dat nu gaat vertrekken\nB. vliegtuig waar je nog tijd voor hebt\nC. wacht tot er een beter vliegtuig komt ")
    v4=input()
    if v4=='A':
        print("")
        vraag7()
    elif v4=='B':
        clear()
        print("de terroristen hebben het vliegtuig neer geschoten")
        einden1()
    elif v4=='C':
        vraag8()
    elif v4=='M':
        menu()
        vraag4()
    elif v4=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag4()

def vraag5():
    clear()
    print("Je komt aan bij de safe house en er zijn een paar anderen mensen\nna een paar dagen horen jullie een explosie buiten wat gaan jullie doen\nA. kijk zelf naar buiten\nB. vraag iemand anders om te kijken\nC. wacht er is waarschijnlijk niets aan de hand")
    v5=input()
    if v5=='A':
        clear()
        print("Je loopt naar buiten en word verbrand door de explosie")
        einden1()
    elif v5=='B':
        vraag9()
    elif v5=='C':
        vraag10()
    elif v5=='M':
        menu()
        vraag5()
    elif v5=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag5()

def vraag6():
    clear()
    print("Je bent op het grote schip gegaan er zijn veel mensen, maar na een paar dagen zijn er veel dood\nOmdat het een groot schip zijn er piraten gekomen om al het geld te stelen dus wat ga je doen\nA. AANVALLEN!\nB. spring van het dek\nC. je verstopt je")
    v6=input()
    if v6=='A':
        clear()
        print("Je probeert de piraten aantevallen maar ze hebben geweren dus je wordt neergeschoten")
        einden1()
    elif v6=='B':
        clear()
        print("Je springt van het dek maar je zit op het midden van de oceaan dus je verdrinkt")
        einden1()
    elif v6=='C':
        vraag11()
    elif v6=='M':
        menu()
        vraag6()
    elif v6=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag6()

def vraag7():
    clear()
    print("je komt veilig aan in Nederland en probeert kennis te maken met de locals waar ga je naar toe\nA. museum\nB. een bar")
    v7=input()
    if v7=='A':
        clear()
        print("Je bent naar een museum gegaan en hebt veel van de cultuur geleerd ook heb je wat mensen ontmoet")
        einden2()
    elif v7=='B':
        vraag12()
    elif v7=='M':
        menu()
        vraag7()
    elif v7=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag7()

def vraag8():
    clear()
    print("Je bent op het vlieg veld aan het wachten wanner je het 2e vliegtuig ziet neerstorten gelukkig heb je gekozen om hier te blijven\nNa een paar uur wachten zie je de terroristen iemand gavangen houden wat ga je doen?\nA. val de terroristen aan\nB. maak een afleiding\nC. ren weg")
    v8=input()
    if v8=='A':
        clear()
        print("Je valt de terroristen aan maar je wordt neergeschoten")
        einden1()
    elif v8=='B':
        vraag13()
    elif v8=='C':
        vraag5()
    elif v8=='M':
        menu()
        vraag8()
    elif v8=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag8()

def vraag9():
    clear()
    print("Iedereen kijkt je aan met bozen ogen ze zeggen dat jij de reden bent dat hij dood is\nWat ga je doen om hun beter te laten voelen\nA. zeg dat je niks fout hebt gedaan\nB. zeg dat je je schuldig vind en dat je het recht gaat zeggen\nC. zeg niks")
    v9=input()
    if v9=='A':
        clear()
        print("Je moet weg en gaat dood door de radio actiefe stralingen")
        einden1()
    elif v9=='B':
        listOfGlobals = globals()
        listOfGlobals['kans'] =1
        print("Je geeft een goed punt dus je mag weer in de groep\n maar niet iedereen denkt dat je vertrouwbaar bent")
        vraag10()
    elif v9=='C':
        vraag14()
    elif v9=='M':
        menu()
        vraag9()
    elif v9=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag9()

def vraag10():
    clear()
    print("Iedereen gaat stemmen wie de baas wordt van de bunker wordt wat ga je doen?\nA. word een kandidaat\nB. doe niets\nC. stem voor wie jij denkt ")
    v10=input()
    if v10=='A':
        stem()        
    elif v10=='B':
        vraag16()
    elif v10=='C':
        vraag17()
    elif v10=='M':
        menu()
        vraag10()
    elif v10=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag10()

def vraag11():
    clear()
    print("Je hebt een goede verstop plaats gevonden en je wordt niet gevonden\nNa een tijdje hoor je niets meer wat ga je doen\nA. ga zoeken voor de kapitein\nB. wacht tot iedereen weg is\nC. sneak attack")
    v11=input()
    if v11=='A':
        print("Nadat je de kapitein hebt gevonden zijn jullie bijden naar nederland gegaan")
        vraag7()        
    elif v11=='B':
        clear()
        print("Iedereen is weg maar ook de kapitein dus je zit vast op de boot\nen na een paar dagen ga je van het dek en verdrink je")
        einden1()
    elif v11=='C':
        clear()
        print("Je valt de piraten aan en wordt dood geschoten")
        einden1()
    elif v11=='M':
        menu()
        vraag11()
    elif v11=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag11()

def vraag12():
    clear()
    print("Je bent naar een bar gegaan en ookal kan je de taal niet heb je het nog steeds leuk\nnadat je uit de bar komt komt er iemand naar je toe hij vraagt je om geld\nA. geef je geld\nB. val hem aan")
    v12=input()
    if v12=='A':
        clear()
        print("Je hebt geen geld dus je word neer geschoten")
        einden1()        
    elif v12=='B':
        clear()
        print("Je hebt hem aangevallen en bent weg gaan rennen\n na een tijdje zie je hem niet meer en ben je veilig weg")
        einden2()
    elif v12=='M':
        menu()
        vraag12()
    elif v12=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag12()

def vraag13():
    clear()
    print("Je hebt een afleiding gemaakt en word naar een gevangenis gebracht maar je hebt wel de persoon gered\nNa een paar dagen heb je meerdere ontsnappings plannen maar welke ga je kiezen?\nA. ga va het gat\nB. ga graven onder de muur\nC. ga over het hek ")
    v13=input()
    if v13=='A':
        vraag18()        
    elif v13=='M':
        menu()
        vraag13()
    elif v13=='S':
        ()
    elif v13=='B':
        clear()
        print("Je bent gesnapt en neergeschoten")
        einden1()
    elif v13=='C':
        clear()
        print("Je bent gesnapt en neergeschoten")
        einden1()
    else:
        print("Incorrect input")
        input()
        vraag13()

def vraag14():
    clear()
    print("Je hebt niets gezecht dus wat ga je nu doen\nA. zeg weer niks\nB. sorry?")
    v14=input()
    if v14=='A':
        clear()
        print("De groep vindt dat je weg moet")
        einden1()        
    elif v14=='B':
        print("Goed gezet?")
        listOfGlobals = globals()
        listOfGlobals['kans'] =2
        vraag10()
    elif v14=='M':
        menu()
        vraag14()
    elif v14=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag14()

def vraag15():
    print("Je hebt de electies gewonnen maar wat ga je nu doen?\nA. vecht tegen de terroristen\nB. maak een plan om te emigreren\nC. find meer mensen")
    v15=input()
    if v15=='A':
        clear()
        print("Ook al waren jullie met minder man\nJullie hebben alsnog gewonnen\nJe bent later de president geworden en je leeft een goed leven ")
        einden6()        
    elif v15=='M':
        menu()
        vraag15()
    elif v15=='S':
        ()
    elif v15=='B'or'C':
        vraag20()
    else:
        print("Incorrect input")
        input()
        vraag15()

def vraag16():
    clear()
    print("Je hebt niets gedaan en de baas van de bunker is een slecht persoon\nHij maakt het zodat je moet werken om weg to komen\n wat ga je doen\nA. doe wat hij zegt\nB. vecht voor je vrijheid")
    v16=input()
    if v16=='A':
        clear()
        einden4()        
    elif v16=='B':
        clear()
        print("Hij had meer man dan jij en je werd naar buiten gezet en je ging dood")
        einden1()
    elif v16=='M':
        menu()
        vraag16()
    elif v16=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag16()

def vraag17():
    clear()
    print("Je stem heeft geteld en je werkt samen met de baas dus wat ga je nu doen?\nA. vecht tegen de terroristen\nB. maak een plan om te emigreren\nC. find meer mensen")
    v17=input()
    if v17=='A':
        clear()
        print("Ook al waren jullie met minder man\nJullie hebben alsnog gewonnen\nJe bent later de vice president geworden en je leeft een goed leven ")
        einden6()        
    elif v17=='M':
        menu()
        vraag17()
    elif v17=='S':
        ()
    elif v17=='B'or'C':
        vraag20()
    else:
        print("Incorrect input")
        input()
        vraag17()

def vraag18():
    clear()
    print("Je bent uit de gevangenis gesnapt en bent terug in de stad wat ga je nu doen\nA. naar de stad\nB. naar het platte land")
    v18=input()
    if v18=='A':
        print("Je blijft in de stad zoeken en er zijn 3 mogenlijke plaatsen waar je je familie kan vinden waar ga je naar toe\nA. je huis\nB. het gemeentehuis\nC. de signaaltoren")
        vraag21()
    elif v18=='B':
        clear()
        einden5()        
    elif v18=='M':
        menu()
        vraag18()
    elif v18=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag18()

def vraag19():
    print("Je hebt de electies niet gewonnen en de baas van de bunker is een slecht persoon\nHij maakt het zodat je moet werken om weg to komen\nWat ga je doen\nA. doe wat hij zegt\nB. vecht voor je vrijheid")
    v19=input()
    if v19=='A':
        clear()
        einden4()        
    elif v19=='B':
        clear()
        print("Hij had meer man dan jij en je werd naar buiten gezet en je ging dood")
        einden1()
    elif v19=='M':
        menu()
        vraag19()
    elif v19=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag19()

def vraag20():
    clear()
    print("Nudat je de baas bent van de groep ga je zoeken naar meer mensen in de stad\nna een paar uur zoeken vind je je familie en vrienden\niemand van je familie is gewond dus de groep is opgesplitst maar met welke groep ga je\nA. familie\nB. vrienden")
    v20=input()
    if v20=='A':
        vraag22()      
    elif v20=='B':
        vraag23()
    elif v20=='M':
        menu()
        vraag20()
    elif v20=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag20()

def vraag21():
    clear()
    v21=input()
    if v21=='A':
        clear()
        print("Er zijn terroristen bij je huis en je wordt neer geschoten")
        einden1()
    elif v21=='B':
        vraag24()
    elif v21=='C':
        print("Je hebt ze niet gevonden waar ga je nu naar toe\nA. je huis\nB. het gemeentehuis")
        vraag21      
    elif v21=='M':
        menu()
        vraag21()
    elif v21=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag21()

def vraag22():
    clear()
    print("Je bent met je familie naar het ziekenhuis gegaan en hebt medicijn gekregen voor de verwonde familie lid\nje ziet dat je vrienden al weg zijn dus nu moet je zelf een uitzoeken hoe je gaat ontsnappen\nA. met een truck\nB. met een boot")
    v22=input()
    if v22=='A':
        clear()
        print("De truck werd onderzocht en je bent gepakt")
        einden1()
    elif v22=='B':
        clear()
        einden3()
    elif v22=='M':
        menu()
        vraag22()
    elif v22=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag22()

def vraag23():
    clear()
    print("Jouw familie is naar het ziekenhuis gegaan en waneer ze uit het huis zijn gaan jullie weg\nje hebt twee keuzes om uit te kiezen\nA. met een truck\nB. met een boot")
    v23=input()
    if v23=='A':
        clear()
        einden3()
    elif v23=='B':
        clear()
        print("De boot werd onderzocht en je bent gepakt")
        einden1()
    elif v23=='M':
        menu()
        vraag22()
    elif v23=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag23()

def vraag24():
    clear()
    print("Nadat je je familie en vrienden vindt in het gemeentehuis\nmaken jullie een plan om naar Nederland te gaan\nA. met een truck\nB. met een boot")
    v24=input()
    if v24=='A':
        clear()
        print("De truck werd onderzocht en je bent gepakt")
        einden1()
    elif v24=='B':
        clear()
        einden3()
    elif v24=='M':
        menu()
        vraag22()
    elif v24=='S':
        ()
    else:
        print("Incorrect input")
        input()
        vraag22()

#Eindes
def einden1():
    listOfGlobals = globals()
    listOfGlobals['eind1']+=1
    einde()

def einden2():
    print("Na een paar jaar heb je in Nederland een familie gemaakt en leef je een leuk leven")
    listOfGlobals = globals()
    listOfGlobals['eind2'] ='gehaald'
    einde()

def einden3():
    print("Je komt veilig aan in Nederland en leeft een lang en leuk leven")
    listOfGlobals = globals()
    listOfGlobals['eind3'] ='gehaald'
    einde()

def einden4():
    print("Je zit in een werk kamp van de bunker baas\n3 jaar nadat je bent begonnen ben je vrij\nje bent buiten waar alles anders is en je begint met een familie oprichten")
    listOfGlobals = globals()
    listOfGlobals['eind4'] ='gehaald'
    einde()

def einden5():
    print("Je bent een boer op het platteland\nJe leeft van je eigen planten en hebt niet veel te maken met iedereen anders")
    listOfGlobals = globals()
    listOfGlobals['eind5'] ='gehaald'
    einde()

def einden6():
    listOfGlobals = globals()
    listOfGlobals['eind6'] ='gehaald'
    einde()

def einde():
    restart=input("opnieuw spelen? Y/N: ")
    if restart=='Y':
        vraag1()
    elif restart=='N':
        ()
    elif restart=='M':
        menu()
        vraag1()
    else:
        print("Incorrect input")
        input()
        einde()

#Start code
start()
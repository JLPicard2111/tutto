import pandas as pd
import random
import numpy as n
from helpers.classes import Würfel
import helpers.functions as f

random.seed()

# globale Variablen:
w = 1
currRoll = 1 #Wurfanzahl
würfelliste = []
totalScore = 0


print("+++++++++ Programmstart +++++++++++++++++++")

# beim Ersten Wurf ausführen:
while True:
    currScore = 0

    # 6 Würfel werfen
    würfelliste = f.rollTheDice(würfelliste)

    print(f"_____________________ WURF {currRoll} ________________________ ")
    # Dictionary erstellen mit den geworfenen Werten
    valueCount = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}

    # Würfelaugen zählen und dem Dictionary hinzufügen
    for dice in würfelliste:
        if dice.thrown == 1:
            currValue = str(dice.value)
            #print(f"Aktueller Wert: {currValue}")
            valueCount[currValue] = valueCount[currValue] + 1
    currScore = f.getScores(valueCount)
    print(f"Gezählte Werte: {valueCount}")
    print('----------------------')
    
    if currScore > 0:
        print(f"Das ist dein {currRoll}. Wurf und deine erzielte Punktzahl ist: {currScore}")
    else:
        print(f"Leider hast du keine gültigen Würfel und die Runde ist beendet!")
        break
    
    print("=============== Prüfung ==============================")

    # Prüfen, welche Würfel gültig sind und gehalten werden können
    # vorher alle Keep werte auf 0 setzen
    for dice in würfelliste:
        dice.keep = 0
        dice.setValidity(valueCount)
        if dice.thrown == 1:
            if dice.valid == 1:
                print(f"Der Würfel {dice.id} hat den Wert {dice.value} und ist gültig")
            else:
                print(f"Der Würfel {dice.id} hat den Wert {dice.value} und ist damit leider nicht gültig")
    
    if f.isTutto(würfelliste):
        print("--------------------TUTTO TUTTO TUTTO------------------")
        
    print('============= Entscheidung ==============================')
    for dice in würfelliste:
        if dice.valid == 1 and dice.thrown == 1:
            while True:
                result = input(f"Möchtest du den Würfel {dice.id} mit dem Wert {dice.value} behalten?")
                if f.correctYesNoAnswer(result):
                    dice.setKeep()
                    break
                else:
                    print("Leider war das keine gültige Ja/Nein Antwort. Bitte versuche es noch einmal!")
                    continue

    counter = 0
    for dice in würfelliste:
        dice.thrown = 0
        if dice.keep == 1:
            dice.thrownPast = 1
            counter += 1

    print(f"Bravo! Du behältst {counter} Würfel und hast {currScore} Punkte damit erzielt!")
    totalScore = totalScore + currScore
    print(f"Aktuelle Gesamtpunktzahl: {totalScore}")
    if currScore != 0:
        # hier muss der User entscheiden, ob er überhaupt weitermacht!
        exit = input("Möchtest du mit den verbliebenden Würfeln weiterspielen?")
        if exit.lower() == "ja":
            currRoll += 1
            continue
        else:
            #Hier muss sich jetzt bedankt werden und der Total Score Wert muss irgendwie weggeschrieben werden
            if totalScore > 0:
                print(f"Bravo! Du hast die Runde erfolgreich beendet und insgesamt {totalScore} Punkte erzielt")
            else:
                print("Die Runde ist beendet aber leider hast du keine Punkte erzielt!")
            break    
    else:
        totalScore = 0
        currScore = 0
        print(f"Leider war der Wurf ungültig und die Punkte sind verloren")
        break


print("!!!!!!!!!!!!!!!!!!!!! RUNDENENDE !!!!!!!!!!!!!!!!!!!")






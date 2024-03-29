from helpers.classes import Würfel
import random


def getScores(values):
    score = 0
    if isinstance(values, dict):
        for key, value in values.items():
            key = int(key)
            if key in (1,5):
                if value < 3:
                    if key == 1:
                        score = score + ((key * value) * 100)
                    else:
                        score = score + ((key * value) * 10)
                else:
                    if key == 1:
                        score = score + 1000
                    else:
                        score = score + 500
            else:
                if value < 3:
                    score = score + 0
                else:
                    score = score + (key * 100)
        return score
    else:
        return 0

def correctYesNoAnswer(reply):
    if reply.lower() in ("ja", "yes", "jawoll", "na gut", "nein", "nö", "njiet", "lieber nicht"):
        return True
    else:
        return False

def rollTheDice(würfelliste):
    w = 1
    random.seed()
    
    if len(würfelliste) == 0:
    # 1. Wurf, das Dictionary ist leer
        while w <= 6:
            dice = Würfel(w, random.randrange(1,7),0,1,0,1)
            würfelliste.append(dice)
            w += 1
    else:
    # 2. Wurf: Nur die Würfeln, die in keep eine 0 haben
        for dice in würfelliste:
            if dice.keep == 0 and dice.thrownPast == 0:
                newDice = Würfel(dice.id, random.randrange(1,7),0,0,0,1)
                dice.value = newDice.value
                dice.setThrown()
                
    return würfelliste

def isTutto(dices):
    counter = 0
    for dice in dices:
        if dice.valid == 1:
            counter += 1
    if counter == 6:
        return True
    else:
        return False


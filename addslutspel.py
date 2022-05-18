from random import randint

def slutspel(savedsum, dice4, dice5):
    r = 1000000                 # antalet gånger simulationen ska köras
    savedsum += dice4       # de sparade tärningarnas summa med 4e tärningen

    wins = 0
    losses = 0

    for i in range(r):
        dice6 = randint(1, 6)                   # slår 6e tärningen
        #print("hitting dice6:", dice6)
        #print("savedsum:", savedsum + dice5 + dice6)
        if savedsum + dice5 + dice6 >= 30:      # om man når 30
            wins += 1
            #print("wins:", wins, "\n")
        elif savedsum + dice5 + dice6 < 30:     # om man inte når 30
            losses += 1
            #print("losses:", losses, "\n")

    savewinrate = round(wins / r * 100, 2)            # sannolikheten att vinna om man sparar 5e tärningen
    savelossrate = losses / r * 100         # sannolikheten att förlora

    # om man slår om 5:e tärningen
    #print("hit\n")
    wins = 0
    losses = 0

    for i in range(r):
        dice5 = randint(1, 6)                   # slår om 5e och 6e tärningen
        dice6 = randint(1, 6)
        #print("try 1:")
        #print("hitting dice5:", dice5)
        #print("hitting dice6:", dice6)
        #print("savedsum:", savedsum + dice5 + dice6)
        if savedsum + dice5 + dice6 >= 30:      # om man når 30
            wins += 1
            #print("wins:", wins, "\n")
        elif savedsum + dice5 + dice6 < 30:     # om man inte når 30
            #print("2.")
            if dice5 < dice6:
                dice5 = randint(1, 6)
                #print("saving one dice:", dice6)
                #print("hitting the other:", dice5)
            else:
                dice6 = randint(1, 6)           # spara en tärning, slå om den andra
                #print("saving one dice:", dice5)
                #print("hitting the other:", dice6)
            #print("savedsum", savedsum + dice5 + dice6)
            if savedsum + dice5 + dice6 >= 30:
                wins += 1
                #print("wins:", wins, "\n")
            elif savedsum + dice5 + dice6 < 30:
                losses += 1
                #print("losses:", losses, "\n")

    hitwinrate = round(wins / r * 100, 2)             # sannolikheten att vinna om man slår om 5e och 6e tärningen
    hitlossrate = losses / r * 100          # sannolikheten att förlora

    # statistik för om man sparar 5e tärningen
    print("\nSavewinrate: {}%".format(savewinrate))
    #print("Savelossrate: {:.2f}%".format(savelossrate))

    # statistik för om man slår om 5e och 6e tärningen
    print("\nHitwinrate: {}%".format(hitwinrate))
    #print("Hitlossrate: {:.2f}%\n".format(hitlossrate))

    if savewinrate > hitwinrate:        # om man har störst chans att vinna genom att spara
        #print("Action: Save\n")
        return "save"
    elif savewinrate < hitwinrate:      # om man har störst chans att vinna genom att slå om
        #print("Action: Hit\n")
        return "hit"
    else:                               # om sannolikheten är lika stor
        #print("Action: -\n")
        return "save"

slutspel(18, 2, 5)
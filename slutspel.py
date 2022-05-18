from random import randint

r = 1000000             # antalet gånger simulationen ska köras
savedsum = 24           # de sparade tärningarnas summa med 4e tärningen
dice5 = 5               # den 5:e tärningens värde som man kan välja att spara eller ej

print(r, savedsum, dice5)

wins = 0
losses = 0

for i in range(r):
    dice6 = randint(1, 6)                   # slår 6e tärningen
    if savedsum + dice5 + dice6 >= 30:      # om man når 30
        wins += 1
    elif savedsum + dice5 + dice6 < 30:     # om man inte når 30
        losses += 1

savewinrate = wins / r * 100            # sannolikheten att vinna om man sparar 5e tärningen
savelossrate = losses / r * 100         # sannolikheten att förlora

wins = 0
losses = 0

for i in range(r):
    dice5 = randint(1, 6)                   # slår om 5e och 6e tärningen
    dice6 = randint(1, 6)
    if savedsum + dice5 + dice6 >= 30:      # om man når 30 / instant win
        wins += 1
    elif savedsum + dice5 + dice6 < 30:     # om man inte når 30
        if dice5 < dice6:
            dice5 = randint(1, 6)
        else:
            dice6 = randint(1, 6)               # spara en tärning, slå om den andra
        if savedsum + dice5 + dice6 >= 30:
            wins += 1
        elif savedsum + dice5 + dice6 < 30:
            losses += 1

hitwinrate = wins / r * 100             # sannolikheten att vinna om man slår om 5e och 6e tärningen
hitlossrate = losses / r * 100          # sannolikheten att förlora

# statistik för om man sparar 5e tärningen
print("\nSavewinrate: {}%".format(round(savewinrate, 2)))
print("Savelossrate: {}%".format(round(savelossrate, 2)))

# statistik för om man slår om 5e och 6e tärningen
print("\nHitwinrate: {}%".format(round(hitwinrate, 2)))
print("Hitlossrate: {}%\n".format(round(hitlossrate, 2)))

if savewinrate > hitwinrate:        # om man har störst chans att vinna genom att spara
    print("Action: Save")
elif savewinrate < hitwinrate:      # om man har störst chans att vinna genom att slå om
    print("Action: Hit")
else:                               # om sannolikheten är lika stor
    print("Action: -")

"""100000 21 3

Savewinrate: 16.84%
Savelossrate: 83.17%

Hitwinrate: 27.82%
Hitlossrate: 72.19%

Actiom: Hit"""

"""100000 21 3

Savewinrate: 16.68%
Savelossrate: 83.33%

Hitwinrate: 41.67%
Hitlossrate: 58.33%

Actiom: Hit"""
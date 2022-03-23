from random import randint

r = 1000000    # antalet omgångar som ska spelas

wins = 0
losses = 0

for j in range(r):
    dicesnr = 6     # nollställer värden
    savedsum = 0

    while dicesnr > 0:      # när det finns tärningar kvar att slå
        throwndices = []    # kastade tärningar
        savedices = []      # tärningar som ska läggas undan i detta kast

        for i in range(dicesnr):                    # slår tärningar
            throwndices.append(randint(1, 6))       # lägger till de i listan

        if savedsum + sum(throwndices) >= 30:       # om man når till 30 på detta kast
            savedsum += sum(throwndices)            # vinst
            dicesnr = 0                             # avbryt loopen

        else:                                                       # om man inte är klar
            for i in range(len(throwndices)):                       # kolla alla tärningar
                if throwndices[i] == 5 or throwndices[i] == 6:      # kolla efter femmor och sexor
                    savedices.append(throwndices[i])                # lägg undan femmor och sexor

            if len(savedices) == 0:                     # om det inte finns några femmor eller sexor
                savedices.append(max(throwndices))      # lägg undan tärningen med högst värde

            for i in savedices:     # spara alla undanlagda tärningar
                savedsum += i

            dicesnr -= len(savedices)       # kasta inte om undanlagda tärningar

    if savedsum >= 30:      # när alla tärningar har sparats
        wins += 1
    else:
        losses += 1

winrate = round(wins / r * 100, 2)
lossrate = round(losses / r * 100, 2)

print("\nWinrate: {}%".format(winrate))
print("Lossrate: {}%".format(lossrate))

results1000000 = "Winrate: 53.89%, Lossrate: 46.11%"
results10000000 = "Winrate: 53.93%, Lossrate: 46.07%"

results1000000_luck = "Winrate: 60.78%, Lossrate: 39.22%"
results10000000_luck = "Winrate: 60.81%, Lossrate: 39.19%"
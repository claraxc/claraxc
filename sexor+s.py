from random import randint
import addslutspel2

r = 10000000   # antalet omgångar som ska spelas

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

        #print("savedsum " + str(savedsum))
        #print("dicesnr", dicesnr)
        #print("throwndices: ", end="")
        #print(throwndices)

        if savedsum + sum(throwndices) >= 30:       # om man når till 30 på detta kast
            #print("instant win")
            savedsum += sum(throwndices)            # vinst
            dicesnr = 0                             # avbryt loopen

        else:                                           # om man inte är klar
            if dicesnr == 3:                            # om slutspelet ska köras
                throwndices.sort(reverse=True)
                simresult = addslutspel2.slutspel(savedsum, throwndices[0], throwndices[1])
                if simresult == "save":
                    savedices.append(throwndices[1])
                savedices.append(throwndices[0])
            else:
                for i in range(len(throwndices)):           # kolla alla tärningar
                    if throwndices[i] == 6:                 # kolla efter sexor
                        savedices.append(throwndices[i])    # lägg undan sexor

                if len(savedices) == 0:                     # om det inte finns några sexor
                    savedices.append(max(throwndices))      # lägg undan tärningen med högst värde

            for i in savedices:     # spara alla undanlagda tärningar
                savedsum += i

            dicesnr -= len(savedices)       # kasta inte om undanlagda tärningar
            #print("savedices:", savedices, "\n")

    if savedsum >= 30:      # när alla tärningar har sparats
        wins += 1
    else:
        losses += 1

winrate = round(wins / r * 100, 2)
lossrate = round(losses / r * 100, 2)

print("\nWinrate: {}%".format(winrate))
print("Lossrate: {}%".format(lossrate))

results10000_10000luck = "Winrate: 67.27%, Lossrate: 32.73%"
results100000_1000luck = "Winrate: 67.32%, Lossrate: 32.68%%"
results1000000_100luck = "Winrate: 67.33%, Lossrate: 32.67%"


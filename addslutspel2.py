def slutspel(savedsum, dice4, dice5):
    savedsum += dice4          # de sparade tärningarnas summa med 4e tärningen

    if savedsum < 18:
        return "hit"
    elif savedsum <= 22:
        if dice5 <= 5:
            return "hit"
        elif dice5 == 6:
            return "save"
    elif savedsum > 22:
        if dice5 <= 4:
            return "hit"
        elif dice5 >= 5:
            return "save"

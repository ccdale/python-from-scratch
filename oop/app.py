# import oop.things as th
#
# mything = th.Thing()

from oop.hangman import Hangman

hm = Hangman("This is a phrase to be guessed")

while True:
    didwewin = hm.askQ("wibble")
    if didwewin:
        if hm.score < hm.maxtries:
            print(
                f"{hm.score}/{hm.maxtries}: hurrah, you win: the phrase was {hm.phrase}\n\n"
            )
            break
            # WE WON
    elif hm.score > hm.maxtries:
        print(
            f"{hm.score}/{hm.maxtries}: Sorry you lose\nThe correct phrase is\n     {hm.phrase}\n\n"
        )
        break
    print(f"{hm.score}/{hm.maxtries}")

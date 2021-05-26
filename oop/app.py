# import oop.things as th
#
# mything = th.Thing()

from oop import Hangman

hm = Hangman("This is a phrase to be guessed")

while True:
    didwewin = hm.askQ("wibble")
    if didwewin:
        if hm.score < hm.maxtries:
            break
            # WE WON
    elif hm.score > hm.maxtries:
        break

# import oop.things as th
#
# mything = th.Thing()

import random

from oop.hangman import Hangman

phrases = ["phrase number one", "phrase number two", "phrase number six"]
phrase = random.choice(phrases)

hm = Hangman(phrase)

while True:
    didwewin = hm.askQ("guess a letter or the whole phrase")
    if didwewin:
        if hm.score < hm.maxtries:
            print(
                f"{hm.score}/{hm.maxtries}: hurrah, you win: the phrase was {hm.phrase}\n\n"
            )
            break
            # WE WON
    elif hm.score >= hm.maxtries:
        print(
            f"{hm.score}/{hm.maxtries}: Sorry you lose\nThe correct phrase is\n     {hm.phrase}\n\n"
        )
        break
    print(f"{hm.score}/{hm.maxtries}\n")

#!/usr/bin/env python3
"""Application to play the Coundown letters game."""

import random
import sys

from anagrams import testWord
from buildwordlist import onlyInWords
from buildwordlist import readWordList
from buildwordlist import sortWordsByLetter


def rndLetter(vowel=False):
    letters = [chr(x) for x in range(ord("a"), ord("z") + 1)]
    vowels = ["a", "e", "i", "o", "u"]
    cons = [x for x in letters if x not in vowels]
    lst = vowels if vowel else cons
    return random.choice(lst)


def askMe(q, default):
    """Input routine for the console.

    Args:
        q: str input question
        default: str default answer

    Raises:
        TypeError: if input `q` is not a string

    Returns:
        str: user input or default
    """
    try:
        if type(q) is not str:
            raise TypeError("Input error, question is not a string.")
        ret = default
        val = input(f"{q} ({default}) > ")
        if len(val) > 0:
            ret = val
        return ret
    except Exception as e:
        fname = sys._getframe().f_code.co_name
        msg = f"Exception in {fname}:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


def outputCheck(check):
    """Outputs the check list prettily."""
    # for each letter turn it into it's upper case equivelent
    # seperate each letter with " . "
    xstr = " . ".join([x.upper() for x in check])
    if len(xstr) > 0:
        print(f"\n{xstr}\n")


def countdown():
    try:
        words = readWordList("brit-a-z.txt", 4, 9)
        swords = sortWordsByLetter(words)
        # make a list of all letters from a-z (all lowercase)
        letters = [chr(x) for x in range(ord("a"), ord("z") + 1)]
        # the check list
        check = []
        # instructions
        msg = "Input a letter or a number\n"
        msg += "1 - random consonent\n"
        msg += "2 - random vowel\n"
        msg += ">2 is the number of consonents in the output:\n"
        msg += "i.e.: 6 will give 6 consonents and 3 vowels."
        # loop until we have 9 letters
        while len(check) < 9:
            outputCheck(check)
            letter = askMe(msg, "6")
            # ensure if it is a letter that it is lower case
            letter = letter.lower()
            if letter in letters:
                check.append(letter)
            elif letter == "1":
                check.append(rndLetter())
            elif letter == "2":
                check.append(rndLetter(True))
            else:
                # this will fail hard if letter cannot be coerced into a number
                i = int(letter)
                v = 9 - i
                for x in range(i):
                    check.append(rndLetter())
                for x in range(v):
                    check.append(rndLetter(True))
        print()
        outputCheck(check)
    except Exception as e:
        msg = "Exception in countdown:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


if __name__ == "__main__":
    print(rndLetter())
    print(rndLetter(True))
    countdown()

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


def countdown():
    try:
        words = readWordList("brit-a-z.txt", 4, 9)
        swords = sortWordsByLetter(words)
    except Exception as e:
        msg = "Exception in countdown:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


if __name__ == "__main__":
    print(rndLetter())
    print(rndLetter(True))

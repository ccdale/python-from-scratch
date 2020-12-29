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


def autoGenerateCheck(cn):
    """Generate a random sequence of 9 letters, with `cn` number of consonents.

    args: cn - int - number of consonents in ouput

    returns: str
    """
    try:
        # the check list
        check = []
        # this will fail hard if cn is not a number.
        i = int(cn)
        v = 9 - i
        for x in range(i):
            check.append(rndLetter())
        for x in range(v):
            check.append(rndLetter(True))
        # so that we don't have a nice demarcation between vowels
        # and consonents, convert check to a list, shuffle it a
        # couple of times and convert it back to a string.
        xchk = list(check)
        for x in range(5):
            random.shuffle(xchk)
        check = "".join(xchk)
        return check
    except Exception as e:
        msg = "Exception in autoGenerateCheck:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


def generateCheck():
    try:
        # make a list of all letters from a-z (all lowercase)
        letters = [chr(x) for x in range(ord("a"), ord("z") + 1)]
        nums = [chr(x) for x in range(ord("3"), ord("9"))]
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
            elif letter in nums:
                check = autoGenerateCheck(int(letter))
            else:
                raise Exception(f"dodgy input detected: {letter}")
        return check
    except Exception as e:
        msg = "Exception in generateCheck:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


def countLists(xdict):
    try:
        # set up a totals counter
        tn = 0
        for length in xdict:
            if type(xdict[length]) is dict:
                for letter in xdict[length]:
                    tn += len(xdict[length][letter])
            elif type(xdict[length]) is list:
                tn += len(xdict[length])
        return tn
    except Exception as e:
        msg = "Exception in countLists:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


def findAnagram(check, words):
    try:
        # remove duplicate letters for looping purposes
        op = None
        found = False
        mx = 0
        chk = set(check)
        for length in words:
            for word in words[length]:
                if testWord(word, check):
                    if length > mx:
                        mx = length
                        op = word
                    # special case, if we find a nine letter word, stop
                    # checking immediately.
                    if length == 9:
                        found = True
                        break
            if found:
                break
        return op
    except Exception as e:
        msg = "Exception in findAnagram:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


def countdown():
    try:
        words = readWordList("brit-a-z.txt", 4, 9)
        tn = countLists(words)
        print(f"total words after sorting by length: {tn:,}")
        swords = sortWordsByLetter(words)
        tn = countLists(swords)
        print(f"total words after sub-sorting by letter: {tn:,}")
        check = generateCheck()
        cwords = onlyInWords(swords, check)
        tn = countLists(cwords)
        print(f"total words to check after input of anagram: {tn:,}")
        print()
        outputCheck(check)
        word = findAnagram(check, cwords)
        if word is not None:
            cn = len(word)
            print(f"Found a {cn} letter word: {word}")
        else:
            print("Failed to find a word, sorry")
    except Exception as e:
        msg = "Exception in countdown:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


if __name__ == "__main__":
    # print(rndLetter())
    # print(rndLetter(True))
    countdown()

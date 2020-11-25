#!/usr/bin/env python3
"""Code to generate passwords."""

import random

from lesson3 import phoneticAlphabet

# word list
# random choice
# concatenation
# obfuscation
# hashing


def capitalise(word):
    char = word[0:1]
    return char.upper()


def randomWord(wordlist):
    word = random.choice(wordlist)
    word = word.strip()
    return word


def phoneticAl2(msg):
    d = {
            "A": "Alpha",
            "B": "Bravo",
            "C": "Charlie",
            "D": "Delta",
            "E": "Echo",
            "F": "Foxtrot",
            "G": "Golf",
            "H": "Hotel",
            "I": "India",
            "J": "Juliet",
            "K": "Kilo",
            "L": "Lima",
            "M": "Mike",
            "N": "November",
            "O": "Oscar",
            "P": "Papa",
            "Q": "Quebec",
            "R": "Romeo",
            "S": "Sierra",
            "T": "Tango",
            "U": "Uniform",
            "V": "Victor",
            "W": "Whiskey",
            "X": "X-ray",
            "Y": "Yankee",
            "Z": "Zulu"
            }
    lop = []
    for letter in msg:
        xl = d.get(letter.upper(), letter)
        if letter.upper() == letter:
            lop.append("Capital " + xl)
        else:
            lop.append(xl)
    op = " . ".join(lop)
    # op = " . ".join(d.get(letter.upper(), letter) for letter in msg)
    return op


def genpw():
    with open("wordlist.txt", "r") as ifn:
        # returns a list of the lines in the file, including the newline at the
        # end of each line.
        wlist = ifn.readlines()
    # the file will now be automatically closed when python hits this line

    # word = random.choice(wlist)
    # words = []
    # for i in range(4):
    #     newword = randomWord(wlist)
    #     words.append(newword)

    # print(words)

    pwlist = []
    # line 41 is functionally equivelent to lines 31 - 35
    twords = [randomWord(wlist) for i in range(4)]
    for word in twords:
        xw = capitalise(word)
        yw = word[1:]
        pwlist.append("".join([xw, yw]))
    pw = "".join(pwlist)
    print(pw)
    # print(phoneticAlphabet(pw))
    print(phoneticAl2(pw))


if __name__ == "__main__":
    genpw()

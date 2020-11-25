#!/usr/bin/env python3
"""Code to generate passwords."""

import random

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


if __name__ == "__main__":
    genpw()

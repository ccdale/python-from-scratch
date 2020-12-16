"""The password object."""

import os
import random


class Password():
    def __init__(self, wordlistFilename):
        self.wordlistfilename = wordlistFilename
        self.wordlist = None
        self.readFile()

    def readFile(self):
        if os.path.exists(self.wordlistfilename):
            with open(self.wordlistfilename, "r") as ifn:
                self.wordlist = ifn.readlines()

    def capitalise(self, word):
        char = word[0:1]
        return char.upper()

    def randomWord(self):
        word = None
        if self.wordlist is not None:
            word = random.choice(self.wordlist)
            word = word.strip()
        return word

    def genpw(self):
        pwlist = []
        twords = [self.randomWord() for i in range(4)]
        for word in twords:
            xw = self.capitalise(word)
            yw = word[1:]
            pwlist.append("".join([xw, yw]))
        pw = "".join(pwlist)
        phpw = self.phoneticAl2(pw)
        return (pw, phpw)

    def phoneticAl2(self, msg):
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

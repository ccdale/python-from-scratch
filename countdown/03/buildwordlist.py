"""Builds lists of words ordered alphabetically and sub-divided by length.

using the word list found at https://github.com/Tchanders/countdan/blob/master/brit-a-z.txt
of british spelling words of various lengths.

All words with apostrophes will be removed.

The list will be split into sub-lists by length of word.

The output will be all words of between 4-9 characters in length, sorted alphabetically.
"""

import sys


# build a dictionary of words sorted by length
def sortWordsByLength(lines, minl, maxl):
    try:
        # create empty dictionary
        words = {}
        # create a list of all numbers between the minimum length
        # and the maximum length.
        lengths = [x for x in range(minl, maxl + 1)]
        # create empty lists for each length in the dictionary
        for length in lengths:
            words[length] = []
        for line in lines:
            lln = len(line)
            if lln in lengths:
                words[lln].append(line)
        return words
    except Exception as e:
        msg = "Exception in sortWordsByLength:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


def readWordList(filename, minl=4, maxl=9):
    try:
        # read the whole file into a variable as a (long) string.
        # no need to worry about the different line endings for text files
        # between windows, macs and linux.  See https://stackoverflow.com/a/4601716
        # for the reasons.
        with open(filename, "rt") as ifn:
            wholefile = ifn.read()
        lines = [x for x in wholefile.split("\n")]
        words = sortWordsByLength(lines, minl, maxl)
        return words
    except Exception as e:
        msg = "Exception in readWordList:\n"
        msg += f"    input filename: {filename}\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


def toptail(words, cn):
    # using the number formatting rules
    # the ':,' at the end of the number in the format string
    # tells python to add a thousands seperator to the number
    # when printing - the thousands seperator will be a dot or
    # a comma, depending on your locale
    print(f"{len(words[cn]):,} {cn}-letter words")
    # print the first word in the list
    print(words[cn][0])
    # print the last word in the list
    print(words[cn][-1])


if __name__ == "__main__":
    try:
        words = readWordList(sys.argv[1])
        for i in range(4, 10):
            toptail(words, i)
    except Exception as e:
        msg = "Exception in main:\n"
        msg += f"    argv: {sys.argv}\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)

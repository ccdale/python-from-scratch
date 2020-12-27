"""Builds lists of words ordered alphabetically and sub-divided by length.

using the word list found at https://github.com/Tchanders/countdan/blob/master/brit-a-z.txt
of british spelling words of various lengths.

All words with apostrophes will be removed.

The list will be split into sub-lists by length of word.

The output will be all words of between 4-9 characters in length, sorted alphabetically.
"""

import sys


def readWordList(filename):
    try:
        # read the whole file into a variable as a (long) string.
        # no need to worry about the different line endings for text files
        # between windows, macs and linux.  See https://stackoverflow.com/a/4601716
        # for the reasons.
        with open(filename, "rt") as ifn:
            wholefile = ifn.read()
        lines = [x for x in wholefile.split("\n")]
        # because of the way split works we will have a final empty string
        # value in our list. using a negative value for the list slice here
        # means all but the last item. (not setting the starting value of the slice
        # means start at the beginning)
        lines = lines[:-1]
        return lines
    except Exception as e:
        msg = "Exception in readWordList:\n"
        msg += f"    input filename: {filename}\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


if __name__ == "__main__":
    try:
        lines = readWordList(sys.argv[1])
        print(f"{len(lines)}")
    except Exception as e:
        msg = "Exception in main:\n"
        msg += f"    argv: {sys.argv}\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)

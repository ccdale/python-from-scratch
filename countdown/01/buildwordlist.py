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
        lines = []
        # open the file with the context manager
        with open(filename, "r") as ifn:
            aline = ifn.readline()
            while aline:
                # remove the trailing newline char
                lines.append(aline.strip())
                # read in the next line and repeat
                aline = ifn.readline()
        # end of context manager, file will be closed automatically
        return lines
    except Exception as e:
        msg = "Exception in readWordList:\n"
        msg += f"    input filename: {filename}\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)
        raise


if __name__ == "__main__":
    try:
        # sys.argv holds the arguments to the program
        # [0] is the name of the program
        # >1 are the arguments (if any)
        # we could test it for length to ensure that there are the correct
        # number of arguments, but the exception handler will trigger if
        # there isn't a filename argument
        lines = readWordList(sys.argv[1])
        print(f"{len(lines)}")
    except Exception as e:
        msg = "Exception in main:\n"
        msg += f"    argv: {sys.argv}\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)

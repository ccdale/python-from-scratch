"""Builds lists of words ordered alphabetically and sub-divided by length.

using the word list found at https://github.com/Tchanders/countdan/blob/master/brit-a-z.txt
of british spelling words of various lengths.

All words with apostrophes will be removed.

The list will be split into sub-lists by length of word.

The output will be all words of between 4-9 characters in length, sorted alphabetically.
"""


# possible optimisation:
# adjust the word dictionary, sort by starting letter
def sortWordsByLetter(words):
    """Returns a dictionary of words sorted first by length then by starting letter.

    Output dictionary will be laid out like this:
    {
        9: {
            "a": [],
            "b": [],
            ...
            "z": [],
           },
        ...
        4: {
            "a": [],
            "b": [],
            ...
            "z": [],
           },
    }
    """
    try:
        # ord returns the ascii code for the supplied letter
        # chr converts an ascii code into a string of the representative letter
        # this list comprehension builds a list of single character strings a-z
        letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        # start with an empty output dictionary
        op = {}
        # do each length in turn
        for length in words:
            # setup the output dictionary, sub-dictionary
            op[length] = {}
            # assign each word in turn to it's correct place in the output dictionary
            for word in words[length]:
                # find the starting letter of the word
                startchr = word[0]
                # have we seen this starting letter before
                # if not, create a new, empty list under the op[length][startchr] keys
                if startchr not in op[length]:
                    op[length][startchr] = []
                # assign each word in turn to it's correct place in the output dictionary
                op[length][startchr].append(word)
        return op
    except Exception as e:
        msg = "Exception in sortWordsByLetter:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


# build a dictionary of words sorted by length
def sortWordsByLength(lines, minl, maxl):
    """Returns a dictionary of words sorted by length"""
    try:
        # create empty dictionary
        words = {}
        # iterate over each line (one word per line)
        # throw away words that are shorter than minl
        # throw away words that are longer than maxl
        for line in lines:
            lln = len(line)
            if lln >= minl and lln <= maxl:
                if lln not in words:
                    words[lln] = []
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
        minl = 4
        maxl = 9
        # note using hardcoded filename for wordlist now
        words = readWordList("brit-a-z.txt", minl, maxl)
        for i in range(minl, maxl + 1):
            toptail(words, i)
    except Exception as e:
        msg = "Exception in main:\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)

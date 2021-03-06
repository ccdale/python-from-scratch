"""Solves anagrams countdown style.
"""

import sys


# check to see if testw is an anagram of check
# check can be longer than testw
# if all the characters in testw appear in check
# then testw is an anagram of check (or contained in check)
def testWord(testw, check):
    try:
        ret = False
        # take a copy of the check argument and convert to a list of characters
        xchk = list(check)
        # set a character found counter
        cn = 0
        ccn = 0
        # loop through every character in testw
        # we don't need to convert the test string to a list to
        # iterate over it.
        for char in testw:
            ccn += 1
            # is that char in xchk (copy of check)
            if char in xchk:
                # yes it is, so remove it from xchk
                # .remove will only remove the first item it sees
                # so this is safe to use against a list that
                # contains duplicate items
                xchk.remove(char)
                # add one to the count of chars found
                cn += 1
            else:
                # no, therefore testw cannot be an anagram of check
                break
        # if the chars removed count is the same as the length
        # of the input word, testw, then testw must be an anagram
        # of check, or contained within check
        if cn == len(testw):
            # return a true value to say 'yes, it is an anagram'
            ret = True
        # return a false value to say 'nope, it aint an anagram'
        return ret
    except Exception as e:
        msg = "Exception in testWord:\n"
        msg += f"    check: {check}\n"
        msg += f"    testw: {testw}\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)


if __name__ == "__main__":
    # These imports are required only if we are testing this file
    # This shows that imports can be performed at any point in the program flow
    from buildwordlist import readWordList
    from buildwordlist import toptail

    try:
        words = readWordList(sys.argv[1])
        for i in range(4, 10):
            toptail(words, i)
        if testWord("aardvark", "aaadkrrv"):
            print("aardvark is an anagram of aaadkrrv")
        else:
            print("aardvark is NOT an anagram of aaadkrrv")
        if testWord("testtube", "aaadkrrvttbb"):
            print("testtube is an anagram of aaadkrrv")
        else:
            print("testtube is NOT an anagram of aaadkrrvttbb")
        if testWord("testtube", "tubeestb"):
            print("testtube is an anagram of tubeestb")
        else:
            print("testtube is NOT an anagram of tubeestb")
        if testWord("testtube", "tubeestbt"):
            print("testtube is an anagram of tubeestbt")
        else:
            print("testtube is NOT an anagram of tubeestbt")

    except Exception as e:
        msg = "Exception in main:\n"
        msg += f"    argv: {sys.argv}\n"
        msg += f"    {type(e).__name__} Exception:\n"
        msg += f"        {e}"
        print(msg)

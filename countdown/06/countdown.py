#!/usr/bin/env python3
"""Application to play the Coundown letters game."""

import sys

from buildwordlist import readWordList
from buildwordlist import sortWordsByLetter


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

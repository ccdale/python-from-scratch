#!/usr/bin/env python3
"""Code to generate passwords."""

# TODO
# use the password object to generate the password - DONE
# removing the need for the genpw function above
# add numbers and symbols to the password in random locations
# constrain the password to a set length

from passwordobject import Password


pobj = Password("wordlist.txt")

xpw, xphpw = pobj.genpw()

print(xpw)

print(xphpw)

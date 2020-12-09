#!/usr/bin/env python3
"""Code to generate passwords."""

from passwordobject import Password


def genpw(pwobj):
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
    twords = [pwobj.randomWord(wlist) for i in range(4)]
    for word in twords:
        xw = pwobj.capitalise(word)
        yw = word[1:]
        pwlist.append("".join([xw, yw]))
    pw = "".join(pwlist)
    print(pw)
    # print(phoneticAlphabet(pw))
    print(pwobj.phoneticAl2(pw))


if __name__ == "__main__":
    # TODO
    # use the password object to generate the password
    # removing the need for the genpw function above
    pw = Password()
    # print(dir(pw))
    genpw(pw)

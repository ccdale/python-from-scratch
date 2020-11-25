"""Dictionaries or associative arrays notes"""

# create an empty dictionary
xdict = {}

# create new keys in the dictionary and associate them with values
# keys are always strings
# values can be anything - strings, ints, floats, lists - even
# other dictionaries
xdict["string"] = "this is a string"
xdict["s2"] = 24
xdict["another"] = [1, 2, "three", 4]

# iterating over a dictionary returns the keys one by one
# the order cannot be guaranteed
# for key in xdict:
#      print(f"Key: {key} => Value: {xdict[key]}")


def phoneticAlphabet(msg):
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
    # lop = []
    # for letter in msg:
    #     xl = d.get(letter.upper(), letter)
    #     lop.append(xl)
    # op = " . ".join(lop)
    op = " . ".join(d.get(letter.upper(), letter) for letter in msg)
    return op


print(phoneticAlphabet("hello"))
print(phoneticAlphabet("hello eric 2345"))


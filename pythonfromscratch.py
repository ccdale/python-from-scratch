#!/usr/bin/env python3
"""This is the first file in the python from scratch module"""

# this is a comment
# and will be ignored by all apart from the (human) reader of this script
print("hello from python from scratch")

# loop to display all numbers from 0 to 10
for i in range(10):
    print(i)

# this is outside the loop
print("loop has now finished.")

# loop to display all even numbers
# remember that list indices and the range function start at zero
# the 3 parameters to range are (in order):
#    start
#    exclusive end
#    step
for i in range(0, 11, 2):
    print(i)

flag = True
noflag = False

flag = noflag

if flag is True:
    print("flag is true")
else:
    print("flag is not true (i.e. False)")


if flag:
    print("shorthand: flag is true")
else:
    print("shorthand: flag is not true (i.e. False)")


# lists
xlist = [1, 2, 3, 4, "52", 7]

cn = len(xlist)

print(f"list is {cn} items long")

print(xlist[3])

for i in xlist:
    print(i)

print("out of iteration loop")

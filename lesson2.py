xint = 12

zstr = "A string"


def printIt():
    print("IT")


def thirdFunc(arg1, arg2, flag=True):
    if flag:
        print(arg1)
        print(arg2)
    else:
        print("not printing the argument")


def timestwo(arg1, arg2):
    op = arg1 * arg2
    print("global variables")
    print(zstr)
    print(xint)
    print("local variables")
    print(op)
    return op


val = timestwo(12, 3)
val23 = timestwo(3, 22)
print("back to global vars again")
print("val is a var in global scope")
print(val)
print(val23)

print("divider -----------------")
print(xint)
# the line below will trigger a NameError Exception
# as the op variable name is not valid outside of hte timestwo function
# print(op)
print(zstr)
printIt()

print("Named arguments\n")
thirdFunc(22, "this is the contents of the positional argument 2")

thirdFunc(22, "anythin", flag=False)
thirdFunc(22, "nothing", flag=True)


print("switching things about")

thirdFunc("anythin", 22, flag=False)
thirdFunc("nothing", 22, flag=True)

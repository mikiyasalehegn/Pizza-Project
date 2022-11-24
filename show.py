from data import *


def show():
    for add in additionals:
        print(add, end="\n\t")
    add = int(input("\rHow many externals did you add? "))
    if 1 <= add <= 4:
        return add*2
    else:
        print("You inserted out of range")
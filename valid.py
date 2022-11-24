from data import *
from show import show


def valid():
    sz = input("Enter size")
    if sz in pizza:
        ap = show()  # ap represents the price due to additionals in show function
        city = input("do you live in Beer Sheva?, Y/N: )")
        if city == "Y".casefold():
            p1 = pizza[sz] + 20 + ap
            tot.append(p1)
        elif city == "N".casefold():
            p2 = pizza[sz] + 60 + ap
            tot.append(p2)

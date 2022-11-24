from data import *
from display import display
from valid import valid

f_sum = 0

if __name__ == '__main__':
    display()
    c = 1
    while True:
        age = int(input("Enter your age? "))
        if age < 18:
            break
        valid()
        con = input("do you want to continue ? y/n ")
        if con == "n":
            break
        c += 1

    for element in tot:
        f_sum += element
    print(f"You Bought {c} Pizzas, Total price is {f_sum}")



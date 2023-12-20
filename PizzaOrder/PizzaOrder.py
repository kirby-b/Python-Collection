import random
import math

class Pizzas: 

    def getValue():
        return random.randrange(10,20)
    def toString(order, pizzas):
        print("Listed below is your current pizza inventory: ")
        start = 0
        for x in range(int(pizzas)):
            for y in range(5):
                print(order[start + y])
            start += (y + 1)
            print("\n")
    
    order = []
    pizzas = input("How many holographic future pizzas would you like to order: ")
    while(True):
        if int(pizzas) < 1 or int(pizzas) > 10:
            pizzas = input("That is not a accepted number. Please in put a number between 1 and 10: ")
        elif pizzas.isnumeric() == False:
            pizzas = input("Please input a number, not a letter or symbol. Please in put a number between 1 and 10: ")
        else:
            break
    i = 0
    print("You will not be asked for the rest of the pizza information. This includes a name, code, and how many to order. The price will be automatically generated.")
    while (i <= int(pizzas) - 1):
        value = getValue()
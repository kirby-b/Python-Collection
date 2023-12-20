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
        order.append("Menu Price: $" + str(value))
        uniqueCode = input("Please input a three letter/number menu code for pizza number " + str(i + 1) + ": ")
        while(True):
            if len(uniqueCode) != 3:
                uniqueCode = input("Invalid code. Please input a 3 letter/number code: ")
            else:
                break
        print("You entered: " + str(uniqueCode))
        order.append("Menu Code: " + str(uniqueCode))
        name = input("Please input th pizza name: ")
        order.append("Menu Name: " + str(name))
        stock = input("Please input the amount of the " + str(name) + " pizza you want in the virtual storage freezer: ")
        while(True):
            if stock.isnumeric() == False: 
                stock = input("Please input a number, not symbols or letters: ")
            else:
                break
        order.append("Total Pizza Count: " + str(stock))
        total = int(stock) * int(value)
        order.append("Total Inventory Price: $ " + str(total))
        i += 1
    toString(order, pizzas) 
import random
import math

class Pizzas: 

    def main():
        order = []
        pizzas = input("How many holographic future pizzas would you like to order: ")#Gets the pizza creation amount
        while(True):# Validates the number
            if int(pizzas) < 1 or int(pizzas) > 10:
                pizzas = input("That is not a accepted number. Please in put a number between 1 and 10: ")
            elif pizzas.isnumeric() == False:
                pizzas = input("Please input a number, not a letter or symbol. Please in put a number between 1 and 10: ")
            else:
                break
        i = 0
        print("You will not be asked for the rest of the pizza information. This includes a name, code, and how many to order. The price will be automatically generated.")
        while (i <= int(pizzas) - 1):#Loops for number of pizzas and gets informataion of each pizza
            value = Pizzas.get_value()#Gets price
            order.append("Menu Price: $" + str(value)) #Appends price to order list
            unique_code = input("Please input a three letter/number menu code for pizza number " + str(i + 1) + ": ") #Gets unique code from user
            while(True): # Validates the code
                if len(unique_code) != 3:
                    unique_code = input("Invalid code. Please input a 3 letter/number code: ")
                else:
                    break
            print("You entered: " + str(unique_code)) 
            order.append("Menu Code: " + str(unique_code)) #Appends code to order list
            name = input("Please input the pizza name: ") #Gets pizza name
            order.append("Menu Name: " + str(name)) #Appends name to order list
            stock = input("Please input the amount of the " + str(name) + " pizza you want in the virtual storage freezer: ") #Gets amount of the type of pizza
            while(True): # Validates the number
                if stock.isnumeric() == False: 
                    stock = input("Please input a number, not symbols or letters: ")
                else:
                    break
            order.append("Total Pizza Count: " + str(stock)) #Appends stock to order list
            total = int(stock) * int(value) #Calculates the total price
            order.append("Total Inventory Price: $ " + str(total)) #Appends total price of each listing to order list
            i += 1
        Pizzas.to_string(order, pizzas) #Prints using the to_string function
    def get_value():
        return random.randrange(10,20)#Gets a random number for pizza price
        
    def to_string(order, pizzas):
        print("Listed below is your current pizza inventory: ")
        start = 0
        for x in range(int(pizzas)):#Prints out the contents of an array for the virtual pizza inventory
            for y in range(5):
                print(order[start + y])
            start += (y + 1)
            print("\n")

    if __name__ == "__main__":
        main()

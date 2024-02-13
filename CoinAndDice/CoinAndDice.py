import random

def main():
    print("Coin (two sides) or Dice (pick how many sides)")
    choice = str.lower(str.strip(input()))
    if choice == "dice":
        dice()
    #Rolls a die with the input number of sides, for the input number of dice
    if choice == "coin":
        coin_flip()
    #Flips a coin for the amount of times the user says to
    print ("Would you like to go again")
    YesNo = str.lower(str.strip(input()))
        
    while YesNo != "yes" and YesNo != "no":
        print("Error, try again")
        YesNo = str.lower(str.strip(input()))

    if YesNo == "no":
        print("Ok. Goodbye")

    if YesNo == "yes":
        print("Alright!")
        coin_n_dice()
    #Asking if the user want to go again

def dice():
    sides = str.strip(input("How many sides do you want each die to have:"))
    amount = str.strip(input("How many die would you like to roll:"))
    print("\n")
    for x in range(int(amount)):
        print(random.randrange(1,int(sides) + 1))
#Rolls a die with the input number of sides, for the input number of dice

def coin_flip():
    print("How many times would you like to flip")
    flips = str.strip(input())
    print("\n")
    for x in range(int(flips)):
        print(random.randrange(1,3))
#Flips a coin for the amount of times the user says to

if __name__ == "__main__":
    main()

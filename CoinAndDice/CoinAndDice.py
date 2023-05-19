import random

def coinNDice():
    print("Coin (two sides) or Dice (pick how many sides)")
    choice = str.lower(str.strip(input()))
    if choice == "dice":
        choice = str.strip(input("How many sides do you want each die to have:"))
        choice2 = str.strip(input("How many die would you like to roll:"))
        print("\n")
        for x in range(int(choice2)):
            print(random.randrange(1,int(choice) + 1))
    #Rolls a die with the input number of sides, for the input number of dice
    if choice == "coin":
        print("How many times would you like to flip")
        choice = str.strip(input())
        print("\n")
        for x in range(int(choice)):
            print(random.randrange(1,3))
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
        coinNDice()
    #Asking if the user want to go again
coinNDice()
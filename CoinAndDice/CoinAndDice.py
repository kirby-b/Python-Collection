import random

def coinNDice():
    print("Coin (two sides) or Dice (pick how many sides)")
    choice = str.lower(str.strip(input()))
    if choice == "dice":
        print("How many sides and how many dice do you want to roll")
        choice = str.strip(input("Sides:"))
        choice2 = str.strip(input("Dice:"))
        print("\n")
        for x in range(int(choice2)):
            print(random.randrange(1,int(choice) + 1))
    if choice == "coin":
        print("How many times would you like to flip")
        choice = str.strip(input())
        print("\n")
        for x in range(int(choice)):
            print(random.randrange(1,3))

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

coinNDice()
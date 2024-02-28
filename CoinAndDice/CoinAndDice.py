import random


def main():
    print("Welcome to the virtual dice roller and coin flipper. To stop this program hit control + C")
    while True:
        try:
            choice = str.lower(str.strip(input("""Do you want a Coin (two sides) or Dice (pick).
             Input Coin, Dice, C, or D:""")))
            while True:
                if validate(choice):
                    break
                else:
                    choice = str.lower(str.strip(input("""Invalid Input. Do you want a Coin (two sides) or Dice (pick).
                                                       Input Coin, Dice, C, or D:""")))
            
            if choice == "dice" or choice == "d":
                dice()
            # Rolls a die with the input number of sides, for the input number of dice
            if choice == "coin" or choice == "c":
                coin_flip()
            # Flips a coin for the amount of times the user says to
        except KeyboardInterrupt:
            print("Thank you for using the virtual dice roller and coin flipper.")
            break


def dice():
    sides = str.strip(input("How many sides do you want each die to have:"))
    amount = str.strip(input("How many die would you like to roll:"))
    print("-----")
    for x in range(int(amount)):
        print(random.randrange(1, int(sides) + 1))
# Rolls a die with the input number of sides, for the input number of dice


def coin_flip():
    print("How many times would you like to flip")
    flips = str.strip(input())
    print("-----")
    for x in range(int(flips)):
        print(random.randrange(1, 3))
# Flips a coin for the amount of times the user says to


def validate(ans):
    if ans not in ["c", "d", "coin", "dice"]:
        return False
    else:
        return True


if __name__ == "__main__":
    main()

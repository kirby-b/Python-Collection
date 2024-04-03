import random
from time import sleep

def main():
    earnings = 0
    cash = input('Welcome to the Lucky Programmer Slots. How many dollars would you like to put in (1 dollar per spin)')
    spins = int(cash)
    while True:
        try:
            while spins >= 0:
                if spins == 0:
                    cash = input("You are out of cash! \nPlease insert more money to continue!")
                    while not cash.isnumeric():
                        cash = input("Invalid input! Please try again:")
                    spins = int(cash)
                print("Spinning slots")
                earnings += winnings()
                print(f"Current Winnings: {earnings}")
                sleep(1)
                spins -= 1
        except KeyboardInterrupt:
            print("Thank you for playing. Come again and test your luck.")
            break


def winnings():
    win_or_no = random.randrange(0, 10000000000)
    if win_or_no == 77:
        print("Money Back")
        return 10
    elif win_or_no == 777:
        print("Small Prize")
        return 50
    elif win_or_no == 77777:
        print("Big Prize")
        return 200
    elif win_or_no == 7777777777:
        print("JackPot")
        return 10000
    else:
        print("No luck")
        return 0


if __name__ == "__main__":
    main()

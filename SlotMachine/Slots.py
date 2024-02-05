import random

class Slots:
    def main():
        jackpot = 0
        spins = 0
        cash = input('Welcome to the Lucky Programmer Slots. How many dollars would you like to put in (1 dollar per spin)')
        spins = int(cash)
        while(True):
            try:
                while(spins >= 0):
                    if(spins == 0):
                        cash = input("You are out of cash! \nPlease insert more money to continue!")
                        while cash.isnumeric() == False:
                            cash = input("Invalid input! Please try again:")
                        spins = int(cash)
                    print("Spinning slots")
                    Slots.winnings()    
                    spins -= 1
            except(KeyboardInterrupt):
                print("Thank you for playing. Come again and test your luck.")
                break

    def winnings():
        win_or_no = random.randrange(0,10000000000)
        if (win_or_no == 77):
            print("Money Back")
        elif (win_or_no == 777):
            print("Small Prize")
        elif (win_or_no == 77777):
            print("Big Prize")
        elif (win_or_no == 7777777777):
            print("JackPot")
        else:
            print("No luck")

if __name__ == "__main__":
    Slots.main()

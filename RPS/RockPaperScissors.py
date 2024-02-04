import random



def RockPaperScissorfunc():
    print("Rock")
    print("Paper")
    print("Scissors")
    print("Shoot")

    RPS = random.randrange(1,4)
    PlayerRPS = str.lower(str.strip(input()))
    while PlayerRPS != "rock" and PlayerRPS != "paper" and PlayerRPS != "scissors" and PlayerRPS != "gun":
        print("Error, try again")
        PlayerRPS = str.lower(str.strip(input()))

    if RPS == 1:
        print("Rock")
    if RPS == 2:
        print("Paper")
    if RPS == 3:
        print("Scissors")
    #Determines the computers choice

    if PlayerRPS == "rock" and RPS == 3 or PlayerRPS == "scissors" and RPS == 2 or PlayerRPS == "paper" and RPS == 1:
        print("You Win")
    elif PlayerRPS == "paper" and RPS == 3 or PlayerRPS == "rock" and RPS == 2 or PlayerRPS == "scissors" and RPS == 1:
        print("You Lose")
    elif PlayerRPS == "scissors" and RPS == 3 or PlayerRPS == "paper" and RPS == 2 or PlayerRPS == "rock" and RPS == 1:
        print("Tie")
    elif PlayerRPS == "gun":
        print("Cheater")
    #Determines output
    print ("Would you like to play again")
    YesNo = str.lower(str.strip(input()))

    while YesNo != "yes" and YesNo != "no":
        print("Error, try again")
        YesNo = str.lower(str.strip(input()))

    if YesNo == "no":
        print("GoodBye!")

    if YesNo == "yes":
        print("Alright!")
        RockPaperScissorfunc()

if __name__ == "__main__":
    RockPaperScissorfunc()

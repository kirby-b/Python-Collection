import random

def rock_paper_scissor_func():
    while(True):
        try:
            print("Rock \nPaper \nScissors \nShoot")
        
            RPS = random.randrange(1,4)
            player_RPS = lower(strip(input()))
            while player_RPS not in["rock","paper","scissors","gun"]:
                print("Error, try again")
                player_RPS = lower(strip(input()))
        
            if RPS == 1:
                print("Rock")
            if RPS == 2:
                print("Paper")
            if RPS == 3:
                print("Scissors")
            #Determines the computers choice
        
            if player_RPS == "rock" and RPS == 3 or player_RPS == "scissors" and RPS == 2 or player_RPS == "paper" and RPS == 1:
                print("You Win")
            elif player_RPS == "paper" and RPS == 3 or player_RPS == "rock" and RPS == 2 or player_RPS == "scissors" and RPS == 1:
                print("You Lose")
            elif player_RPS == "scissors" and RPS == 3 or player_RPS == "paper" and RPS == 2 or player_RPS == "rock" and RPS == 1:
                print("Tie")
            elif player_RPS == "gun":
                print("Cheater")
            #Determines who wins
        except(KeyboardInterrupt):
            print("Thank you for playing")
            break

if __name__ == "__main__":
    rock_paper_scissor_func()

import random
#Global Variables for scores
PLAYER_SCORE = 0
COMPUTER_SCORE = 0
TIMES_CHEATED = 0
TIES = 0

def rock_paper_scissor_func():
    while(True):
        try:
            print("Rock \nPaper \nScissors \nShoot")
        
            RPS = random.randrange(1,4)
            player_RPS = lower(strip(input()))
            while player_RPS not in["rock","paper","scissors","gun"]:
                print("Error, try again")
                player_RPS = lower(strip(input()))
            #Validates input
        
            if RPS == 1:
                print("Rock")
            if RPS == 2:
                print("Paper")
            if RPS == 3:
                print("Scissors")
            #Determines the computers choice
        
            if player_RPS == "rock" and RPS == 3 or player_RPS == "scissors" and RPS == 2 or player_RPS == "paper" and RPS == 1:
                print("You Win")
                keep_score("p")
            elif player_RPS == "paper" and RPS == 3 or player_RPS == "rock" and RPS == 2 or player_RPS == "scissors" and RPS == 1:
                print("You Lose")
                keep_score("c")
            elif player_RPS == "scissors" and RPS == 3 or player_RPS == "paper" and RPS == 2 or player_RPS == "rock" and RPS == 1:
                print("Tie")
                keep_score("t")
            elif player_RPS == "gun":
                print("Cheater")
                keep_score("cheat")
            #Determines who wins and calls the function to update the score
        except(KeyboardInterrupt):
            print("Thank you for playing. Here are the final scores:")
            keep_score("thisstringdoesntmatter")
            break
        #If the user uses a keyboard interupt, it will end the program with this catch
def keep_score(winner):
    if winner == "p":
        PLAYER_SCORE += 1
    elif winner == "c":
        COMPUTER_SCORE += 1
    elif winner == "t":
        TIES += 1
    elif winner == "cheat":
        PLAYER_SCORE += 1
        TIMES_CHEATED += 1
    else:
        pass
    #Calculates the new scores
    
    print(f"Player Wins:{PLAYER_SCORE}\nComputer Wins:{COMPUTER_SCORE}\nTimes you tied:{TIES}\nTimes you cheated:{TIMES_CHEATED}")
    #Prints current scores

if __name__ == "__main__":
    rock_paper_scissor_func()

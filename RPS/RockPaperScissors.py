import random
#Global Variables for scores
player_score = 0
computer_score = 0
times_cheated = 0
ties = 0

def rock_paper_scissor_func():
    while(True):
        try:
            print("Rock \nPaper \nScissors \nShoot")
        
            RPS = random.randrange(1,4)
            player_RPS = str.lower(str.strip(input()))
            while player_RPS not in["rock","paper","scissors","gun"]:
                print("Error, try again")
                player_RPS = str.lower(str.strip(input()))
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
    global times_cheated
    global player_score 
    global computer_score
    global ties 
    if winner == "p":
        player_score += 1
    elif winner == "c": 
        computer_score += 1
    elif winner == "t":
        ties += 1
    elif winner == "cheat":
        player_score += 1
        times_cheated += 1
    else:
        pass
    #Calculates the new scores
    
    print(f"Player Wins:{player_score}\nComputer Wins:{computer_score}\nTimes you tied:{ties}\nTimes you cheated:{times_cheated}")
    #Prints current scores

if __name__ == "__main__":
    rock_paper_scissor_func()

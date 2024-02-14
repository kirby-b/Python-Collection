import random

NUM_DIGITS = 3
MAX_GUESS = 10
#Global Variables for scores
loses = 0
player_score = 0

def main():
    print("Welcome to my deduction game. To stop this program hit control + C")
    print("I am thinking of a %s-digit number. Try to guess what it is." % (NUM_DIGITS))
    print("The clues I give are...")
    print("When I say:    That means:")
    print(" NOPE        None of the digits are correct.")
    print(" Cold        One digit is correct but in the wrong position.")
    print(" Warm        One digit is correct and in the right position.")
    #Tells the user what the clues mean
    while True:
        try:
            secret_num = get_secret_num()
            print("I have generated a number. You have %s guesses to get it." % (MAX_GUESS))
        
            guesses_taken = 1
            while guesses_taken <= MAX_GUESS:
                guess = ""
                while len(guess) != NUM_DIGITS or not is_only_digits(guess):
                    print("Guess #%s: " % (guesses_taken))
                    guess = input()
        
                print(get_clues(guess, secret_num))
                guesses_taken += 1
        
                if guess == secret_num:
                    print("You guessed it. Good Job!")
                    keep_score("w")
                    break
                if guesses_taken > MAX_GUESS:
                    print("You ran out of guesses. The answer was %s." % (secret_num))
                    keep_score("l")
            #Checks to see if the user guessed the number and if they have run out of guesses
        except(KeyboardInterrupt):
            print("Thank you for playing. Here is your final score:")
            keep_score("lolthisstringispointless")
            break
        
def get_secret_num():
    # Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess, secret_num):
    # Returns a string with the clues to the user.
    if guess == secret_num:
        return "You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Warm")
        elif guess[i] in secret_num:
            clues.append("Cold")
    if len(clues) == 0:
        return "Nope"

    clues.sort()
    return " ".join(clues)

def is_only_digits(num):
    # Checks to make sure the user only input digits. Returns true if they did, otherwise it is false.
    if num == "":
        return False

    for i in num:
        if i not in "0 1 2 3 4 5 6 7 8 9".split():
            return False

    return True
def keep_score(winner):
    global loses
    global player_score
    if winner == "w":
        player_score += 1
    elif winner == "l":
        loses += 1
    else:
        pass
    #Calculates the new scores
    
    print(f"Games Won:{player_score}\nGames Lost:{loses}")
    #Prints current scores

if __name__ == "__main__":
    main()

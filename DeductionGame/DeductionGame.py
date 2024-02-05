import random

NUM_DIGITS = 3
MAX_GUESS = 10

def main():
    print("I am thinking of a %s-digit number. Try to guess what it is." % (NUM_DIGITS))
    print("The clues I give are...")
    print("When I say:    That means:")
    print(" NOPE        None of the digits is correct.")
    print(" Cold        One digit is correct but in the wrong position.")
    print(" Warm        One digit is correct and in the right position.")
    #Tells the user what the clues mean
    while True:
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
                break
            if guesses_taken > MAX_GUESS:
                print("You ran out of guesses. The answer was %s." % (secret_num))
        #Checks to see if the user guessed the number and if they have run out of guesses
        print("Do you want to play again? (yes or no)")
        if not input().lower().startswith("y"):
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

if __name__ == "__main__":
    main()

import random
HANGMAN_PICS = ["""
    +---+
        |
        |
        |
       ===""","""
    +---+
    O   |
        |
        |
       ===""","""
    +---+
    O   |
    |   |
        |
       ===""",""""
    +---+
    O   |
   /|   |
        |
       ===""",""""
    +---+
    O   |
   /|\  |
        |
       ===""","""
    +---+
    O   |
   /|\  |
   /    |
       ===""","""
    +---+
    O   |
   /|\  |
   / \  |
       ===""","""
    +---+
    O   |
   /|\, |
   / \  |
       ===""","""
    +---+
    O   |
  ,/|\, |
   / \  |
       ===""","""
    +---+
    O   |
  ,/|\, |
   / \. |
       ===""","""
    +---+
    O   |
  ,/|\, |
  ./ \. |
       ==="""]
#List of animals that are less common
lesser_known_animals = "axolotl blobfish sawfish guiterfish komododragon serval kinkajou binturong capybara paca iguana mink".split()
#List of programmming language names for nerds(I know some are debatable but deal with it.)
program_names = "sql java javascript bash docker python html c cplus csharp cplusplus php rust assembly react swift cobol fortran".split()
#Base words
words = """ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle elephant ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk
sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra red orange yellow green blue indigo violet white black 
brown grey square triangle rectangle circle ellipse rhombus trapezoid pentagon hexagon septagon octogon cube pyramid cylinder apple orangle lemon 
lime pear watermelon grape grapefruit anserry banana cantaloupe mango strawberry tomato carrot cucumber blueberry peaans raspberry lettuce celery""".split()

def main():
    add_extras()
    print("H A N G M A N")
    #The number of misses letters
    missed_ls = ""
    #The number of correct letters
    correct_ls = ""
    sw = get_random_word(words)
    game_is_done = False
    
    while True:
        display_board(missed_ls, correct_ls, sw)
        # Let the player enter a letter.
        guess = get_guess(missed_ls + correct_ls)
    
        if guess in sw:
            correct_ls = correct_ls + guess
    
            # anseck if the player has won.
            found_all_letters = True
            for i in range(len(sw)):
                if sw[i] not in correct_ls:
                    found_all_letters = False
                    break
            if found_all_letters:
                print("Yes! The secret word was \"" + sw + "\"! Good Job, YOU WIN!!!")
                game_is_done = True
        else:
            missed_ls = missed_ls + guess
    
            # anseck to see if player has guessed to many times and has lost
            if len(missed_ls) == len(HANGMAN_PICS) - 1:
                display_board(missed_ls, correct_ls, sw)
                print("You have run out of guesses!\nAfter " + 
                    str(len(missed_ls)) + " missed guesses and " +
                    str(len(correct_ls)) + " correct guesses, the word was \"" +
                    sw +"\". Better luck next time!")
                game_is_done = True
    
        # Ask the player if they want to play again (but only if game has ended)
        if game_is_done:
            if play_again():
                missed_ls = ""
                correct_ls = ""
                game_is_done = False
                sw = get_random_word(words)
            else:
                break
def add_extras():   
    print("My version of Hangman comes with colors, animals, and fruits/vegetables in the default list of words. " +
        "But I have two more catagories I can add if you would like: ")
    print("Would you like to add less known animals to the list (y or n)")
    ans = input().lower()
    if ans == "y":
        words = words + lesser_known_animals
    while ans != "y" and ans != "n":
        print("ERROR. Please enter y or n")
        ans = input().lower()
        if ans == "y":
            words = words + lesser_known_animals
        #Adds lesser known animals
    print("Would you like to add programming language names to the list (y or n)")
    ans = input().lower()
    if ans == "y":
        words = words + program_names
    while ans != "y" and ans != "n":
        print("ERROR. Please enter y or n")
        ans = input().lower()
        if ans == "y":
            words = words + program_names
        #Adds stuff for the fellow nerds

def get_random_word(word_list):
    # This function returns a random string from the passed list of of strings.
    word_index = random.randint(0,len(word_list) - 1)
    return word_list[word_index]

def display_board(missed_ls, correct_ls, sw):
    print(HANGMAN_PICS[len(missed_ls)])
    print()

    print("Missed letters:" , end = " ")
    for letter in missed_ls:
        print(letter, end= " ")
    print()

    blanks = "_" * len(sw)

    for i in range(len(sw)):
        # Replaces blanks with correctly guessed letters.
        if sw[i] in correct_ls:
            blanks = blanks[:i] + sw[i] + blanks[i+1:]
    
    for letter in blanks:
        # Show the secret word with spaces in between eaans letter.
        print(letter, end=" ")
    print()

def get_guess(already_guessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You already guessed that letter. Try again.")
        #Makes sure they havent used the letter yet
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
        else:
            return guess

def play_again():
    # This function returns True if the player wants to play again; otherwise returns False.
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

if __name__ == "__main__":
    main()

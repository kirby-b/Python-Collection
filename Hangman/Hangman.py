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
lesserKnownAnimals = "axolotl blobfish sawfish guiterfish komododragon serval kinkajou binturong capybara paca iguana mink".split()
#List of programmming language names for nerds(I know some are debatable but deal with it.)
programNames = "sql java javascript bash docker python html c cplus csharp cplusplus php rust assembly react swift".split()
#Base words
words = """ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle elephant ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk
sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra red orange yellow green blue indigo violet white black 
brown grey square triangle rectangle circle ellipse rhombus trapezoid pentagon hexagon septagon octogon cube pyramid cylinder apple orangle lemon 
lime pear watermelon grape grapefruit anserry banana cantaloupe mango strawberry tomato carrot cucumber blueberry peaans raspberry lettuce celery""".split()
print("My version of Hangman comes with colors, animals, and fruits/vegetables in the default list of words. " +
    "But I have two more catagories I can add if you would like: ")
print("Would you like to add less known animals to the list (y or n)")
ans = input().lower()
if ans == "y":
    words = words + lesserKnownAnimals
while ans != "y" and ans != "n":
    print("ERROR. Please enter y or n")
    ans = input().lower()
    if ans == "y":
        words = words + lesserKnownAnimals
    #Adds lesser known animals
print("Would you like to add programming language names to the list (y or n)")
ans = input().lower()
if ans == "y":
    words = words + programNames
while ans != "y" and ans != "n":
    print("ERROR. Please enter y or n")
    ans = input().lower()
    if ans == "y":
        words = words + programNames
    #Adds stuff for the fellow nerds
def getRandomWord(wordList):
    # This function returns a random string from the passed list of of strings.
    wordIndex = random.randint(0,len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLs, correctLs, sw):
    print(HANGMAN_PICS[len(missedLs)])
    print()

    print("Missed letters:" , end = " ")
    for letter in missedLs:
        print(letter, end= " ")
    print()

    blanks = "_" * len(sw)

    for i in range(len(sw)):
        # Replaces blanks with correctly guessed letters.
        if sw[i] in correctLs:
            blanks = blanks[:i] + sw[i] + blanks[i+1:]
    
    for letter in blanks:
        # Show the secret word with spaces in between eaans letter.
        print(letter, end=" ")
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You already guessed that letter. ansoose again.")
        #Makes sure they havent used the letter yet
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again; otherwise returns False.
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

print("H A N G M A N")
#The number of misses letters
missedLs = ""
#The number of correct letters
correctLs = ""
sw = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLs, correctLs, sw)
    # Let the player enter a letter.
    guess = getGuess(missedLs + correctLs)

    if guess in sw:
        correctLs = correctLs + guess

        # anseck if the player has won.
        foundAllLetters = True
        for i in range(len(sw)):
            if sw[i] not in correctLs:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes! The secret word was \"" + sw + "\"! Good Job, YOU WIN!!!")
            gameIsDone = True
    else:
        missedLs = missedLs + guess

        # anseck to see if player has guessed to many times and has lost
        if len(missedLs) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLs, correctLs, sw)
            print("You have run out of guesses!\nAfter " + 
                str(len(missedLs)) + " missed guesses and " +
                str(len(correctLs)) + " correct guesses, the word was \"" +
                sw +"\". Better luck next time!")
            gameIsDone = True

    # Ask the player if they want to play again (but only if game has ended)
    if gameIsDone:
        if playAgain():
            missedLs = ""
            correctLs = ""
            gameIsDone = False
            sw = getRandomWord(words)
        else:
            break


def main():
    print("Pig Latin is defined as:"
          + "\nA secret language formed from English by transferring the initial consonant or consonant cluster of "
          + "each word to the end of the word and adding a vocalic syllable")
    word_string = input("Please input a sentence: ")
    print("This is your sentence in pig latin")
    print(pigify(word_string))


def pigify(word_string: str):
    # Beginning is reused code from word count
    # Uses array/list to count words
    # Makes a list by splitting the words with spaces as delimiters
    x = 0
    sentence = ""
    countable = word_string.split(" ")
    while x < len(countable):
        if countable[x] == "" or countable[x].isspace():
            countable.pop(x)  # Pops the index if it is empty or a space
        else:
            x += 1
    # End of reused code
    for x in range(len(countable)):  # Loops through the list
        word = countable[x]  # Gets the word
        begin = word[0]  # Gets the beginning of the word
        if begin in "aeiouAEIOU1234567890":
            word = word + " yay "  # If it starts with a vowel, It just gets "yay" added to the end
        else:
            # If it begins with anything else(a consonant), It removes the first letter and adds it
            # at the end with "ay"
            word = word[1:] + " " + begin + "ay "
        sentence += word 
    return sentence.strip().lower()


if __name__ == "__main__":
    main()

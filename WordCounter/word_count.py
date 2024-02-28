def main():
    word_string = input("Please input a sentence:")
    word_count(word_string)


def word_count(word_string: str):
    # Uses array/list to count words
    # Makes a list by splitting the words with spaces as delimiters
    y = 0
    x = 0
    countable = word_string.split(" ")
    while x < len(countable):
        if countable[x] == "" or countable[x].isspace():
            countable.pop(x)  # Pops the index if it is empty or a space
        else:
            x += 1

    print("This sentence contains " + str(len(countable)) + " words")


if __name__ == "__main__":
    main()

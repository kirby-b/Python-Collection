def main():
    word_string = input("Please input a sentence:")
    word_count(word_string)


def word_count(word_string: str):
    # Counts the spaces and assumes no foul play
    word_string.strip(" ")
    total_words = word_string.count(" ") + 1
    # Assumes there is one space per word except the last
    print(str(total_words))


if __name__ == "__main__":
    main()

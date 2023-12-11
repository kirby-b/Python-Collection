def main(): 
    word_string = input("Please input a sentence:")
    word_count(word_string)

def word_count(word_string: str):
    #Uses array/list to count words
    #Makes a list by splitting the words with spaces as delimiters
    word_string.strip(" ")
    countable = word_string.split(" ")
    for x in range(len(countable)- 1):
        if countable[x] == "" or countable[x].isspace():
            countable.pop(x)
    print(str(len(countable)))

main()
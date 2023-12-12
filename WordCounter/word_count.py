def main(): 
    word_string = input("Please input a sentence:")
    word_count(word_string)

def word_count(word_string: str):
    #Uses array/list to count words
    #Makes a list by splitting the words with spaces as delimiters
    y = 0
    x = 0
    word_string.strip(" ")
    countable = word_string.split(" ")
    while x < len(countable):
        if countable[x] == "" or countable[x].isspace():
            countable.pop(x)
        else:
            print(countable[x])
            x +=1
    print(str(len(countable)))
main()
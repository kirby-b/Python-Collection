def main(): 
    word_string = input("Please input a sentence:")
    word_count(word_string)

def word_count(word_string: str):
    #Counts the spaces and assumes no foul play
    word_string.strip(" ")
    total_words = word_string.count(" ") + 1
    print(str(total_words))

main()
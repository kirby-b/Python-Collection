import random

def high_or_low_func():
    print("HIGHER or LOWER:")
    rando = random.randrange(1,11)
    print ("The number is: "+rando)
    #Generates a random number and prints it. 
    print("Will the next number be Higher or Lower.")
    h_or_l = str.lower(str.strip(input()))
    #Holds the users answer
    while h_or_l != "higher" and h_or_l != "lower" and h_or_l != "h" and h_or_l != "l":
        print("Error, try again. Please input higher or lower.")
        h_or_l = str.lower(str.strip(input()))
    #Asks if the user thinks the next number with be Higher or Lower
    new_rando = random.randrange(1,11)
    ans = ""
    if rando > new_rando:
        print(new_rando)
        print("Lower")
        ans = "lower"
    if rando < new_rando:
        print(new_rando)
        print("Higher")
        ans = "higher"     
    #Determines if the new number is Higher or Lower and tells the user
    if ans == h_or_l:
      print ("Correct")
    else :
        print ("Wrong, sorry")
    print ("Would you like to play again")
    yes_no = str.lower(str.strip(input()))
    #Tells user if they were right or now
    while yes_no != "yes" and yes_no != "no":
        print("Error, try again")
        yes_no = str.lower(str.strip(input()))

    if yes_no == "no":
        print("Goodbye!")

    if yes_no == "yes":
        print("Alright!")
        high_or_low_func()
    #Figure out if the user wants to play again

if __name__ == "__main__":
    high_or_low_func()

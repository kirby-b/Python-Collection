import random

def highORlowfunc():
    print("HIGHER or LOWER:")
    rando = random.randrange(1,11)
    print ("The number is: "+rando)
    #Generates a random number and prints it. 
    print("Will the next number be Higher or Lower.")
    HorL = str.lower(str.strip(input()))
    #Holds the users answer
    while HorL != "higher" and HorL != "lower" and HorL != "h" and HorL != "l":
        print("Error, try again. Please input higher or lower.")
        HorL = str.lower(str.strip(input()))
    #Asks if the user thinks the next number with be Higher or Lower
    newrando = random.randrange(1,11)
    ans = ""
    if rando > newrando:
        print(newrando)
        print("Lower")
        ans = "lower"
    if rando < newrando:
        print(newrando)
        print("Higher")
        ans = "higher"     
    #Determines if the new number is Higher or Lower and tells the user
    if ans == HorL:
      print ("Correct")
    else :
        print ("Wrong, sorry")
    print ("Would you like to play again")
    YesNo = str.lower(str.strip(input()))
    #Tells user if they were right or now
    while YesNo != "yes" and YesNo != "no":
        print("Error, try again")
        YesNo = str.lower(str.strip(input()))

    if YesNo == "no":
        print("Goodbye!")

    if YesNo == "yes":
        print("Alright!")
        highORlowfunc()
    #Figure out if the user wants to play again

highORlowfunc()
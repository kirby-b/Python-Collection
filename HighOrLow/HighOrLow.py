import random

def highORlowfunc():
    next = 0
    print("HIGHER or LOWER:")
    rando = random.randrange(1,11)
    print (rando)
    print("Will the next number be Higher or Lower.")
    HorL = str.lower(str.strip(input()))
    while HorL != "higher" and HorL != "lower" and HorL != "h" and HorL != "l":
        print("Error, try again. Please input higher or lower.")
        HorL = str.lower(str.strip(input()))

    newrando = random.randrange(1,11)
    ans = ""
    if rando > newrando:
        print(newrando)
        print("Lower")
        ans = "lower"
        next = 1
    if rando < newrando:
        print(newrando)
        print("Higher")
        ans = "higher"
        next = 1     

    if ans == HorL:
      print ("Correct")
    else :
        print ("Wrong, sorry")
    print ("Would you like to play again")
    YesNo = str.lower(str.strip(input()))

    while YesNo != "yes" and YesNo != "no":
        print("Error, try again")
        YesNo = str.lower(str.strip(input()))

    if YesNo == "no":
        print("Goodbye!")

    if YesNo == "yes":
        print("Alright!")
        highORlowfunc()


highORlowfunc()
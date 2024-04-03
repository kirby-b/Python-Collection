import random

def high_or_low_func():
    print("Welcome to higher or lower. To stop the program please please control + C.")
    while True:
        try:
            print("HIGHER or LOWER:")
            rando = random.randrange(1, 11)
            print("The number is: " + str(rando))
            # Generates a random number and prints it.
            print("Will the next number be Higher or Lower.")
            h_or_l = str.lower(str.strip(input()))
            # Holds the users answer
            while h_or_l not in ["higher", "lower"]:
                print("Error, try again. Please input higher or lower.")
                h_or_l = str.lower(str.strip(input()))
            # Asks if the user thinks the next number with be Higher or Lower
            new_rando = random.randrange(1, 11)
            ans = ""
            if rando > new_rando:
                print(new_rando)
                print("Lower")
                ans = "lower"
            if rando < new_rando:
                print(new_rando)
                print("Higher")
                ans = "higher"
                # Determines if the new number is Higher or Lower and tells the user
            if ans == h_or_l:
                print("Correct")
            else:
                print("Wrong, sorry")
            # Tells user if they were right or not
        except KeyboardInterrupt:
            print("Thank you for playing")
            break

if __name__ == "__main__":
    high_or_low_func()

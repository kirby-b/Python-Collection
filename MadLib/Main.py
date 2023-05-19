from MadLibs import MadLibs
print("""Welcome to my MadLib program. Would you like to play:
    A simple MadLib
    or
    A Crazy MadLib
    (please type simple, crazy, c, or s)""")
ans = str.lower(str.strip(input()))
#Gets the mode answer from the user
while ans != "simple" and ans != "s" and ans != "crazy" and ans != "c":
        print("Error, try again")
        ans = str.lower(str.strip(input()))
    #Checks if input is valid

if ans == "simple" or ans == "s":
    MadLibs.SimpleMadLibModeFunc()
if ans == "crazy" or ans == "c":
    MadLibs.CrazyMadLibModeFunc()
#Prints the Madlib based on type from a function in the MadLib class
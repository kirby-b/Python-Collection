from MadLibs import MadLibs
print("""Welcome to my MadLib program. Would you like to play:
    A simple MadLib
    or
    A Crazy MadLib
    (please type simple, crazy, c, or s)""")
ans = str.lower(str.strip(input()))
while ans != "simple" and ans != "s" and ans != "crazy" and ans != "c":
        print("Error, try again")
        ans = str.lower(str.strip(input()))

if ans == "simple" or ans == "s":
    MadLibs.SimpleMadLibModeFunc()
if ans == "crazy" or ans == "c":
    MadLibs.CrazyMadLibModeFunc()
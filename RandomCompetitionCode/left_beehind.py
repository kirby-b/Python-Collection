import sys

output = ""
never = False
cases = 0
while True:
    if cases == 15:
        break
    try:
        pots = input("")
        pots = pots.strip()
        sweet, sour = pots.split(" ")
        if int(sweet) == 0 or int(sour) == 0 or int(sweet) <= 1000 or int(sour) <= 1000 or int(sweet) >= 0 or int(
                sour) >= 0:
            break
        if not sweet.isnumeric() or not sour.isnumeric():
            sys.exit(0)
    except ValueError:
        sys.exit(0)
    if int(sweet) + int(sour) == 13:
        output = "Never speak again." + "\n"
        never = True
    elif int(sweet) < int(sour) and never is False:
        output += "Left beehind." + "\n"
    elif int(sweet) > int(sour) and never is False:
        output += "To the convention." + "\n"
    elif int(sweet) == int(sour) and never is False:
        output += "Undecided." + "\n"

print(output)
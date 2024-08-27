import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    *    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  *      │",
        "│         │",
        "│      *  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  *      │",
        "│    *    │",
        "│      *  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  *   *  │",
        "│         │",
        "│  *   *  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  *   *  │",
        "│    *    │",
        "│  *   *  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  *   *  │",
        "│  *   *  │",
        "│  *   *  │",
        "└─────────┘")
}   # Dice art

dice = []
total = 0
num_of_dice = input("How many dice do you want?: ")
# Gets the number of dice
while True:
    if not num_of_dice.isnumeric():
        num_of_dice = input("Invalid Input, please input an a whole number(1 2 3 4 5...)\n How many dice do you want?: ")
    else:
        break

for die in range(int(num_of_dice)):
    dice.append(random.randint(1, 6))

# PRINT VERTICALLY
for die in range(int(num_of_dice)):
    for line in dice_art.get(dice[die]):
        print(line)

# PRINT HORIZONTALLY
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"Total from dice: {total}")

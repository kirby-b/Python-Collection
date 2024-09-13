binary_num = ""
while True:
    try:
        number = input("Please input a whole number (EX:2000): ")
        val = int(str(number))
        break
    except ValueError:
        print("\nThat's not an whole number, try again.\n")
while int(number) > 0:
    binary_num += str(int(number) % 2)
    number = int(number) / 2

print(binary_num[::-1])
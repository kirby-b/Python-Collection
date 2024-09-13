binary_num = ""
while True:
    try:
        # Gets whole number
        number = input("Please input a whole number (EX:2000): ")
        val = int(str(number))
        break
    except ValueError:
        print("\nThat's not an whole number, try again.\n")
while int(number) > 0:
    binary_num += str(int(number) % 2)
    number = int(number) / 2
# The while loop outputs a str of 0s and 1s from the remainder of current num after modulus.
# The output itself will be the reverse of the binary for the input int. 
# Because of this I output it "backwards" that way it is correct
print(binary_num[::-1])
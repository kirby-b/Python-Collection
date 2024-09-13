binary_num = ""
number = input("Please input a number (EX:2000): ")

while int(number) > 0:
    binary_num += str(int(number) % 2)
    number = int(number) / 2

print(binary_num[::-1])
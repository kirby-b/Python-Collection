def main():
    fizz1 = FizzBuzz(3)
    fizz2 = FizzBuzz(5)
    fizz3 = FizzBuzz(10)
    fizz4 = FizzBuzz(20)
    print("\nInput Number 3:")
    fizz1.fizz_buzz()
    print("\nInput Number 5:")
    fizz2.fizz_buzz()
    print("\nInput Number 10:")
    fizz3.fizz_buzz()
    print("\nInput Number 20:")
    fizz4.fizz_buzz()


class FizzBuzz:
    def __init__(self, number):
        self.number = number

    def fizz_buzz(self):
        n = self.number
        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:  # If it is divisible by 5 and 3 it prints FizzBuzz
                print("FizzBuzz", end=" ")
            elif i % 3 != 0 and i % 5 != 0:  # If it is divisible by none it prints the number
                print(str(i), end=" ")
            elif i % 3 == 0:  # If it is divisible by 3 it prints Fizz
                print("Fizz", end=" ")
            elif i % 5 == 0:  # If it is divisible by 5 it prints Buzz
                print("Buzz", end=" ")
            # Prints a phrase based on the current number being tested


if __name__ == "__main__":
    main()

class FizzBuzz:
    def fizzBuzz(n: int):
        for i in range(1, n+1):
            if i%5 == 0 and i%3 == 0:
                print("FizzBuzz", end=" ")
            elif i%3 != 0 and i%5 != 0:
                print(str(i), end=" ")
            elif i%3 == 0:
                print("Fizz", end=" ")
            elif i%5 == 0:
                print("Buzz", end=" ")
        
    print("\nInput Number 3:")
    fizzBuzz(3)
    print("\nInput Number 5:")
    fizzBuzz(5)
    print("\nInput Number 10:")
    fizzBuzz(10)
    print("\nInput Number 20:")
    fizzBuzz(20)
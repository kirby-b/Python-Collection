class FizzBuzz:
    def fizzBuzz(n: int):
        for i in range(1, n+1):
            if i%5 == 0 and i%3 == 0: #If it is divisible by 5 and 3 it prints FizzBuzz
                print("FizzBuzz", end=" ")
            elif i%3 != 0 and i%5 != 0: #If it is divisible by none it prints the number
                print(str(i), end=" ")
            elif i%3 == 0: #If it is divisible by 3 it prints Fizz
                print("Fizz", end=" ")
            elif i%5 == 0: #If it is divisible by 5 it prints Buzz
                print("Buzz", end=" ")
            #Prints a phrase based on the current number being tested
        
    print("\nInput Number 3:")
    fizzBuzz(3)
    print("\nInput Number 5:")
    fizzBuzz(5)
    print("\nInput Number 10:")
    fizzBuzz(10)
    print("\nInput Number 20:")
    fizzBuzz(20)

#There is also a holiday version on my gists
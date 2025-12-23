# Number guessing game
import random
secret_number = random.randint(1, 100)
print("Guess the number between 1 and 100!")
while True:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Higher!")
    elif guess > secret_number:
        print("Lower!")
    else:
        print("Congratulations! You guessed the right number:", secret_number)
        break


#list iteration
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print("Number:", num, "Square:", num ** 2)

# fizz buzz
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
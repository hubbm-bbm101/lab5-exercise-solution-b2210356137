import random
number = random.randint(0,100)
def guessing_function():
    guess = int(input("Guess the number:"))
    if guess == number:
        print("Your guess is true!")
    elif guess < number:
        print("Increase your number")
        guessing_function()
    else: 
        print("Decrease your number")
        guessing_function()
guessing_function()
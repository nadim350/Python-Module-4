import random
number_to_guess = random.randint(1, 10)

while True:
    try:

        guess = int(input("Guess the number between 1 and 10: "))

        if guess < number_to_guess:
            print("Too low.")
        elif guess > number_to_guess:
            print("Too high.")
        else:
            print("Correct! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid integer.")

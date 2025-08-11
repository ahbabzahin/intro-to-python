import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = []
    

    print("Guess a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        attempts.append(guess)
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {len(attempts)} attempts.")
            print("Your guesses were:", attempts)
            break

number_guessing_game()

import random

def play_round():
    options = ["rock", "paper", "scissors"]
    user = input("Enter Rock, Paper, or Scissors: ").strip().lower()
    if user not in options:
        print("Invalid choice! Try again.")
        return None
    computer = random.choice(options)
    print(f"Computer chose: {computer}")
    if user == computer:
        return "It's a Tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

def game():
    print("Welcome to Rock Paper Scissors!")
    while True:
        result = play_round()
        if result:
            print(result)
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

game()


import random

def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def get_user_choice():
    choice = input("Enter your choice (snake/water/gun): ").lower()
    while choice not in ['snake', 'water', 'gun']:
        print("Invalid input! Please choose from snake, water, or gun.")
        choice = input("Enter your choice again: ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
def play_game():
    print("Welcome to Snake 🐍, Water 💧, Gun 🔫 Game!")
    user = get_user_choice()
    computer = get_computer_choice()
    
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    
    result = determine_winner(user, computer)
    print("\nResult:", result)

# Run the game
play_game()

import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print("\nYour choice:", user_choice)
    print("Computer's choice:", computer_choice)
    print(result)

def play_game():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        
        if user_choice not in choices:
            print("Invalid choice! Please choose again.")
            continue
        
        computer_choice = random.choice(choices)
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

print("Welcome to Rock-Paper-Scissors Game!")
print("Instructions: Rock beats scissors, scissors beat paper, and paper beats rock.")

# Scissors background
print("""
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

play_game()
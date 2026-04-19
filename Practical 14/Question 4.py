# Activity - 4

import random

def rock_paper_scissors(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        return f"It's a tie! Both chose {player_choice}."
    
    if (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'paper' and computer_choice == 'rock') or \
       (player_choice == 'scissors' and computer_choice == 'paper'):
        return f"You win! {player_choice} beats {computer_choice}."
    
    return f"You lose! {computer_choice} beats {player_choice}."

player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
while player_choice not in ['rock', 'paper', 'scissors']:
    player_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

result = rock_paper_scissors(player_choice)
print(result)

# Output:
# Enter your choice (rock, paper, or scissors): rock
# You win! rock beats scissors.


import random

# Initialize win counters
user_wins = 0
computer_wins = 0
total_games = 0

# Define possible options
options = ['rock', 'paper', 'scissors']

# Game loop
while True:
    # Get user input
    user_input = input("Type Rock/Paper/Scissors or press Q to quit: ").lower()

    # Check if the user wants to quit
    if user_input == 'q':
        break

    # Check for invalid input
    if user_input not in options:
        print("Invalid input, please try again.")
        continue

    # Generate computer's pick
    computer_pick = random.choice(options)
    print(f'Computer picked {computer_pick}.')

    # Determine the winner
    if user_input == computer_pick:
        print("It's a tie!")
    elif (user_input == 'rock' and computer_pick == 'scissors') or \
            (user_input == 'paper' and computer_pick == 'rock') or \
            (user_input == 'scissors' and computer_pick == 'paper'):
        print('You won!')
        user_wins += 1
    else:
        print('You lost.')
        computer_wins += 1

    # Increment total games played
    total_games += 1

# Display final results
print(f'\nFinal Results:')
print(f'Total games played: {total_games}')
print(f'You won {user_wins} times.')
print(f'The computer won {computer_wins} times.')
print(f'There were {total_games - user_wins - computer_wins} ties.')
print('Thanks for playing!')


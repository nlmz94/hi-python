import random


def play_rock_paper_scissors_against_computer():
    user_input = input("enter r for rock, p for paper and s for scissors : ")
    computer_input = random.choice(['r', 'p', 's'])
    print(f'Inputs : player : {user_input} and computer : {computer_input}')
    if user_input == computer_input:
        return 'It\'s a tie'
    if (user_input == 'r' and computer_input == 's') or (user_input == 's' and computer_input == 'p') or (
            user_input == 'p' and computer_input == 'r'):
        return 'Player wins'
    return 'Computer wins'

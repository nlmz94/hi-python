import random


def play_rock_paper_scissors_against_computer():
    user_input = input("enter r for rock, p for paper and s for scissors : ")
    computer_input = random.choice(['r', 'p', 's'])
    print(f'Inputs : player : {user_input} and computer : {computer_input}')
    if user_input not in ['r', 'p', 's']:
        return 'Incorrect input'
    if user_input == computer_input:
        return 'It\'s a tie'
    if (user_input == 'r' and computer_input == 's') or (user_input == 's' and computer_input == 'p') or (
            user_input == 'p' and computer_input == 'r'):
        return 'Player wins'
    return 'Computer wins'


def play_rock_paper_scissors_gameloop():
    user_score = 0
    ia_score = 0
    while user_score < 3 and ia_score < 3:
        round_winner = play_rock_paper_scissors_against_computer()
        print(round_winner)
        if round_winner == 'Player wins':
            user_score = user_score + 1
        if round_winner == 'Computer wins':
            ia_score = ia_score + 1
    print('PLAYER: ' + str(user_score) + ' | COMPUTER: ' + str(ia_score))
    if user_score == 3:
        return 'Player wins the game!'
    return 'Computer wins the game!'

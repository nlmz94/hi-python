import random


def guess_number(low_limit, high_limit):
    random_number = random.randint(int(low_limit), int(high_limit))
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between {low_limit} and {high_limit} : '))
        if guess > random_number:
            print('too high')
            high_limit = guess
        elif guess < random_number:
            print('too low')
            low_limit = guess
    print(f'you win, the number was {random_number}')
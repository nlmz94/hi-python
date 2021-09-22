import random
import string

from words import english_words


def get_valid_word(words):
    random_word = random.choice(words)
    while '-' in random_word or ' ' in random_word:
        random_word = random.choice(words)
    return random_word.upper()


def hangman():
    word = get_valid_word(english_words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters) > 0:
        print('You have used these bad letters : ',
              ' '.join(used_letters))
        current_word = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(current_word))
        user_letter = input('Guess a letter : ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print('Letter not in the word!')
        elif user_letter in used_letters:
            print('Letter already used ! try again')
        else:
            print('Invalid character !')
    print(f'Well played, the word was {word}')

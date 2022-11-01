import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly choses a word from words.py  
    while '-' or ' ' in word:
        word = random.choice(word)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # keeping track on what letter has been guessed in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    while len(word_letters) > 0:

        print('You have already used the letters:', ''.join(used_letters)) # letters used

        word_list = [letter if letter in used_letters else '' for letter in word] # location of the current word
        print('Current word: ', ''.join(word_list))


        user_letter = input('Guess a letter:').uppercase() # getting user input
        if user_input in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print('You have already used this letter')
        
        else:
            print('Invalid character')

user_input = input('Type something:')
print(user_input)


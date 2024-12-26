import random
from data import data 
import string

def get_valid_word(data):
    word = random.choice(data).upper()
    while '-' in word or ' ' in word:
        word = random.choice(data).upper()
    return word 
    
def hangman():
    word = get_valid_word(data) 
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    #Creamos la variable de vidas
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        #letter used
        print('You have', lives, 'lives left and you have used these letters', ' '.join(used_letters))
        
        #
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        #
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            #Si la letra esta en la palabra
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good guess! {user_letter} is in the word.")
            #Si la letra no esta en la palabra
            else:
                lives = lives - 1
                print('Letter is not in word. Please try again')                
        #Si la letra ya fue usada
        elif user_letter in used_letters:
            print('You have already used that character. Please try again')
        #Si la letra no es valida   
        else:
            print('Invalid character. Please enter a valid letter.')
    #Si se acaban las vidas
    if lives == 0:
        print('You have run out of lives. The word was', word)
    else:
        print(f'Congratulations! You guessed the word: {word}')

hangman()
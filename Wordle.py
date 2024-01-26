# File: Wordle.py

"""
This program generates a random 5-letter word and allows the user to guess.
"""

# imports
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    
    # initialize variables
    gw = WordleGWindow()
    

    # create random word
    random_word = random.choice(FIVE_LETTER_WORDS).upper()
    # for i in range(len(random_word)):
    #     gw.set_square_letter(0, i, random_word[i])
    
    print(random_word)

    # word guess
    def enter_action(guess):
        
        # check if word is in word list
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list.")
        # color correct/incorrect letters
        else:
            for i in range(len(guess)):
                if guess[i] == random_word[i]:
                    gw.set_square_color(0, i, CORRECT_COLOR)
                elif guess[i] in random_word:
                    gw.set_square_color(0, i, PRESENT_COLOR)
                else:
                    gw.set_square_color(0, i, MISSING_COLOR)            

    gw.add_enter_listener(enter_action)
            
# run program
if __name__ == "__main__":
    wordle()
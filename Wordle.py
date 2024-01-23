# File: Wordle.py

"""
This program generates a random 5-letter word and allows the user to guess.
"""

# imports
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    
    # initialize variables
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # create random word
    random_word = random.choice(FIVE_LETTER_WORDS).upper()
    # for i in range(len(random_word)):
    #     gw.set_square_letter(0, i, random_word[i])
    
    # word guess
    def enter_action(s):
        
        # check if word is in word list
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list.")
        # color correct/incorrect letters
        else:
            # gw.show_message("In word list.")
            
            gw.set_square_color(row, col, color)    
            
            
# run program
if __name__ == "__main__":
    wordle()
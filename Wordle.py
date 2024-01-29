# File: Wordle.py

"""
This program generates a random 5-letter word and allows the user to guess.
"""

# imports
import random
from tkinter import Tk, messagebox
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, CORRECT_COLOR_COLORBLIND, PRESENT_COLOR_COLORBLIND, MISSING_COLOR

# return true or false if colorblind mode is enabled
def colorblind_mode():
    root = Tk()
    root.withdraw()
    result = messagebox.askyesno("Colorblind Mode", "Do you want to enable colorblind mode?")
    root.destroy()
    return result

# main program
def wordle():
    
    # colorblind mode prompt, will use this later to change colors
    colorblind = colorblind_mode()
    
    # initialize variables
    gw = WordleGWindow()

    # create random word
    random_word = random.choice(FIVE_LETTER_WORDS).upper()
    # random_word = "GUESS"
    # print(random_word)

    # word guess
    def enter_action(guess):
        
        # check if word is 5 letters
        if len(guess.replace(" ", "")) == 5:
        
            # check if word is in word list
            if guess.lower() not in FIVE_LETTER_WORDS:
                gw.show_message("Not in word list.")
            
            # run program
            else:
                
                # create dictionary of random_word letters
                random_word_letter_count = {}
                for letter in random_word:
                    count = random_word_letter_count.get(letter, 0)
                    count += 1
                    random_word_letter_count[letter] = count
                
                # color correct letters
                for i in range(len(guess)):
                    
                    # first, color all letters missing
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                    
                    # then, color correct letters
                    if guess[i] == random_word[i]:
                        # change if colorblind mode
                        if colorblind:
                            gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR_COLORBLIND)
                        else:
                            gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                        random_word_letter_count[guess[i]] -= 1
                        
                # color present letters
                for i in range(len(guess)):
                    if (guess[i] in random_word) and (guess[i] != random_word[i]):
                        
                        # color only as many letters are in the word
                        if random_word_letter_count[guess[i]] > 0:
                            # change if colorblind mode
                            if colorblind:
                                gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR_COLORBLIND)
                            else:
                                gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                            random_word_letter_count[guess[i]] -= 1
                            
                # check if word is correct
                if guess.upper() == random_word:
                    gw.show_message("You win!")
                # check if last row
                elif gw.get_current_row() == N_ROWS - 1:
                    gw.show_message(f"Sorry, the word was {random_word}.")
                # if not, move to next row
                else:
                    gw.set_current_row(gw.get_current_row() + 1)

    # add enter key listener
    gw.add_enter_listener(enter_action)
            
# run program
if __name__ == "__main__":
    wordle()
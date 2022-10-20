import random

class Word:
    """The word to be guessed"""

    def __init__(self):
    
        """Constructs a Word

        Args:
            self (Word) An instance of Word
        """
        
        self._word = self.draw_word()

    def draw_word(self):
        """ Gets a random word"""
        with open("word_list") as file:
            word =

    def check_guess(self):
        """ checks to see if guess is in word. 
        If it is in the word then it displays place in word.
        """

    def is_guessed(self):
        """ tells player that letter was already guessed.
        """
        
from random import randint
from unittest.result import failfast
class Word:
    """The word to be guessed"""
    
    def __init__(self):
        """Constructs a Word

        Args:
            self (Word) An instance of Word
        """
        
        word_list = ['wares',
                    'soup',
                    'mount',
                    'extend',
                    'brown',
                    'expert',
                    'tired',
                    'humidity',
                    'backpack',
                    'crust',
                    'dent',
                    'market',
                    'knock',
                    'smite',
                    'windy',
                    'coin',
                    'throw',
                    'silence',
                    'bluff',
                    'downfall',]
        
        random_index = randint(0, len(word_list) - 1)
        self._word = word_list[random_index]
        self._guessed_letters = ""
                                        
    def draw_word(self):
        """ Gets a random word
        """
        
        print("")
        for letter in self._word:
            if letter in self._guessed_letters:
                print(f"{letter}", end="")
            else:
                print("_", end="")
        print("")
        
    def check_guess(self, guess):
        """ checks to see if guess is in word. 
        If it is in the word then it displays place in word.
        """
        if guess in self._word:
            self._guessed_letters += guess
            return True
        else:
            return False

    def is_guessed(self):
        """ tells player that letter was already guessed.
        """
        
        fail_count = 0

        for letter in self._word:
            if letter not in self._guessed_letters:
                fail_count += 1

        return (fail_count == 0)
            
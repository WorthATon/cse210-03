from game.terminal import Terminal
from game.jumper import Jumper
from game.word import Word

class Player:
    """The person that handles the game.
    
    The responsibility of a Player is to control the sequence of play.
    
    Attributes:
        _word_to_guess (Word): The word the player has to guess
        _jumper (Jumper): The games jumper
        _terminal (Terminal): For getting and displaying information on the terminal.
    """
    
    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): and instance of Player
        """

        self._word_to_guess = ""
        self._jumper = ""
        self._health = 5
        self._terminal = Terminal()
        
        
    def start_game(self):
        """Starts the game by running the game loop
        
        Args:
            self (Player): an instance of Player
        """
        
        while Jumper.is_alive(self):
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        
    def _get_inputs(self):
        """Makes a guess for the word.
        
        Args:
            self (Player): An instance of Player
        """
        pass
    
    def _do_updates(self):
        """Determines if the Jumper has any lives left or if the word has been guessed.
        
        Args: 
            self (Player): An instance of Player
        """
        pass
    
    def _do_outputs(self):
        """Displays the Jumper's state and the word status.
        
        Args:
            self (Player): an instance of Player
        """
        pass
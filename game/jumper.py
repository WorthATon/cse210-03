class Jumper:
    """The jumper represent the guessing attempts the player has.
    
    Attributes:
        _health (integer): The guessing attempts left
        _image (string list): A graphic representation of the guessing attempts left
    """

    def __init__(self):
        """Constructs a new jumper.
        
        Args:
            self (Jumper): an instance of Jumper
        """
        self._health = 4
        self._image = [" ___", 
                     "/___\\"
                    ,"\   / "
                    , " \ /"
                    ,  "  0"
                    ,"/ | \\"
                    , " / \\"
                    ,"\n^^^^^^^"]

    def draw_jumper(self):
        """Draws the player with jumper on the screen according to attempts remaining.
        
        Args:
            self (Jumper): an instance of Jumper
        """        
        if self._health < 1:
            self._image[0] = "  X"
        
        print("")
        for layer in self._image: #variable layer declared for each item in list.
            print (layer)
        print("")

    def take_health(self):
        """Diminishes one attempt to _health variable on failed attempt
        
        Args:
            self (Jumper): an instance of Jumper
        """
        self._health  -= 1
        self._image.pop(0)  #method to remove designated item in a list (default is last item)

    def is_alive(self):
        """Determines if there are guessing attempts remaining.
        
        Args:
            self (Jumper): an instance of Jumper
        """
        if self._health == 0:
           return False 
        else: 
            return True

# jumper = Jumper(4)       test code to make sure jumper prints a jumper
# jumper.draw_jumper()
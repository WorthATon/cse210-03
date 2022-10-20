class Jumper:

    def __init__(self):
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
        
        if self._health < 1:
            self._image[0] = "  X"
        
        print("")
        for layer in self._image: #variable layer declared for each item in list.
            print (layer)
        print("")

    def take_health(self):
        self._health  -= 1
        self._image.pop(0)  #method to remove designated item in a list (default is last item)

    def is_alive(self):
        if self._health == 0:
           return False 
        else: 
            return True

# jumper = Jumper(4)       test code to make sure jumper prints a jumper

# jumper.draw_jumper()
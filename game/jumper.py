class Jumper:

    def __init__(self, health):
       self._health = health
       self._image = [" ___", 
                     "/___\\"
                    ,"\   / "
                    , " \ /"
                    ,  "  0"
                    ,"/ | \\"
                    , " / \\"
                    ,"^^^^^^^"]

    def draw_jumper(self):
        for layer in self._image: #variable layer declared for each item in list.
            print (layer)
  

    def take_health(self):
        self._health  -= 1
        self._image.pop(0)  #method to remove designated item in a list (default is last item)
        if self._image[0] =="0": #checks to see if any layers above the head, if not, first layer = head. (game over)
            self._image[0] ="x"


    def is_alive(self):
        if self._health == 0:
           return False 
        else: 
            return True

# jumper = Jumper(4)       test code to make sure jumper prints a jumper

# jumper.draw_jumper()
import random

class Random():
    #a dumb snake that chooses a random direction

    def __init__(self):
        pass
    

    def start(self, data):
        #setup
        pass

    def move(self, data):
        directions = ['up', 'down', 'left', 'right']
        direction = random.choice(directions)

        return direction

    def end(self, data):
        #teardown
        pass
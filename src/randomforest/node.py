LEFT  = 0
RIGHT = 1

class Node(object):
    def __init__(self, direction, numobservations, purity):
        self.direction          = direction
        self.numobservations    = numobservations
        self.purity             = purity
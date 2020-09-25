class Position:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to_tuple(self):
        return (self.x, self.y)
    
    def equals(self, position):
        return self.x == position.x and self.y == position.y
        
    def __str__(self):
        return 'Position: ({}, {})'.format(self.x, self.y)
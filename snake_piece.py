from position import Position

class Snake_Piece:
    
    def __init__(self, move_direction, position):
        self.position = position
        self.move_direction = move_direction
               
    def __str__(self):
        return 'Snake_Piece: [position: {}, move_direction: {}]'.format(self.position, self.move_direction)
    
    def copy(self):
        return Snake_Piece(self.move_direction, Position(self.position.x, self.position.y))
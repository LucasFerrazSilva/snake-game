import pygame
import random
import colors
import properties

from position import Position

class Food:
    
    def __init__(self):        
        self.color = colors.RED
        
        self.set_position()
        
        
    def draw(self, screen):
        if self.blink_frequency <= 0:
            self.is_even = not self.is_even
            self.__set_blink_frequency() 
        
        self.blink_frequency -= 1
        
        if self.is_even:
            pygame.draw.rect(screen, self.color, [self.position.x, self.position.y, properties.BLOCK_SIZE, properties.BLOCK_SIZE])
    
    
    def set_position(self, snake_pieces = None):
        valid = False
        
        while not valid:
            number_of_blocks_in_one_line = properties.GAME_WINDOW_SIZE//properties.BLOCK_SIZE
        
            random_x = random.randrange(number_of_blocks_in_one_line) * properties.BLOCK_SIZE + properties.GAME_WINDOW_START_POSITION.x
            random_y = random.randrange(number_of_blocks_in_one_line) * properties.BLOCK_SIZE + properties.GAME_WINDOW_START_POSITION.y
            
            self.position = Position(random_x, random_y)
            
            valid = True
            
            if snake_pieces != None:
                for snake_piece in snake_pieces:
                    if self.position.equals(snake_piece.position):
                        valid = False
        
        self.is_even = True
        self.__set_blink_frequency()
        
    def __set_blink_frequency(self):
        self.blink_frequency = 25
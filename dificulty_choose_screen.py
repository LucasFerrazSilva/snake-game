import pygame
import properties
import colors

from position import Position
from dificulty_options import Dificulty_Options

class Dificulty_Choose_Screen:
    
    def __init__(self):
        self.text_font = pygame.font.SysFont('Montserrat', 25, False, False)
        self.text_position = Position(properties.WINDOW_SIZE[0]/2 - 100, properties.WINDOW_SIZE[1]/2 - 100)
        
    def draw(self, screen):
        text_message = self.text_font.render('Choose the dificulty: ', True, colors.WHITE)
        screen.blit(text_message, self.text_position.to_tuple())
        
        options = [
            '1 - Very Easy',
            '2 - Easy',
            '3 - Normal',
            '4 - Hard',
            '5 - Very Hard'
        ]
        
        option_count = 1
        
        for option in options:        
            option_position = self.text_position.to_tuple()
            text_message = self.text_font.render(option, True, colors.WHITE)
            screen.blit(text_message, [option_position[0] + 25, option_position[1] + (option_count * 30)])
            option_count += 1
        
        
        
    def set_dificulty(self, dificulty_input):
        dificulty_option = Dificulty_Options.NORMAL
        
        if dificulty_input in [pygame.K_1, pygame.K_KP1]:
            dificulty_option = Dificulty_Options.VERY_EASY
            
        elif dificulty_input in [pygame.K_2, pygame.K_KP2]:
            dificulty_option = Dificulty_Options.EASY
            
        elif dificulty_input in [pygame.K_3, pygame.K_KP3]:
            dificulty_option = Dificulty_Options.NORMAL
              
        elif dificulty_input in [pygame.K_4, pygame.K_KP4]:
            dificulty_option = Dificulty_Options.HARD
              
        elif dificulty_input in [pygame.K_5, pygame.K_KP5]:
            dificulty_option = Dificulty_Options.VERY_HARD
            
        properties.SNAKE_SPEED = dificulty_option.value
import pygame
import colors
import properties

from position import Position

class Game_Over:
    
    def __init__(self):
        self.font_game_over = pygame.font.SysFont('Montserrat', 40, True, False)        
        self.font_message = pygame.font.SysFont('Montserrat', 25, False, False)
                
        self.game_over_position = Position(properties.WINDOW_SIZE[0]/2 - 75, properties.WINDOW_SIZE[1]/2 - 100)
        self.score_position = Position(properties.WINDOW_SIZE[0]/2 - 50, self.game_over_position.y + 40)
        self.higher_scores_position = Position(properties.WINDOW_SIZE[0]/2 - 50, self.game_over_position.y + 70)
        self.message_position = Position(properties.WINDOW_SIZE[0]/2 - 170, self.game_over_position.y + 220)
    
    def draw(self, screen, score, higher_scores):
        #self.__draw_center_lines(screen)
        
        text_game_over = self.font_game_over.render('Game Over', True, colors.WHITE)
        screen.blit(text_game_over, self.game_over_position.to_tuple())
        
        text_score = self.font_message.render('Your Score: {}'.format(score), True, colors.WHITE)
        screen.blit(text_score, self.score_position.to_tuple())
        
        self.higher_scores_position = Position(properties.WINDOW_SIZE[0]/2 - 50, self.game_over_position.y + 70)
        
        text_higher_scores = self.font_message.render('Higher Scores:', True, colors.WHITE)
        screen.blit(text_higher_scores, self.higher_scores_position.to_tuple())
        
        self.higher_scores_position.x += 40
        
        for i in range(len(higher_scores)):
            higher_score = higher_scores[i]
            
            self.higher_scores_position.y += 25
            
            text_higher_scores = self.font_message.render('{}: {}'.format(i+1, higher_score), True, colors.WHITE)
            screen.blit(text_higher_scores, self.higher_scores_position.to_tuple())            
        
        
        text_message = self.font_message.render('Press "Space" to play again or "Esc" to quit', True, colors.WHITE)
        screen.blit(text_message, self.message_position.to_tuple())
        
    def __draw_center_lines(self, screen):        
        pygame.draw.line(screen, colors.RED, [properties.WINDOW_SIZE[0]/2, 0], [properties.WINDOW_SIZE[0]/2, properties.WINDOW_SIZE[1]])
        pygame.draw.line(screen, colors.RED, [0, properties.WINDOW_SIZE[1]/2], [properties.WINDOW_SIZE[0], properties.WINDOW_SIZE[1]/2])
import pygame
import colors
import properties

from position import Position

class Score:
    
    def __init__(self, score=0):
        self.score = score
        self.font = pygame.font.SysFont('Montserrat', 30, False, False)
        
        score_position_y = properties.GAME_WINDOW_START_POSITION.y
        self.text_position = Position(10, score_position_y)
        self.text_score_position = Position(30, score_position_y + 25)
        
        
    def improve(self):
        self.score += 1
    
    
    def draw(self, screen):
        text = self.font.render('Score', True, colors.WHITE)
        text_score = self.font.render(str(self.score), True, colors.WHITE)
        
        screen.blit(text, self.text_position.to_tuple())
        screen.blit(text_score, self.text_score_position.to_tuple())
    
    def save(self):
        scores = self.get_higher_scores()
        
        max_scores = []
                
        actual_score = self.score
        
        for score in scores:
            if int(score) > int(actual_score):
                max_scores.append(score)
            else:
                max_scores.append(actual_score)
                actual_score = score
        
        with open('scores.txt', 'w') as scores_file:
            for score in max_scores:
                scores_file.writelines((str(score), '\n'))
    
    def  get_higher_scores(self):
        scores = []
        
        with open('scores.txt', 'r') as scores_file:
            for i in range(5):
                scores.append(int(scores_file.readline()))
         
        return scores
        
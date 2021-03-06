import pygame
import colors
import properties

from grid import Grid
from food import Food
from snake import Snake
from move_direction import Move_Direction
from score import Score
from game_over import Game_Over
from dificulty_choose_screen import Dificulty_Choose_Screen
from beat_the_game_message import Beat_The_Game_Message


def init():
    pygame.init() # inicia a engine do jogo
    screen = pygame.display.set_mode(properties.WINDOW_SIZE) # cria a janela principal
    pygame.display.set_caption('Snake Game') # define o título da janela
    clock = pygame.time.Clock() # pega o clock, usado para definir o fps do jogo
    
    return screen, clock


def quit():
    pygame.display.quit() # fecha a janela principal
    pygame.quit() # para a engine
    
    
def init_objects():
    score = Score()
    grid = Grid()
    food = Food()
    snake = Snake()
    game_over = Game_Over()
    dificulty_choose = Dificulty_Choose_Screen()
    beat_the_game_message = Beat_The_Game_Message()
    
    food.set_position(snake.snake_pieces)
    
    return score, grid, food, snake, game_over, dificulty_choose, beat_the_game_message

def main():
    screen, clock = init()
    score, grid, food, snake, game_over, dificulty_choose, beat_the_game_message = init_objects()
    
    done = False
    is_game_over = False
    must_choose_dificulty = True
    paused = False
    won_the_game = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                done = True
                
            elif (is_game_over or won_the_game) and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                score, grid, food, snake, game_over, dificulty_choose, beat_the_game_message = init_objects()
                is_game_over = False
                won_the_game = False
                must_choose_dificulty = True
                
            elif must_choose_dificulty and event.type == pygame.KEYDOWN and event.key in properties.DIFICULTY_OPTIONS:
                dificulty_choose.set_dificulty(event.key)
                must_choose_dificulty = False                
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                snake.move(Move_Direction.UP)
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                snake.move(Move_Direction.DOWN)
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                snake.move(Move_Direction.LEFT)
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                snake.move(Move_Direction.RIGHT)
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused
        
        if not paused:
            screen.fill(colors.DARK_GREY)            
            
            if must_choose_dificulty:
                dificulty_choose.draw(screen)    
            elif won_the_game:
                beat_the_game_message.draw(screen, score.score, score.get_higher_scores())                
            elif is_game_over:
                game_over.draw(screen, score.score, score.get_higher_scores())
            else:
                snake.move(None)
        
                if snake.hit_border_or_body():
                    is_game_over = True
                    score.save()
                    continue
                
                if snake.ate(food):
                    if snake.beat_the_game():
                        won_the_game = True
                        continue
                    else:
                        food.set_position(snake.snake_pieces)
                        snake.must_increase = True
                        score.improve()
                
                score.draw(screen)
                grid.draw_border_only(screen)    
                food.draw(screen)
                snake.draw(screen)
            
            pygame.display.flip()
            clock.tick(60)
            
    quit()
        
if __name__ == "__main__":
    main()


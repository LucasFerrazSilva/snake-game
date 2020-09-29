import pygame
from position import Position
from move_direction import Move_Direction

GAME_WINDOW_SIZE = 600
MARGIN_SIZE = 20
SCORE_SIZE = 80

WINDOW_SIZE = (GAME_WINDOW_SIZE + SCORE_SIZE + MARGIN_SIZE, GAME_WINDOW_SIZE + MARGIN_SIZE * 2)

GAME_WINDOW_START_POSITION = Position(SCORE_SIZE, MARGIN_SIZE)
GAME_WINDOW_FINAL_POSITION = Position(GAME_WINDOW_START_POSITION.x + GAME_WINDOW_SIZE, GAME_WINDOW_START_POSITION.y + GAME_WINDOW_SIZE)

BLOCK_SIZE = 100
NUMBER_OF_BLOCKS = (GAME_WINDOW_SIZE / BLOCK_SIZE) ** 2

SNAKE_SPEED = 7

DIFICULTY_OPTIONS = [pygame.K_1, pygame.K_KP1, pygame.K_2, pygame.K_KP2, pygame.K_3, pygame.K_KP3, pygame.K_4, pygame.K_KP4, pygame.K_5, pygame.K_KP5]

MOVES = [
    Move_Direction.UP, Move_Direction.UP, Move_Direction.UP, Move_Direction.RIGHT, Move_Direction.DOWN, Move_Direction.DOWN, 
    Move_Direction.RIGHT, Move_Direction.UP, Move_Direction.UP, Move_Direction.RIGHT, Move_Direction.DOWN, Move_Direction.DOWN, 
    Move_Direction.RIGHT, Move_Direction.UP, Move_Direction.UP, Move_Direction.RIGHT, Move_Direction.DOWN, Move_Direction.DOWN, 
    Move_Direction.DOWN, Move_Direction.DOWN, Move_Direction.DOWN, Move_Direction.LEFT, Move_Direction.UP, Move_Direction.UP, 
    Move_Direction.LEFT, Move_Direction.DOWN, Move_Direction.DOWN, Move_Direction.LEFT, Move_Direction.UP, Move_Direction.UP, 
    Move_Direction.LEFT, Move_Direction.DOWN, Move_Direction.DOWN, Move_Direction.LEFT, Move_Direction.UP, Move_Direction.UP]

LET_SNAKE_PLAY = True
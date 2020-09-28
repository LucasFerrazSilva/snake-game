import pygame
import colors
import properties

from position import Position
from move_direction import Move_Direction
from snake_piece import Snake_Piece

class Snake:
    
    def __init__(self):        
        self.color = colors.GREEN
        
        self.snake_pieces = []
        
        self.__generate_initial_body()
        
        self.__init_speed()
    
    
    
    def move(self, move_direction):
        actual_move_direction = self.snake_pieces[0].move_direction
                
        if move_direction != None:
            if self.__is_invalid_move(move_direction, actual_move_direction):
                return
            
            self.snake_pieces[0].move_direction = move_direction             
        elif self.speed > 0: # controla a velocidade do jogo
            self.speed -= 1
            return
        
        self.__init_speed()        
        
        next_move_direction = self.snake_pieces[0].move_direction        
        
        for snake_piece in self.snake_pieces:
            if snake_piece.move_direction == Move_Direction.UP:
                snake_piece.position.y -= properties.BLOCK_SIZE
            elif snake_piece.move_direction == Move_Direction.DOWN:
                snake_piece.position.y += properties.BLOCK_SIZE
            elif snake_piece.move_direction == Move_Direction.LEFT:
                snake_piece.position.x -= properties.BLOCK_SIZE
            elif snake_piece.move_direction == Move_Direction.RIGHT:
                snake_piece.position.x += properties.BLOCK_SIZE
            
            temp_move_direction = snake_piece.move_direction
            snake_piece.move_direction = next_move_direction
            next_move_direction = temp_move_direction
    
    
    def __is_invalid_move(self, move_direction, actual_move_direction):
        return (move_direction.value - actual_move_direction.value) % 2 == 0
       
        
    def draw(self, screen):        
        for piece in self.snake_pieces:
            self.__draw_rect(screen, piece.position)
            
    def __draw_rect(self, screen, position):
        pygame.draw.rect(screen, self.color, [position.x, position.y, properties.BLOCK_SIZE - 1, properties.BLOCK_SIZE - 1])
            
    
    def increase_size(self):        
        last_snake_piece = self.snake_pieces[-1]
        
        snake_piece = last_snake_piece.copy()
        
        if snake_piece.move_direction == Move_Direction.UP:
            snake_piece.position.y += properties.BLOCK_SIZE
        elif snake_piece.move_direction == Move_Direction.DOWN:
            snake_piece.position.y -= properties.BLOCK_SIZE
        elif snake_piece.move_direction == Move_Direction.LEFT:
            snake_piece.position.x += properties.BLOCK_SIZE
        elif snake_piece.move_direction == Move_Direction.RIGHT:
            snake_piece.position.x -= properties.BLOCK_SIZE
            
        self.snake_pieces.append(snake_piece)
        
        
    def ate(self, food):
        return self.snake_pieces[0].position.equals(food.position)
    
    
    def hit_border_or_body(self):
        return self.__hit_border() or self.__hit_body()
    
    
        
    def __hit_border(self):
        head = self.snake_pieces[0]
        
        return head.position.x < properties.GAME_WINDOW_START_POSITION.x or head.position.x >= properties.GAME_WINDOW_FINAL_POSITION.x \
            or head.position.y < properties.GAME_WINDOW_START_POSITION.y or head.position.y >= properties.GAME_WINDOW_FINAL_POSITION.y

            
    def __hit_body(self):
        head = self.snake_pieces[0]
        
        for i in range(1, len(self.snake_pieces), 1):            
            if head.position.equals(self.snake_pieces[i].position):
                return True
            
        return False            
        
    
    def __init_speed(self):
        self.speed = properties.SNAKE_SPEED
    
    
    def __generate_initial_body(self):        
        head_snake_piece = self.__init_head_snake_piece()
        
        self.snake_pieces.append(head_snake_piece)
        
        previous_snake_piece = head_snake_piece
        
        for i in range(2):            
            snake_piece = previous_snake_piece.copy()
            
            snake_piece.position.x += properties.BLOCK_SIZE # move um bloco para a direita
            
            self.snake_pieces.append(snake_piece)
            
            previous_snake_piece = snake_piece            
            
    
    def __init_head_snake_piece(self):
        number_of_blocks_in_one_line = properties.GAME_WINDOW_SIZE/properties.BLOCK_SIZE
        
        middle_block = number_of_blocks_in_one_line//2 # pega o número inteiro da divisão
        
        x = middle_block * properties.BLOCK_SIZE + properties.GAME_WINDOW_START_POSITION.x
        y = middle_block * properties.BLOCK_SIZE + properties.GAME_WINDOW_START_POSITION.y
        
        return Snake_Piece(Move_Direction.LEFT, Position(x, y))            
            
import pygame
import colors
import properties

class Grid:
    
    
    def draw(self, screen):
        self.__draw_vertical_lines(screen)
        self.__draw_horizontal_lines(screen)
        
    
    def draw_border_only(self, screen):
        x_init = properties.GAME_WINDOW_START_POSITION.x
        x_final = properties.GAME_WINDOW_FINAL_POSITION.x
        
        y_init = properties.GAME_WINDOW_START_POSITION.y
        y_final = properties.GAME_WINDOW_FINAL_POSITION.y
        
        pygame.draw.line(screen, colors.GREY, [x_init, y_init], [x_final, y_init])
        pygame.draw.line(screen, colors.GREY, [x_init, y_init], [x_init, y_final])
        pygame.draw.line(screen, colors.GREY, [x_init, y_final], [x_final, y_final])
        pygame.draw.line(screen, colors.GREY, [x_final, y_init], [x_final, y_final])
        
            
    def __draw_vertical_lines(self, screen):
        initial_y = properties.GAME_WINDOW_START_POSITION.y - 1
        final_y = properties.GAME_WINDOW_FINAL_POSITION.y - 1
        
        for x in range(properties.GAME_WINDOW_START_POSITION.x - 1, properties.GAME_WINDOW_FINAL_POSITION.x, properties.BLOCK_SIZE):
            initial_position = [x, initial_y]
            final_position = [x, final_y]
            
            pygame.draw.line(screen, colors.DARK_MEDIUM_GREY, initial_position, final_position)
    
    def __draw_horizontal_lines(self, screen):
        initial_x = properties.GAME_WINDOW_START_POSITION.x - 1
        final_x = properties.GAME_WINDOW_FINAL_POSITION.x - 1
        
        for y in range(properties.GAME_WINDOW_START_POSITION.y - 1, properties.GAME_WINDOW_FINAL_POSITION.y, properties.BLOCK_SIZE):
            initial_position = [initial_x, y]
            final_position = [final_x, y]
            
            pygame.draw.line(screen, colors.DARK_MEDIUM_GREY, initial_position, final_position)
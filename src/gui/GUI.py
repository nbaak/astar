import pygame

class GUI():
    
    def __init__(self, width, height, title="PyGame"):
        self.width = width
        self.height = height
        
        self.surface = pygame.display.set_mode(size=(width, height))
        
        pygame.display.set_caption(title)
        self.surface.fill((255,255,255))    # WHITE
        
    def get_field_size(self):
        return self.width, self.height
    
    def fill(self, color):
        self.surface.fill(color)
        
    def update(self):
        pygame.display.update()
        
    def flip(self, flip=True):
        if flip:
            pygame.display.flip()
                                              
    def draw_square(self, point, height, width, color, filled=0, flip=True):
        '''
            @param point: (y,x)
        '''
        x, y = point
        pygame.draw.rect(self.surface, color, pygame.Rect(x,y, width, height), filled)
        self.flip(flip)
    
    def draw_line(self, point, target, color, flip=True):
        '''
            @param point: (y,x)
        '''
        f_x, f_y = point
        t_x, t_y = target
        
        pygame.draw.line(self.surface, color, point, target)
        self.flip(flip)
        #print(f"draw: {point} -> {target}")
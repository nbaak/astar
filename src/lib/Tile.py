from lib.Colors import Colors
from lib.Node import Node

class Tile(Node):
    
    def __init__(self, position, color, tile_width, tile_height):
        super().__init__(position, color)
        
        self.width = tile_width
        self.height = tile_height
        
    def make_start(self):
        self.value = Colors.ORANGE
        
    def make_end(self):
        self.value = Colors.TRUQUOISE
        
    def make_barrier(self):
        self.value = Colors.BLACK
        
    def make_empty(self):
        self.value = Colors.WHITE
        
    def make_closed(self):
        self.value = Colors.RED
        
    def make_path(self):
        self.value = Colors.PURPLE
        
    def make_open(self):
        self.value = Colors.GREEN
        
        
    def is_closed(self):
        return self.value == Colors.RED
    
    def is_open(self):
        return self.value == Colors.GREEN
    
    def is_barrier(self):
        return self.value == Colors.BLACK
    
    def is_start(self):
        return self.value == Colors.ORANGE
    
    def is_end(self):
        return self.value == Colors.TRUQUOISE
    
    def update_neighbors(self, grid):
        self.neighbors = []
        col, row = self.position
        grid_cols = len(grid)
        grid_rows = len(grid[0])
                
        if row < grid_rows-1 and not grid[col][row+1].is_barrier(): # down
            self.add_neighbor(grid[col][row+1])
            
        if row > 0 and not grid[col][row-1].is_barrier(): # up
            self.add_neighbor(grid[col][row-1])
            
        if col < grid_cols-1 and not grid[col+1][row].is_barrier(): # right
            self.add_neighbor(grid[col+1][row])
            
        if col > 0 and not grid[col-1][row].is_barrier(): # left
            self.add_neighbor(grid[col-1][row])
        
    def draw(self, gui, border=False, flip=True):
        p_x, p_y = self.position
        gui.draw_square((p_x*self.width, p_y*self.height), self.height, self.width, self.value, border, flip)
        
    def info(self):
        print(f"{self.position}: {self.width}/{self.height}")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
from gui.GUI import GUI
from lib.Tile import Tile
from lib.Colors import Colors
import time


class Board():
    
    def __init__(self, rows=10, cols=10, gui=None, field_size=None):
        self.rows = rows
        self.cols = cols
                
        if not field_size:
            field_size = (100,100)
        print(field_size)
        self.width, self.height = field_size
        
        self.tile_width = self.width // cols
        self.tile_height = self.height // rows
        
        if not gui:
            gui = GUI(self.width,self.height, 'Board')
            print("gui created")
            
        self.gui = gui
        print(self.gui.get_field_size())
        
        self.reset()
        
        
    def reset(self):
        self.grid = []
        self.make_grid()
        
        self.draw()
    
    def make_grid(self):
        for col in range(self.cols):
            self.grid.append([])
            for row in range(self.rows):
                position = (col,row)
                tile = Tile(position, Colors.WHITE, self.tile_width, self.tile_height)
                self.grid[col].append(tile)
                
    def draw_grid(self):
        for x in range(self.rows):
            self.gui.draw_line((0, x * self.tile_height), (self.width, x * self.tile_height), Colors.GREY, flip=False)
            
            for y in range(self.cols):
                self.gui.draw_line((y * self.tile_width, 0), (y * self.tile_width, self.height), Colors.GREY, flip=False)
    
    def draw(self):
        self.gui.fill(Colors.WHITE)
        for row in self.grid:
            for tile in row:
                tile.draw(self.gui, flip=False)
                
        self.draw_grid()
        self.gui.update()
        
    def get_clicked_position(self, pos):
        y,x = pos
        row = y // self.tile_width
        col = x // self.tile_height
        
        return row, col
        
    def get_tile(self, row, col):
        return self.grid[row][col]
    
    def update_neigbors(self):
        print('cols:',len(self.grid))
        print('rows:',len(self.grid[0]))
        
        for col in self.grid:
            for tile in col:
                tile.update_neighbors(self.grid)
    
    def reconstruct_path(self, path, end):
        while end in path:
            end = path[end]
            end.make_path()
    
if __name__ == "__main__":
    b = Board(rows=20, cols=10, gui=None, field_size=(2000,1000))
    time.sleep(5)
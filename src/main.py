from lib.Board import Board
from lib.AStar import AStar
import pygame
import time


def main():
    board = Board(rows=50, cols=50, gui=None, field_size=(1000,1000))
    gui = board.gui
    start = None
    end = None 
    
    run = True
    started = False
    
    while run:
        board.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if started:
                continue
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started and start and end:
                    board.update_neigbors()
                    astar = AStar(start, end, board.grid, gui)
                    path, end = astar.solve()
                    board.reconstruct_path(path, end)
                    start.make_start()
                    end.make_end()
                    
                if event.key == pygame.K_q:
                    run = False
                    
                if event.key == pygame.K_r:
                    start = None
                    end = None
                    board.reset()
                    
                if event.key == pygame.K_s:
                    pygame.image.save(gui.surface,"screenshot.jpg")
                    
            
            if pygame.mouse.get_pressed()[0]:   # left
                pos = pygame.mouse.get_pos()
                row, col = board.get_clicked_position(pos)
                
                tile = board.get_tile(row, col)
                
                if not start:
                    if not tile.is_end():
                        start = tile
                        tile.make_start()
                    
                elif start and not end:
                    if not tile.is_start():
                        end = tile
                        tile.make_end()
                    
                elif start and end:
                    if not tile.is_start() and not tile.is_end():
                        tile.make_barrier()
                        
                        
                print(f"clicked: {tile}")
                    
                
            
            elif pygame.mouse.get_pressed()[1]: # middle
                print(f"start: {start}")
                print(f"end  : {end}")
                
                
            elif pygame.mouse.get_pressed()[2]: # right
                pos = pygame.mouse.get_pos()
                row, col = board.get_clicked_position(pos)
                
                tile = board.get_tile(row, col)
                
                if tile.is_start():
                    start = None
                    
                elif tile.is_end():
                    end = None
                
                
                tile.make_empty()
                
                
    pygame.quit()


def debug():
    pass



if __name__ == '__main__':
    main()
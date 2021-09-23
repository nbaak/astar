
from queue import PriorityQueue
import math
import pygame
from sklearn import neighbors


def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


class AStar():
    
    
    def __init__(self, start, end, grid, gui):
        self.count = 0
        
        self.open_set = PriorityQueue()
        self.open_set.put((0, self.count, start))
        
        self.path = {}
        
        self.start = start
        self.end = end

        self.g_score = {node: float('inf') for col in grid for node in col}
        self.g_score[start] = 0

        self.f_score = {node: float('inf') for col in grid for node in col}
        self.f_score[start] = heuristic(self.start.get_position(), self.end.get_position())
        
        self.open_set_hash = {start}        
        

    def solve(self):        
        while not self.open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            current_node = self.open_set.get()[2]
            self.open_set_hash.remove(current_node)
            
            if current_node == self.end:
                return self.path, self.end
            
            for neighbor in current_node.get_neighbors():
                temp_g_score = self.g_score[current_node]+1
                
                if temp_g_score < self.g_score[neighbor]:
                    self.path[neighbor] = current_node
                    
                    self.g_score[neighbor] = temp_g_score
                    self.f_score[neighbor] = temp_g_score + heuristic(neighbor.get_position(), self.end.get_position())
                    
                    if neighbor not in self.open_set_hash:
                        self.count += 1
                        self.open_set.put((self.f_score[neighbor], self.count, neighbor))
                        self.open_set_hash.add(neighbor)
                        neighbor.make_open()
            
            if current_node != self.start:
                current_node.make_closed()
                
        return False  
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        
                
            
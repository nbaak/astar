
class Node:
    
    def __init__(self, position, value=None):
        self.position = position
        self.value = value
        self.neighbors = []
        
    def get_position(self):
        return self.position
    
    def set_value(self, new_value):
        self.value = new_value
        
    def get_value(self):
        return self.value
    
    def add_neighbor(self, node):
        self.neighbors.append(node)
        
    def get_neighbors(self):
        return self.neighbors
    
    def __str__(self):
        return f"{self.position[0]}/{self.position[1]}"
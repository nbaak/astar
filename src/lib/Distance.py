
class Distance:    
    
    @staticmethod
    def manhattan(p1, p2):
        x1,y1 = p1
        x2,y2 = p2
        return abs(x1-x2) + abs(y1-y2) 
    
    
    @staticmethod
    def euclidean(p1, p2):
        pass
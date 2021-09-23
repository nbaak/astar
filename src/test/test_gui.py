
from gui.GUI import GUI
import time

window_width = 200
window_height = 1000

point = (50,40)
width = 10
height = 10

RED = (255,0,0)
gui = GUI(window_width, window_height, 'Test Window')



color = RED
gui.draw_square(point, height, width, color)

time.sleep(3)
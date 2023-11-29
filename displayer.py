from pygame import *
from grid import *
import pathfinder

init()

screen = display.set_mode((800, 800), RESIZABLE)

mp = grid(size=(800, 800), spacing=0)
# mp = grid()

pointA = [0, 0]
mp.changeColor(pointA)

pointB = [24, 24]
mp.changeColor(pointB)

path = pathfinder.calculate_path(pointA, pointB)

for step in path:
    if step not in [path[0], path[-1]]:
        mp.changeColor(step, (0, 255, 0))

on = True
while on:
    for e in event.get():
        if e.type == QUIT:
            on = False
        if e.type == MOUSEBUTTONUP:
            coords = mp.get_collide(mouse.get_pos())
            if coords:
                pointA = coords
                mp.reset()
                mp.changeColor(pointA)
                mp.changeColor(pointB)
                path = pathfinder.calculate_path(pointA, pointB)
                for step in path:
                    if step not in [path[0], path[-1]]:
                        mp.changeColor(step, (0, 255, 0))
    screen.fill((255, 255, 255))
    
    mp.draw(screen)
    
    display.update()
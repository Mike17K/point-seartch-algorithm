import numpy as np
from tree import *
from visuals import *
import time
import pygame as pg

t=Tree(node(4,0))

pg.init()

screen = pg.display.set_mode((1000,1000))

screen.fill((255,255,255))
pg.display.update()

points_data=[]


for i in range(50): 
    holding_mouse_left_down=False
    start_cords=None
    end_cords=None
    running = True
    while running:
        screen.fill((255,255,255))
        for event in pg.event.get():
            if event.type==pg.MOUSEBUTTONDOWN:
                holding_mouse_left_down=True
                start_cords = pg.mouse.get_pos()
            if event.type==pg.MOUSEBUTTONUP:
                holding_mouse_left_down=False
                end_cords = pg.mouse.get_pos()
        
        if holding_mouse_left_down: #drawing the square for selection
            x,y = pg.mouse.get_pos()
            draw_select_rect(screen,start_cords,x,y)

        if not holding_mouse_left_down:
            if start_cords != None and end_cords != None:
                distance = np.sqrt((end_cords[0]-start_cords[0])**2+(end_cords[1]-start_cords[1])**2)
                if distance<10:
                    #adding point
                    x,y =start_cords
                    running = False
                else:
                    pass #select all points from tree in the space of start_cords and end_cords
                    print("select points")
                    print(t.select(start_cords,end_cords))
                    start_cords=None
                    end_cords=None
        
        for point in points_data:
            draw_Point(screen,point[0],point[1])
        pg.display.update()

    tmp=node(x,y)
    #tmp=node(*np.random.randint(800,size=len(t.root.array)))

    depth , index_leaf = t.add(tmp)
    points_data.append([[str(i),str(depth),str(index_leaf)],tmp])

    pg.display.update()




print("\nPreorder: \n")
preorder(t.root)

while True:
    pass

pg.quit()


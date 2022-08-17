import pygame as pg
import numpy as np

def draw_select_rect(screen,start_cords,x,y):
    distance = np.sqrt((x-start_cords[0])**2+(y-start_cords[1])**2)
    if distance>10:  
        if -start_cords[0]+x>0:
            if -start_cords[1]+y>0:
                pg.draw.rect(screen,(150,150,150),(start_cords[0],start_cords[1],-start_cords[0]+x,-start_cords[1]+y))
            else:
                pg.draw.rect(screen,(150,150,150),(start_cords[0],y,-start_cords[0]+x,start_cords[1]-y))
        else:
            if -start_cords[1]+y>0:
                pg.draw.rect(screen,(150,150,150),(x,start_cords[1],start_cords[0]-x,-start_cords[1]+y))
            else:
                pg.draw.rect(screen,(150,150,150),(x,y,start_cords[0]-x,start_cords[1]-y))

def draw_Point(screen,string,tmp):
    
    pg.draw.circle(screen, (0, 255, 0),[tmp.array[0], tmp.array[1]], 5)

    font = pg.font.SysFont(None, 24)
    img = font.render(string[0], True, (0,0,0))
    screen.blit(img, (tmp.array[0], tmp.array[1]))

    font = pg.font.SysFont(None, 24)
    img = font.render(string[1], True, (0,255,0))
    screen.blit(img, (tmp.array[0]+20, tmp.array[1]))
    
    font = pg.font.SysFont(None, 24)
    img = font.render(string[2], True, (0,0,0))
    screen.blit(img, (tmp.array[0]+20+20, tmp.array[1]))

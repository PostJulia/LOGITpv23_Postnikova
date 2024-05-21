import pygame
import random
import sys
pygame.init()
ekraani_pind=pygame.display.set_mode( (640, 480))
ekraani_pind.fill( (0,0,255))

red=[255, 0, 0]
green=[0, 255, 0]
blue=[0, 0, 255]
pink=[255, 153, 255]
lBlue=[153, 255, 255]

pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Majake")
pind.fill(lBlue)

def drawHouse(x, y, width, height, screen, color):
    points=[(x, y- ((3/4)*height)), (x, y), (x+width,y), (x+width,y-(3/4)*height), (x, y- ((3/4)*height)), (x+width/2,y-height), (x+width,y-(3/4)*height)]
    lineThickness=3
    pygame.draw.lines(screen, color, False, points, lineThickness)

def Uks(x, y, width, height, screen, color):
    points=[(x, y), (x, y- ((1/2)*height)), (x+(1/3)*width,y-(1/2)*height), (x+(1/3)*width,y), (x,y)]
    lineThickness2=3
    pygame.draw.lines(screen, color, True, points, lineThickness2)
    pygame.draw.circle(screen, color, (x+10,y-(1/4)*height),10) 

def Aken(x, y, width, height, screen, color):
    points=[(x, y), (x, y- ((1/2)*height)), (x+(1/3)*width,y-(1/2)*height), (x+(1/3)*width,y), (x,y)]
    lineThickness2=0
    pygame.draw.circle(screen, color, True, points, lineThickness2)

center_coordinates=(500, 70) 
radius=50  
pygame.draw.circle(ekraani_pind, (255, 255, 0), center_coordinates, radius)

ristkylik1=pygame.Rect(0, 400, 700, 100)
pygame.draw.rect(ekraani_pind, (0,255,0), ristkylik1)

drawHouse(100,400,300,400,pind,(0,0,255))
Uks(100,400,300,400,pind,(0,0,255))
Aken(250,300,30,pind,(0,0,255))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()


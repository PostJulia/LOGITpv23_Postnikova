import pygame
import sys
pygame.init()

red=[255, 0, 0]
green=[0, 255, 0]
blue=[0, 0, 255]
pink=[255, 153, 255]
lGreen=[153, 255, 153]
lBlue=[153, 255, 255]

screenX=640
screenY=480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock=pygame.time.Clock()
ball=pygame.image.load("pall.xcf")
ball=pygame.transform.scale(ball,(100,100))
posX,posY=580,400
speedX=1
gameover=False 
while not gameover:
    clock.tick(60)
    events=pygame.event.get()
    for i in pygame.event.get(): 
        if i.type==pygame.QUIT:
            sys.exit()

    screen.blit(ball, (posX,posY))
    posX -=speedX 
    pygame.display.flip()
   
pygame.quit()




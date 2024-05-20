import pygame
import random
import sys
pygame.init()

r=random.randint(0, 255)
g=random.randint(0, 255)
b=random.randint(0, 255)
varv=[r,g,b]
lGreen=[153, 255, 153]

pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Juhuslikud kujundid")
pind.fill(lGreen)

for i in range (1,10):
    x=random.randint(0, 620)
    y=random.randint(0, 460)
    pygame.draw.rect(pind, varv, [x, y, 20, 20])

    pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()

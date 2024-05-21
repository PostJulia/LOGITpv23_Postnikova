import pygame
pygame.init()

green = [0, 155, 0]
blue = [0, 0, 155]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [100, 240, 255]

screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Surface")
screen.fill(lBlue)

surf = pygame.Surface((300,200))
surf.set_colorkey((0,0,0)) 

pygame.draw.circle(surf, blue, (140,100), 100)
pygame.draw.circle(surf,green, (100,160), 80)
pygame.draw.circle(surf, pink, (50,100), 60)
screen.blit(surf,(0,0))

gameover = False
while not gameover:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.display.flip()
pygame.quit()

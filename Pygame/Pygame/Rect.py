import pygame, os
pygame.init()

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Rect")
screen.fill(lBlue)

player = pygame.Rect(0,0, 120, 120)
pygame.draw.rect(screen, red, player)
playerImage = pygame.image.load("pall.xcf")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

screen.blit(playerImage, player)

gameover = False
while not gameover:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break 

    pygame.display.flip()
pygame.quit()

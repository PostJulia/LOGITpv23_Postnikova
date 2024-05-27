import pygame, random
pygame.init()

red=[255, 0, 0]
green=[0, 255, 0]
blue=[0, 0, 255]
pink=[255, 153, 255]
lGreen=[153, 255, 153]
lBlue=[153, 204, 255]

screenX=640
screenY=480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Hiir")
screen.fill(lBlue)
clock=pygame.time.Clock()

gameover=False
while not gameover:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    click=pygame.mouse.get_pos()
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    varv=[r,g,b]
    ruuduke=pygame.Rect(click[0],click[1] , 100, 100)
    pygame.draw.rect(screen, varv, ruuduke)

    pygame.display.flip()
    screen.fill(lGreen)

pygame.quit()

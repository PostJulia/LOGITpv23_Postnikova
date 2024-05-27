import pygame, random
pygame.init()

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
enemy_colors = [red, green, blue, pink, lGreen]

screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Mäng")

screen.fill(lBlue)
clock = pygame.time.Clock()

posX, posY = screenX/2, screenY/2
speedX, speedY = 0, 0

player = pygame.Rect(posX, posY, 30, 30)

enemies = []
for i in range(5):
    rect = pygame.Rect(random.randint(0, screenX - 30), random.randint(0, screenY - 30), 30, 30)
    color = random.choice(enemy_colors)
    enemies.append((rect, color))

enemyCounter = 0
totalEnemies = 20
score = 0
gameover = False

while not gameover:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speedX = 3
            elif event.key == pygame.K_LEFT:
                speedX = -3
            elif event.key == pygame.K_UP:
                speedY = -3
            elif event.key == pygame.K_DOWN:
                speedY = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                speedX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speedY = 0

    posX += speedX
    posY += speedY
    player = pygame.Rect(posX, posY, 30, 30)
    
    if posX > screenX - player.width or posX < 0:
        speedX = -speedX
    if posY > screenY - player.height or posY < 0:
        speedY = -speedY

    enemyCounter += 1
    if enemyCounter >= totalEnemies:
        enemyCounter = 0
        rect = pygame.Rect(random.randint(0, screenX - 30), random.randint(0, screenY - 30), 30, 30)
        color = random.choice(enemy_colors)
        enemies.append((rect, color))

    for enemy in enemies[:]:
        if player.colliderect(enemy[0]):
            enemies.remove(enemy)
            score += 1

    screen.fill(lBlue)
    pygame.draw.rect(screen, red, player)
    
    for enemy in enemies:
        pygame.draw.circle(screen, enemy[1], (enemy[0].x + 15, enemy[0].y + 15), 15)
    
    pygame.display.flip()
    pygame.display.set_caption("Score: " + str(score))
    print(score)
    
    #if score==1200:
    #    gameover=True

pygame.quit()

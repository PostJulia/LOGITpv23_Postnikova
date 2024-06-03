import pygame
import random

pygame.init()
scr_w, scr_h = 640, 480
cell_size = 40
cols, rows = scr_w // cell_size, scr_h // cell_size

screen = pygame.display.set_mode((scr_w, scr_h))
pygame.display.set_caption('Labürint')

pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()

lBlue = (153, 255, 255)
lPurple = (204, 153, 255)
blue = (51, 153, 255)
red = (255, 0, 0)
black = (0, 0, 0)
purple = (76, 0, 153)

plr_r = 10
plr_speed = 5

start_x, start_y = 0, rows - 1
end_x, end_y = cols - 1, 0

plr_x = start_x * cell_size + plr_r
plr_y = start_y * cell_size + plr_r

clock = pygame.time.Clock()
level = 0
max_levels = 3

font = pygame.font.SysFont(None, 36)

def create_cell(x, y):
    return {"x": x, "y": y, "walls": [True, True, True, True], "visited": False}

def draw_cell(cell, cell_size, screen, blue):
    x = cell["x"] * cell_size
    y = cell["y"] * cell_size
    if cell["walls"][0]:
        pygame.draw.line(screen, blue, (x, y), (x + cell_size, y), 2)
    if cell["walls"][1]:
        pygame.draw.line(screen, blue, (x + cell_size, y), (x + cell_size, y + cell_size), 2)
    if cell["walls"][2]:
        pygame.draw.line(screen, blue, (x + cell_size, y + cell_size), (x, y + cell_size), 2)
    if cell["walls"][3]:
        pygame.draw.line(screen, blue, (x, y + cell_size), (x, y), 2)

def create_grid():
    return [[create_cell(x, y) for x in range(cols)] for y in range(rows)]

def generate_maze():
    grid = create_grid()
    stack = []
    current_cell = grid[start_y][start_x]
    current_cell["visited"] = True

    while True:
        neighbors = []
        x, y = current_cell["x"], current_cell["y"]
        if y > 0 and not grid[y - 1][x]["visited"]:
            neighbors.append(grid[y - 1][x])
        if y < rows - 1 and not grid[y + 1][x]["visited"]:
            neighbors.append(grid[y + 1][x])
        if x > 0 and not grid[y][x - 1]["visited"]:
            neighbors.append(grid[y][x - 1])
        if x < cols - 1 and not grid[y][x + 1]["visited"]:
            neighbors.append(grid[y][x + 1])

        if neighbors:
            next_cell = random.choice(neighbors)
            stack.append(current_cell)
            if next_cell["x"] == current_cell["x"] + 1:
                current_cell["walls"][1] = False
                next_cell["walls"][3] = False
            elif next_cell["x"] == current_cell["x"] - 1:
                current_cell["walls"][3] = False
                next_cell["walls"][1] = False
            elif next_cell["y"] == current_cell["y"] + 1:
                current_cell["walls"][2] = False
                next_cell["walls"][0] = False
            elif next_cell["y"] == current_cell["y"] - 1:
                current_cell["walls"][0] = False
                next_cell["walls"][2] = False
            current_cell = next_cell
            current_cell["visited"] = True
        elif stack:
            current_cell = stack.pop()
        else:
            break
    return grid

def reset_player():
    global plr_x, plr_y
    plr_x = start_x * cell_size + plr_r
    plr_y = start_y * cell_size + plr_r

def next_level():
    global level, grid
    level += 1
    if level < max_levels:
        grid = generate_maze()
        reset_player()
    else:
        end_game()

def end_game():
    while True:
        screen.fill(lBlue)
        end_text = font.render("Sa oled kõik tasemed läbinud!", True, black)
        continue_text = font.render("Kas soovite jätkata (J) või väljuda (V)?", True, black)
        screen.blit(end_text, (scr_w // 2 - end_text.get_width() // 2, scr_h // 2 - 40))
        screen.blit(continue_text, (scr_w // 2 - continue_text.get_width() // 2, scr_h // 2 + 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    restart_game()
                    return
                elif event.key == pygame.K_v:
                    pygame.quit()
                    quit()

def restart_game():
    global level, grid
    level = 0
    grid = generate_maze()
    reset_player()

grid = generate_maze()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    new_x, new_y = plr_x, plr_y

    if keys[pygame.K_LEFT] and plr_x > plr_r:
        new_x -= plr_speed
    if keys[pygame.K_RIGHT] and plr_x < scr_w - plr_r:
        new_x += plr_speed
    if keys[pygame.K_UP] and plr_y > plr_r:
        new_y -= plr_speed
    if keys[pygame.K_DOWN] and plr_y < scr_h - plr_r:
        new_y += plr_speed

    plr_rect = pygame.Rect(new_x - plr_r, new_y - plr_r, plr_r * 2, plr_r * 2)

    collision = False
    for row in grid:
        for cell in row:
            cx, cy = cell["x"] * cell_size, cell["y"] * cell_size
            if cell["walls"][0] and plr_rect.colliderect(pygame.Rect(cx, cy, cell_size, 2)):
                collision = True
            if cell["walls"][1] and plr_rect.colliderect(pygame.Rect(cx + cell_size - 2, cy, 2, cell_size)):
                collision = True
            if cell["walls"][2] and plr_rect.colliderect(pygame.Rect(cx, cy + cell_size - 2, cell_size, 2)):
                collision = True
            if cell["walls"][3] and plr_rect.colliderect(pygame.Rect(cx, cy, 2, cell_size)):
                collision = True

    if not collision:
        plr_x, plr_y = new_x, new_y

    if (plr_x // cell_size == end_x and plr_y // cell_size == end_y):
        next_level()

    screen.fill(lBlue)
    for row in grid:
        for cell in row:
            draw_cell(cell, cell_size, screen, blue)

    pygame.draw.rect(screen, black, (start_x * cell_size, start_y * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, red, (end_x * cell_size, end_y * cell_size, cell_size, cell_size))
    pygame.draw.circle(screen, lPurple, (plr_x, plr_y), plr_r)

    level_text = font.render(f"Level: {level + 1}", True, purple)
    screen.blit(level_text, (10, 10))

    pygame.display.update()
    clock.tick(60)


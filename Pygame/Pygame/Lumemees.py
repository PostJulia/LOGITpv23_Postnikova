import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode( (300, 300))
ekraani_pind.fill( (0,0,0))
pygame.display.set_caption("Lumemees")

center_coordinates=(150, 80) 
radius=30  
pygame.draw.circle(ekraani_pind, (255, 255, 255), center_coordinates, radius)
center_coordinates=(140, 80) 
radius=5
pygame.draw.circle(ekraani_pind, (0, 0, 0), center_coordinates, radius)
center_coordinates=(160, 80) 
radius=5 
pygame.draw.circle(ekraani_pind, (0, 0, 0), center_coordinates, radius)
center_coordinates=(150, 135) 
radius=40 
pygame.draw.circle(ekraani_pind, (255, 255, 255), center_coordinates, radius)
center_coordinates=(150, 130) 
radius=5 
pygame.draw.circle(ekraani_pind, (0, 0, 0), center_coordinates, radius)
center_coordinates=(150, 145) 
radius=5 
pygame.draw.circle(ekraani_pind, (0, 0, 0), center_coordinates, radius)
center_coordinates=(150, 200) 
radius=50
pygame.draw.circle(ekraani_pind, (255, 255, 255), center_coordinates, radius)
center_coordinates=(150, 180) 
radius=5 
pygame.draw.circle(ekraani_pind, (0, 0, 0), center_coordinates, radius)
center_coordinates=(150, 200) 
radius=5 
pygame.draw.circle(ekraani_pind, (0, 0, 0), center_coordinates, radius)
center_coordinates=(150, 220) 
radius=5 
pygame.draw.circle(ekraani_pind, (0, 0, 0), center_coordinates, radius)
pygame.draw.line(ekraani_pind, (139, 69, 19), (110, 140), (60, 100), 5) 
pygame.draw.line(ekraani_pind, (139, 69, 19), (190, 140), (240, 100), 5) 

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()

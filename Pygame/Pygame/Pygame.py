import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode( (640, 480))
ekraani_pind.fill( (0,0,255))
pygame.display.set_caption("Minu esimene aken")

#1
#pygame.mixer.music.load('lazarev.mp3')
#pygame.mixer.music.play()

#2
#sounds = ['snd1.mp3', 'snd2.mp3', 'snd3.mp3', 'snd4.mp3', 'snd5.mp3']
#pygame.mixer.music.load('music/'+random.choice(sounds))
#pygame.mixer.music.play()

#3
#hit_sound = pygame.mixer.Sound('music/Hit.wav')
#pygame.mixer.Sound.play(hit_sound)


ristkylik1=pygame.Rect(0, 380, 700, 100)
pygame.draw.rect(ekraani_pind, (0,255,0), ristkylik1)

center_coordinates=(60, 70) 
radius=50  
pygame.draw.circle(ekraani_pind, (255, 255, 0), center_coordinates, radius)


pilt=pygame.image.load("Sipsik.xcf")
pilt=pygame.transform.scale(pilt,(160,160))
ekraani_pind.blit(pilt, (200, 100))

tekst="Tere, Pygame!"
meie_font=pygame.font.SysFont("Verdana", 36)
teksti_pilt=meie_font.render(tekst, False, (250,250,100))
ekraani_pind.blit(teksti_pilt, (300, 30))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
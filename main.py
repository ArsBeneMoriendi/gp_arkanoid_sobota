import pygame
from Platforma import Platforma
from Kulka import Kulka

SZEROKOSC = 1024
WYSOKOSC = 800
ekran = pygame.display.set_mode([SZEROKOSC,WYSOKOSC])
Zycia = 3

pygame.init()
pygame.font.init()

czcionka = pygame.font.SysFont('Comic Sans MS', 24)

zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('images/background.png')

platforma = Platforma()
kulka = Kulka()

gra_dziala = True

while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN: 
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT: 
            gra_dziala = False 
        
    wcisniente_klawisze = pygame.key.get_pressed()
    if wcisniente_klawisze[pygame.K_LEFT]:
        platforma.ruszaj_platforma(-1)
    if wcisniente_klawisze[pygame.K_RIGHT]:
        platforma.ruszaj_platforma(1)
    

    kulka.aktualizuj(platforma)
    platforma.aktualizuj()

    if kulka.przegrana:
        Zycia -= 1
        if Zycia <= 0:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(platforma.obraz, platforma.rect)
    ekran.blit(kulka.obraz, kulka.rect)

    tekst = czcionka.render(f'Życia: {Zycia}', False, (196, 102, 255))
    ekran.blit(tekst, (16, 16))

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()
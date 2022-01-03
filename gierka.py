import pygame
import sys
import numpy as np
pygame.init()
tab = np.zeros((3, 3))
koniec_gry = False
wyjscie_Z_menu=False
player = 1
screen=pygame.display.set_mode((450,300))
screen.fill((95,245,108))
start_icon=pygame.image.load("start-button.png")
screen.blit(start_icon,((75,0)))
tictactoe_baner = pygame.image.load("ikonka.png")


def linia():
    pygame.draw.line(screen, (6, 78, 142), (200, 600), (200, 0), 16)
    pygame.draw.line(screen, (6, 78, 142), (400, 600), (400, 0), 16)
    pygame.draw.line(screen, (6, 78, 142), (0, 400), (600, 400), 16)
    pygame.draw.line(screen, (6, 78, 142), (0, 200), (600, 200), 16)
    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 600), 8)
    screen.blit(tictactoe_baner, (685, 25))


def przyciski():
    a = 1


def rysowanie():
    for kolumna in range(3):
        for wiersz in range(3):
            if(tab[kolumna][wiersz]) == 1:
                pygame.draw.line(screen, ((0, 0, 0)), ((
                    200*kolumna+50, 200*wiersz+200-50)), ((200*kolumna+200-50, 200*wiersz+50)), 16)
                pygame.draw.line(screen, ((0, 0, 0)), ((
                    200*kolumna+50, 200*wiersz+50)), ((200*kolumna+200-50, 200*wiersz+200-50)), 16)
            elif tab[kolumna][wiersz] == 2:
                pygame.draw.circle(screen, ((0, 0, 0)),
                                   ((200*kolumna+100, 200*wiersz+100)), 65, 15)


def zaznaczanie(player, kolumna, wiersz):
    tab[kolumna][wiersz] = player


def sprawdz_wolne_miejsce(kolumna, wiersz):
    if tab[kolumna][wiersz] == 0:
        return True
    else:
        return False


def sprawdz_czy_wygral():
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] and tab[i][0] > 0 and tab[i][1] > 0 and tab[i][2] > 0:
            pygame.draw.line(screen, ((0, 0, 0)),
                             ((200*i+100, 50)), ((200*i+100, 550)), 16)
            return True
        if tab[0][i] == tab[1][i] == tab[2][i] and tab[0][i] > 0 and tab[1][i] > 0 and tab[2][i] > 0:
            pygame.draw.line(screen, ((0, 0, 0)),
                             ((50, 200*i+100)), ((550, 200*i+100)), 16)
            return True
    if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0] > 0 and tab[1][1] > 0 and tab[2][2] > 0:
        pygame.draw.line(screen, ((0, 0, 0)), ((50, 50)), ((550, 550)), 16)
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] and tab[0][2] > 0 and tab[1][1] > 0 and tab[2][0] > 0:
        pygame.draw.line(screen, ((0, 0, 0)), ((50, 550)), ((550, 50)), 16)
        return True
    return False


def czy_wszystkie_pelne():
    for i in range(3):
        for j in range(3):
            if tab[i][j] == 0:
                return False
    return True


def restart():
    screen = pygame.display.set_mode((900, 600))
    for i in range(3):
        for j in range(3):
            tab[i][j] = 0
    screen.fill((94, 160, 217))
    linia()
    player = 1

####################################-------------MAIN------------##################################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            restart()
            koniec_gry = False
        if koniec_gry == False and event.type == pygame.MOUSEBUTTONDOWN and wyjscie_Z_menu==True:
            xy = event.pos
            x = xy[0]
            y = xy[1]
            kolum = int(x//200)
            wiers = y//200
            if kolum<=2 and wiers<=2:
                if sprawdz_wolne_miejsce(kolum, wiers) == True:
                    zaznaczanie(player, kolum, wiers)
                    if sprawdz_czy_wygral():
                        koniec_gry = True
                    if czy_wszystkie_pelne():
                        koniec_gry = True
                    if player == 1:
                        player = 2
                    else:
                        player = 1
            rysowanie()
        if wyjscie_Z_menu==False and event.type==pygame.MOUSEBUTTONDOWN:
            xy=event.pos
            x = xy[0]
            y = xy[1]
            if x>20 and x<410 and y>20 and y<280:
                restart()
                wyjscie_Z_menu=True
        pygame.display.update()

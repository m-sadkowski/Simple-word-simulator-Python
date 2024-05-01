import pygame
from pygame import font

from Punkt import Punkt
from Swiat import Swiat

# PyGame initialization
pygame.init()

# Screen initialization
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
ENTITY_SIZE = 32
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# Title and icon
pygame.display.set_caption("Symulator świata")
icon = pygame.image.load('Assets/czlowiek.jpg')
pygame.display.set_icon(icon)

# Images
czlowiekImg = pygame.image.load('Assets/czlowiek.jpg')
czlowiekImg = pygame.transform.scale(czlowiekImg, (ENTITY_SIZE, ENTITY_SIZE))
antylopaImg = pygame.image.load('Assets/antylopa.jpg')
antylopaImg = pygame.transform.scale(antylopaImg, (ENTITY_SIZE, ENTITY_SIZE))
barszczImg = pygame.image.load('Assets/barszcz.jpg')
barszczImg = pygame.transform.scale(barszczImg, (ENTITY_SIZE, ENTITY_SIZE))
cyberowcaImg = pygame.image.load('Assets/cyberowca.jpg')
cyberowcaImg = pygame.transform.scale(cyberowcaImg, (ENTITY_SIZE, ENTITY_SIZE))
guaranaImg = pygame.image.load('Assets/guarana.jpg')
guaranaImg = pygame.transform.scale(guaranaImg, (ENTITY_SIZE, ENTITY_SIZE))
lisImg = pygame.image.load('Assets/lis.jpg')
lisImg = pygame.transform.scale(lisImg, (ENTITY_SIZE, ENTITY_SIZE))
mleczImg = pygame.image.load('Assets/mlecz.jpg')
mleczImg = pygame.transform.scale(mleczImg, (ENTITY_SIZE, ENTITY_SIZE))
owcaImg = pygame.image.load('Assets/owca.jpg')
owcaImg = pygame.transform.scale(owcaImg, (ENTITY_SIZE, ENTITY_SIZE))
trawaImg = pygame.image.load('Assets/trawa.jpg')
trawaImg = pygame.transform.scale(trawaImg, (ENTITY_SIZE, ENTITY_SIZE))
jagodyImg = pygame.image.load('Assets/jagody.jpg')
jagodyImg = pygame.transform.scale(jagodyImg, (ENTITY_SIZE, ENTITY_SIZE))
wilkImg = pygame.image.load('Assets/wilk.jpg')
wilkImg = pygame.transform.scale(wilkImg, (ENTITY_SIZE, ENTITY_SIZE))
zolwImg = pygame.image.load('Assets/zolw.jpg')
zolwImg = pygame.transform.scale(zolwImg, (ENTITY_SIZE, ENTITY_SIZE))
ziemiaImg = pygame.image.load('Assets/grass.jpg')
ziemiaImg = pygame.transform.scale(ziemiaImg, (ENTITY_SIZE, ENTITY_SIZE))

base_y = SCREEN_HEIGHT - 5 * ENTITY_SIZE

def rysujSwiat(swiat):
    MARGIN = (SCREEN_WIDTH - swiat.getSzerokosc() * ENTITY_SIZE) // 2
    for i, komunikat in enumerate(reversed(swiat.komunikaty)):
        display_y = base_y + i * ENTITY_SIZE
        display_text(komunikat, SCREEN_WIDTH / 2, display_y, (255, 255, 255))
        print(komunikat)
    for i in range(swiat.getWysokosc()):
        for j in range(swiat.getSzerokosc()):
            organizm = swiat.getOrganizm(i, j)
            x = MARGIN + j * ENTITY_SIZE
            y = ENTITY_SIZE + i * ENTITY_SIZE
            if organizm:
                if organizm.getSymbol() == 'C':
                    screen.blit(czlowiekImg, (x, y))
                elif organizm.getSymbol() == 'A':
                    screen.blit(antylopaImg, (x, y))
                elif organizm.getSymbol() == 'b':
                    screen.blit(barszczImg, (x, y))
                elif organizm.getSymbol() == 'X':
                    screen.blit(cyberowcaImg, (x, y))
                elif organizm.getSymbol() == 'g':
                    screen.blit(guaranaImg, (x, y))
                elif organizm.getSymbol() == 'L':
                    screen.blit(lisImg, (x, y))
                elif organizm.getSymbol() == 'm':
                    screen.blit(mleczImg, (x, y))
                elif organizm.getSymbol() == 'O':
                    screen.blit(owcaImg, (x, y))
                elif organizm.getSymbol() == 't':
                    screen.blit(trawaImg, (x, y))
                elif organizm.getSymbol() == 'W':
                    screen.blit(wilkImg, (x, y))
                elif organizm.getSymbol() == 'Z':
                    screen.blit(zolwImg, (x, y))
                elif organizm.getSymbol() == 'w':
                    screen.blit(jagodyImg, (x, y))
            else:
                screen.blit(ziemiaImg, (x, y))

    pygame.display.update()


strzalka = -1

font = pygame.font.SysFont(None, 36)


def display_text(text, x, y, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def rysujPrzyciski():
    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH / 2 - ENTITY_SIZE * 8 / 2 - 4,
                                               SCREEN_HEIGHT / 2 - ENTITY_SIZE * 4 - 4,
                                               ENTITY_SIZE * 8 + 8, ENTITY_SIZE * 2 + 8))
    pygame.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH / 2 - ENTITY_SIZE * 8 / 2,
                                         SCREEN_HEIGHT / 2 - ENTITY_SIZE * 4,
                                         ENTITY_SIZE * 8, ENTITY_SIZE * 2))
    display_text("Nowa gra", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - ENTITY_SIZE * 3)
    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH / 2 - ENTITY_SIZE * 8 / 2 - 4,
                                               SCREEN_HEIGHT / 2 - 4,
                                               ENTITY_SIZE * 8 + 8, ENTITY_SIZE * 2 + 8))
    pygame.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH / 2 - ENTITY_SIZE * 8 / 2,
                                         SCREEN_HEIGHT / 2,
                                         ENTITY_SIZE * 8, ENTITY_SIZE * 2))
    display_text("Wczytaj gre", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + ENTITY_SIZE)


def nowaGra():
    para = wczytajRozmiar()
    swiat = Swiat(para.x, para.y)
    swiat.generujSwiat()
    return swiat


def wczytajGre():
    print("Wczytana gra.")
    swiat.generujSwiat()
    return swiat

def wczytajRozmiar():
    input_text = ''
    m = 0
    n = 0
    liczba1 = True
    while liczba1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                liczba1 = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    m = int(input_text)
                    input_text = ''
                    liczba1 = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill((0,0,0))
        display_text("Podaj wysokość (i wciśnij Enter):  " + input_text, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, (255,255,255))
        pygame.display.flip()

    liczba2 = True
    input_text = ''
    while liczba2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                liczba2 = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    n = int(input_text)
                    liczba2 = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill((0, 0, 0))
        display_text("Podaj szerokość (i wciśnij Enter):  " + input_text, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, (255,255,255))
        pygame.display.flip()

    screen.fill((0, 0, 0))
    return Punkt(m, n)



if __name__ == '__main__':

    welcome = True
    while welcome:

        screen.fill((0, 0, 0))
        rysujPrzyciski()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                welcome = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SCREEN_WIDTH / 2 - ENTITY_SIZE * 8 / 2 < event.pos[0] < SCREEN_WIDTH / 2 + ENTITY_SIZE * 4 \
                        and SCREEN_HEIGHT / 2 - ENTITY_SIZE * 4 < event.pos[
                    1] < SCREEN_HEIGHT / 2 - ENTITY_SIZE * 4 + ENTITY_SIZE * 2:
                    swiat = nowaGra()
                    rysujSwiat(swiat)
                    welcome = False
                if SCREEN_WIDTH / 2 - ENTITY_SIZE * 8 / 2 < event.pos[0] < SCREEN_WIDTH / 2 + ENTITY_SIZE * 4 \
                        and SCREEN_HEIGHT / 2 < event.pos[1] < SCREEN_HEIGHT / 2 + ENTITY_SIZE * 2:
                    wczytajGre()
                    swiat = wczytajGre()
                    welcome = False

        pygame.display.update()

    running = True
    while running:

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    strzalka = 0
                if event.key == pygame.K_DOWN:
                    strzalka = 1
                if event.key == pygame.K_LEFT:
                    strzalka = 2
                if event.key == pygame.K_RIGHT:
                    strzalka = 3
                if event.key == pygame.K_RIGHT:
                    strzalka = 3
                if event.key == pygame.K_LCTRL:
                    strzalka = 4

        if not strzalka == -1:
            swiat.wykonajTure(strzalka)
            rysujSwiat(swiat)

        strzalka = -1

pygame.quit()
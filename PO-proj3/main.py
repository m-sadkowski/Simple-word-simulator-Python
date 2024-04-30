import pygame

from Swiat import Swiat

# PyGame initialization
pygame.init()

# Screen initialization
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
ENTITY_SIZE = 32
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

def rysujSwiat(swiat, MARGIN):
    for komunikat in reversed(swiat.komunikaty):
        print(komunikat)
    for i in range(m):
        for j in range(n):
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

if __name__ == '__main__':

    m = int(input())
    n = int(input())
    swiat = Swiat(m, n)
    MARGIN = (SCREEN_WIDTH - m * ENTITY_SIZE) // 2
    swiat.generujSwiat()
    rysujSwiat(swiat, MARGIN)

    running = True
    while running:

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  # zmiana
                if event.key == pygame.K_UP:  # zmiana
                    strzalka = 0
                if event.key == pygame.K_DOWN:  # zmiana
                    strzalka = 1
                if event.key == pygame.K_LEFT:  # zmiana
                    strzalka = 2
                if event.key == pygame.K_RIGHT:  # zmiana
                    strzalka = 3
                if event.key == pygame.K_RIGHT:  # zmiana
                    strzalka = 3
                if event.key == pygame.K_LCTRL:  # zmiana
                    strzalka = 4

        swiat.wykonajTure(strzalka)
        if not strzalka == -1:
            rysujSwiat(swiat, MARGIN)

        strzalka = -1

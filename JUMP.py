import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (203, 100, 103)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('JUMP')

clock = pygame.time.Clock()

# upload de imagens
playImg = pygame.image.load('play.png')
playSelectedImg = pygame.image.load('playSelected.png')
soundOnImg = pygame.image.load('soundOn.png')
soundOnSelectedImg = pygame.image.load('soundOffSelected.png')
soundOffImg = pygame.image.load('soundOn.png')
soundOffSelectedImg = pygame.image.load('soundOffSelected.png')
exitImg = pygame.image.load('exit.png')
exitSelectedImg = pygame.image.load('exitSelected.png')
creditsImg = pygame.image.load('credits.png')
creditsSelectedImg = pygame.image.load('creditsSelected.png')
helpImg = pygame.image.load('help.png')
helpSelectedImg = pygame.image.load('helpSelected.png')
barMenuImg = pygame.image.load('barraMenu.png')

# definicao variaveis para localizacao dos botoes

def play1Button(px, py):
    gameDisplay.blit(playImg, (px, py))
def play2Button(px, py):
    gameDisplay.blit(playSelectedImg, (px, py))

px = (display_width / 2.3)
py = (display_height / 2.3)

def sound1Button(sx, sy):
    gameDisplay.blit(soundOnImg, (sx, sy))
def sound2Button(sx, sy):
    gameDisplay.blit(soundOnSelectedImg, (sx, sy))
def sound3Button(sx, sy):
    gameDisplay.blit(soundOffImg, (sx, sy))
def sound4Button(sx, sy):
    gameDisplay.blit(soundOffSelectedImg, (sx, sy))

sx = (display_width / 9)
sy = (display_height / 2.3)

def exit1Button(ex, ey):
    gameDisplay.blit(exitImg, (ex, ey))
def exit2Button(ex, ey):
    gameDisplay.blit(exitSelectedImg, (ex, ey))

ex = (display_width / 1.35)
ey = (display_height / 2.3)

def credits1Button(cx, cy):
    gameDisplay.blit(creditsImg, (cx, cy))
def credits2Button(cx, cy):
    gameDisplay.blit(creditsSelectedImg, (cx, cy))
cx = (display_width / 1.7)
cy = (display_height / 2.3)

def help1Button(hx, hy):
    gameDisplay.blit(helpImg, (hx, hy))
def help2Button(hx, hy):
        gameDisplay.blit(helpSelectedImg, (hx, hy))
hx = (display_width / 3.7)
hy = (display_height / 2.3)

def barraMenuUp(bx, by):
    gameDisplay.blit(barMenuImg, (bx, by))
bx = (display_width / 9)
by = (display_height / 3.3)

def barraMenuDown(b2x, b2y):
    gameDisplay.blit(barMenuImg, (b2x, b2y))
b2x = (display_width / 9)
b2y = (display_height / 1.4)

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(red)
    play1Button(px, py)
    sound1Button(sx, sy)
    exit1Button(ex, ey)
    credits1Button(cx, cy)
    help1Button(hx, hy)
    barraMenuDown(b2x, b2y)
    barraMenuUp(bx, by)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

quit()
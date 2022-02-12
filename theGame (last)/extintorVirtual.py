# Um jogo para os bombeiros!

import sys
import pygame
import gameSprites

screenWidth, screenHeight = 800, 600

fire1, fire2, smoke, material, background, logo, prevButton, faseButton = gameSprites.loadSprites()
fireCount = 0
smokeCount = 0
smokeOn = False
fireOn = True

pygame.init()
screen = pygame.display.set_mode(size = (screenWidth,screenHeight))
pygame.display.set_caption('Extintor Virtual')
clock = pygame.time.Clock()

logo = pygame.transform.scale(logo, (int(screenWidth*3/8), int(screenHeight*0.5)))
prevButton = pygame.transform.scale(prevButton, (int(screenHeight*0.15),int(screenHeight*0.15)))

material[0] = pygame.transform.scale(material[0], (int(screenHeight*0.4), int(screenHeight*0.2)))
material[1] = pygame.transform.scale(material[1], (int(screenHeight*0.45), int(screenHeight*0.65)))
material[2] = pygame.transform.scale(material[2], (int(screenHeight*0.22), int(screenHeight*0.3)))
material[3] = pygame.transform.scale(material[3], (int(screenHeight*0.7), int(screenHeight*0.4)))
material[4] = pygame.transform.scale(material[4], (int(screenHeight*0.4), int(screenHeight*0.5)))
material[5] = pygame.transform.scale(material[5], (int(screenHeight*0.3), int(screenHeight*0.2)))
material[6] = pygame.transform.scale(material[6], (int(screenHeight*0.2), int(screenHeight*0.3)))
material[7] = pygame.transform.scale(material[7], (int(screenHeight*0.7), int(screenHeight*0.4)))
material[8] = pygame.transform.scale(material[8], (int(screenHeight*0.8), int(screenHeight*0.4)))

for i in range(len(faseButton)):
    faseButton[i] = pygame.transform.scale(faseButton[i], (int(screenWidth/5), int(screenHeight/8)))
for i in range(len(fire1)):
    fire1[i] = pygame.transform.scale(fire1[i], (int(screenHeight*0.85), int(screenHeight*0.85)))
for i in range(len(fire2)):
    fire2[i] = pygame.transform.scale(fire2[i], (int(screenHeight*0.3), int(screenHeight*0.3)))

def run_game():

    global fase
    global smokeOn
    global fireOn
    fase = 0

    while True:
        clock.tick(12)

        if(fase == 0):
            redrawGameWindow()
        elif(fase == 1):
            drawFase1()
        elif(fase == 2):
            drawFase2()
        elif(fase == 3):
            drawFase3()
        elif(fase == 4):
            drawFase4()
        elif(fase == 5):
            drawFase5()
        elif(fase == 6):
            drawFase6()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if(screenWidth*0.8 <= mouse[0] <= (screenWidth*0.7 + screenHeight*0.9) and screenHeight*0.75 <= mouse[1] <= screenHeight*0.9 and fase != 0):
                    fase = 0
                elif(screenWidth*0.5 <= mouse[0] <= screenWidth*0.7 and screenHeight*0.1875 <= mouse[1] <= screenHeight*0.3125 and fase == 0):
                    fase = 1
                    fireOn = True
                elif(screenWidth*0.75 <= mouse[0] <= screenWidth*0.95 and screenHeight*0.1875 <= mouse[1] <= screenHeight*0.3125 and fase == 0):
                    fase = 2
                    fireOn = True
                elif(screenWidth*0.5 <= mouse[0] <= screenWidth*0.7 and screenHeight*0.4375 <= mouse[1] <= screenHeight*0.5625 and fase == 0):
                    fase = 3
                    fireOn = True
                elif(screenWidth*0.75 <= mouse[0] <= screenWidth*0.95 and screenHeight*0.4375 <= mouse[1] <= screenHeight*0.5625 and fase == 0):
                    fase = 4
                    fireOn = True
                elif(screenWidth*0.5 <= mouse[0] <= screenWidth*0.7 and screenHeight*0.6875 <= mouse[1] <= screenHeight*0.8125 and fase == 0):
                    fase = 5
                    fireOn = True
                elif(screenWidth*0.75 <= mouse[0] <= screenWidth*0.95 and screenHeight*0.6875 <= mouse[1] <= screenHeight*0.8125 and fase == 0):
                    fase = 6
                    fireOn = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    smokeOn = True
            elif event.type == pygame.QUIT:
                sys.exit()

def redrawGameWindow():

    screen.blit(background, (0,0))
    screen.blit(logo, (int(screenWidth/16),int(screenHeight/4)))
    screen.blit(faseButton[0], (int(screenWidth*0.5),int(screenHeight*0.1875)))
    screen.blit(faseButton[1], (int(screenWidth*0.75),int(screenHeight*0.1875)))
    screen.blit(faseButton[2], (int(screenWidth*0.5),int(screenHeight*0.4375)))
    screen.blit(faseButton[3], (int(screenWidth*0.75),int(screenHeight*0.4375)))
    screen.blit(faseButton[4], (int(screenWidth*0.5),int(screenHeight*0.6875)))
    screen.blit(faseButton[5], (int(screenWidth*0.75),int(screenHeight*0.6875)))

    pygame.display.update()

def drawFase1():
    global fireCount
    global fireOn

    screen.blit(background, (0,0))
    screen.blit(prevButton, (int(screenWidth*0.8),int(screenHeight*0.75)))
    screen.blit(material[0], (screenWidth*0.3625,screenHeight*0.65))

    if fireOn == True:
        if fireCount == 6:
            fireCount = 0
        screen.blit(fire1[fireCount], (screenWidth*0.2,screenHeight*0.08))
        fireCount += 1

    if(smokeOn == True):
        drawSmoke()

    pygame.display.update()

def drawFase2():
    global fireCount
    global fireOn

    screen.blit(background, (0,0))
    screen.blit(prevButton, (int(screenWidth*0.8),int(screenHeight*0.75)))
    screen.blit(material[1], (screenWidth*0.32,screenHeight*0.175))

    if fireOn == True:
        if fireCount == 6:
            fireCount = 0
        screen.blit(fire2[fireCount], (screenWidth*0.53,screenHeight*0.46))
        fireCount += 1

    if(smokeOn == True):
        drawSmoke()

    pygame.display.update()

def drawFase3():
    global fireCount
    global fireOn

    screen.blit(background, (0,0))
    screen.blit(prevButton, (int(screenWidth*0.8),int(screenHeight*0.75)))
    screen.blit(material[2], (screenWidth*0.7,screenHeight*0.1))
    screen.blit(material[3], (screenWidth*0.22,screenHeight*0.4))

    if fireOn == True:
        if fireCount == 6:
            fireCount = 0
        screen.blit(fire1[fireCount], (screenWidth*0.16,screenHeight*0.04))
        fireCount += 1

    if(smokeOn == True):
        drawSmoke()

    pygame.display.update()

def drawFase4():
    global fireCount
    global fireOn

    screen.blit(background, (0,0))
    screen.blit(prevButton, (int(screenWidth*0.8),int(screenHeight*0.75)))
    screen.blit(material[5], (screenWidth*0.38,screenHeight*0.2))
    screen.blit(material[4], (screenWidth*0.35,screenHeight*0.3))

    if fireOn == True:
        if fireCount == 6:
            fireCount = 0
        screen.blit(fire2[fireCount], (screenWidth*0.38,screenHeight*0.08))
        fireCount += 1

    if(smokeOn == True):
        drawSmoke()

    pygame.display.update()

def drawFase5():
    global fireCount
    global fireOn

    screen.blit(background, (0,0))
    screen.blit(prevButton, (int(screenWidth*0.8),int(screenHeight*0.75)))
    screen.blit(material[6], (screenWidth*0.7,screenHeight*0.1))
    screen.blit(material[7], (screenWidth*0.22,screenHeight*0.4))

    if fireOn == True:
        if fireCount == 6:
            fireCount = 0
        screen.blit(fire1[fireCount], (screenWidth*0.16,screenHeight*0.04))
        fireCount += 1

    if(smokeOn == True):
        drawSmoke()

    pygame.display.update()

def drawFase6():
    global fireCount
    global fireOn

    screen.blit(background, (0,0))
    screen.blit(prevButton, (int(screenWidth*0.8),int(screenHeight*0.75)))
    screen.blit(material[8], (screenWidth*0.2,screenHeight*0.4))

    if fireOn == True:
        if fireCount == 6:
            fireCount = 0
        screen.blit(fire2[fireCount], (screenWidth*0.6,screenHeight*0.35))
        fireCount += 1

    if(smokeOn == True):
        drawSmoke()

    pygame.display.update()

def drawSmoke():
    global smokeCount
    global smokeOn
    global fireOn

    if smokeCount == 10:
        smokeCount = 0
        smokeOn = False
        fireOn = False

    screen.blit(smoke[smokeCount], (screenWidth*0.2,screenHeight*0.12))
    smokeCount += 1

run_game()
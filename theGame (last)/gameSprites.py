import sys
import pygame

def loadSprites():
    fire1 = [pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire1_01.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire1_02.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire1_03.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire1_04.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire1_05.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire1_06.png')]

    fire2 = [pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire2_01.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire2_02.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire2_03.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire2_04.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire2_05.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\fire2_06.png')]

    smoke = [pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\smoke_01.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\smoke_02.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\smoke_03.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\smoke_04.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\smoke_05.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\smoke_06.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\smoke_07.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\smoke_08.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\smoke_09.png'),
            pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\general\\smoke_10.png')]

    material = [pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\level1\\wood.png'),
                pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\level2\\geladeira.png'),
                pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\level3\\oil.png'),
                pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\level3\\spill.png'),
                pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\level4\\lixeira.png'),
                pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\level4\\papel.png'),
                pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\level5\\alcohol_bottle.png'),
                pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\level5\\spill.png'),
                pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\level6\\car.png')]

    logo = pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\mainScreen\\logo.png')

    prevButton = pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\mainScreen\\prev.png')

    faseButton = [pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\mainScreen\\fase1.png'),
                  pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\mainScreen\\fase2.png'),
                  pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\mainScreen\\fase3.png'),
                  pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\mainScreen\\fase4.png'),
                  pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\mainScreen\\fase5.png'),
                  pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\mainScreen\\fase6.png')]

    background = pygame.image.load('C:\\Users\\Tiago Feu\\Desktop\\theGame\\assets\\levels\\mainScreen\\background.png')

    return fire1, fire2, smoke, material, background, logo, prevButton, faseButton
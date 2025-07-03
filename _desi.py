import sys, random
import pygame, time
import cv2
import numpy as np
image = cv2.imread(r"C:\python\kirby\h.png")
cv2.imwrite("buki.png", image)
from pygame.locals import *
pygame.init()
pygame.mixer.init()


import _func
import _value

font = pygame.font.SysFont("hg正楷書体pro", 30)

def step8():
        pygame.display.update()
        _value.screen.fill((200,200,255))
        if _value.wazatype[_value.ka3]==0:
            _func.settingkirby(100,298)
            
        # if _value.wazatype[_value.ka3]==1:
        # if _value.wazatype[_value.ka3]==2:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
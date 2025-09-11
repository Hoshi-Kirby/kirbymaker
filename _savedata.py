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

def savedata():
    pygame.display.update()
    _value.screen.fill((200,200,255))
    mouseX, mouseY = pygame.mouse.get_pos()
    text = _value.font.render("どこにセーブしますか", False, (0,0,0))
    text_rect = text.get_rect(center=(400, 70))
    _value.screen.blit(text, text_rect)
    ka9=-1
    for i in range(2):
        for ii in range(3):
            if 80+i*350<mouseX<80+i*350+300 and 130+ii*150<mouseY<130+ii*150+100:
                pygame.draw.rect(_value.screen,(220,220,230),(80+i*350,130+ii*150,300,100),border_radius=5)
                ka9=i*3+ii
            else:
                pygame.draw.rect(_value.screen,(255,255,255),(80+i*350,130+ii*150,300,100),border_radius=5)
            text = _value.font.render(str(i*3+ii+1), False, (0,0,0))
            text_rect = text.get_rect(center=(80+i*350+20,130+ii*150+20))
            _value.screen.blit(text, text_rect)
            text = _value.font.render(_value.nameload[i*3+ii], False, (0,0,0))
            text_rect = text.get_rect(center=(80+i*350+150,130+ii*150+50))
            _value.screen.blit(text, text_rect)
            if _value.nameload[i*3+ii]!="データなし":
                _func.loadkirby(80+i*350+20,130+ii*150+50,_value.bukiload[i*3+ii],_value.bosiload[i*3+ii],i*3+ii)
    _value.ka9=ka9

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and ka9>=0:
                _value.savestep=1
                _value.se_enter1.play()
            else:
                _value.se_bubu.play()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                _value.savestep=-1
                _value.step=_value.stepbefore
                _value.se_esc.play()
    
    time.sleep(0.01)
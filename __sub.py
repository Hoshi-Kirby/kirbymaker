import sys, random
import pygame, time
import cv2
import numpy as np
from pygame.locals import *
pygame.init()
pygame.mixer.init()


import _func
import _value
import _title
import _appe
import _skill
import _deta
import _orbit
import _reco
import _test
import _desi
import _savedata
import _name
import _save
import _load

pygame.display.set_caption("k")

while True:
    pygame.display.update()
    _value.screen.fill((200,200,255))
    text_rect = pygame.Rect(100, 80, 600, 440)
    _func.draw_text_wrapped(_value.screen, "とんでとんでとんでとんでとんlううーーーーー", _value.font, (0, 0, 0), text_rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
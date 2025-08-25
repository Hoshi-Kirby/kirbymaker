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

_value.step=10
while True:

    if _value.step==10:
        _value.loadstep=0
        _name.nameload()
    while _value.step==10:
        while _value.loadstep==0:
            _load.loaddata()
        while _value.loadstep==1:
            1
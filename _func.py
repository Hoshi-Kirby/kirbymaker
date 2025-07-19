import sys, random
import pygame, time
import cv2
import numpy as np
import _value

def bgr_to_rgb(color_bgr):
    b, g, r = color_bgr
    return (r, g, b)
def settingkirby(x,y,st):
    if _value.ka8_2[_value.ka3]==0 or st==0 :
        if _value.buki==0:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマル1.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x,y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマル1ボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマル1ファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-5, y))
        if _value.buki==1:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマル2.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.55)
                _value.screen.blit(img1, (x-2.3, y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマル2ボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマル2ファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-5, y))
                
            img2 = pygame.image.load("buki.png")
            img2 = pygame.transform.scale_by(img2, 1.8)
            img2.set_colorkey((255, 255, 255))
            img2 = img2.convert_alpha()
            _value.screen.blit(img2, (x-25, y-38))
    elif 0<st<=4:
        img1 = pygame.image.load(f"{_value.ka8_2[_value.ka3]}_{st}.png")
        img1.set_colorkey((255, 255, 255))
        img1 = img1.convert_alpha()
        img1 = pygame.transform.scale_by(img1, 2.5)
        _value.screen.blit(img1, (x,y))
        if _value.buki==1:
            img2 = pygame.image.load("buki.png")
            img2 = pygame.transform.scale_by(img2, 1.8)
            img2.set_colorkey((255, 255, 255))
            img2 = img2.convert_alpha()
            _value.screen.blit(img2, (x-25, y-38))

def skill(a):
    _value.t=0
    _value.t2=0
    _value.ws=0
    _value.ad=0
    _value.kx=_value.kx0[a]*50+_value.kxtest
    _value.ky=_value.ky0[a]*50+_value.kytest
    _value.kxv=_value.kx1[a]
    _value.kyv=_value.ky1[a]
    _value.skillnum=a
    if _value.wazatype[a]==2:
        _value.kxtest+=(-1)*_value.flip*_value.kx0[a]
        _value.kytest+=_value.ky0[a]

def skillkirby(x,y,st):
    if _value.ka8_2[_value.skillnum]==0 or st==0 :
        if _value.buki==0:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマル1.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x,y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマル1ボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマル1ファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-5, y))
        if _value.buki==1:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマル2.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-2.3, y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマル2ボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマル2ファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-5, y))
    elif 0<st<=4:
        img1 = pygame.image.load(f"{_value.ka8_2[_value.skillnum]}_{st}.png")
        img1.set_colorkey((255, 255, 255))
        img1 = img1.convert_alpha()
        img1 = pygame.transform.scale_by(img1, 2)
        if _value.flip==1:
            img1=pygame.transform.flip(img1, True, False)
        _value.screen.blit(img1, (x,y))
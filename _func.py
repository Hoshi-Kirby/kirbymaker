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
                img1 = pygame.image.load("ノーマルf.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x,y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルfボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルfファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-5, y))
        if _value.buki==1:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルh.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.55)
                _value.screen.blit(img1, (x-2.3, y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルhボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルhファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-5, y))
    elif 0<st<=4:
        img1 = pygame.image.load(f"{_value.ka8_2[_value.ka3]}_{st}.png")
        img1.set_colorkey((255, 255, 255))
        img1 = img1.convert_alpha()
        img1 = pygame.transform.scale_by(img1, 2.5)
        _value.screen.blit(img1, (x,y))
    if _value.erabuki[_value.ka3]==1:
        img2 = pygame.image.load(f"buki ({_value.ka3}).png")
        img2 = pygame.transform.scale_by(img2, 2.5)
        img2.set_colorkey((255, 255, 255))
        img2 = img2.convert_alpha()
        _value.screen.blit(img2, (x+_value.bukix[_value.ka3], y+_value.bukiy[_value.ka3]))

def standingkirby(x,y,st):
    if _value.ka8_2[_value.ka3]==0 or st==0 :
        if _value.buki==0:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルf.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x,y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルfボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルfファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-5, y))
        if _value.buki==1:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルh.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.55)
                _value.screen.blit(img1, (x-2.3, y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルhボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルhファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-5, y))
                
            img2 = pygame.image.load("buki.png")
            img2 = pygame.transform.scale_by(img2, 2.5)
            img2.set_colorkey((255, 255, 255))
            img2 = img2.convert_alpha()
            _value.screen.blit(img2, (x-34.7, y-52.8))
    elif 0<st<=4:
        img1 = pygame.image.load(f"{_value.ka8_2[_value.ka3]}_{st}.png")
        img1.set_colorkey((255, 255, 255))
        img1 = img1.convert_alpha()
        img1 = pygame.transform.scale_by(img1, 2.5)
        _value.screen.blit(img1, (x,y))
        if _value.buki==1:
            img2 = pygame.image.load("buki.png")
            img2 = pygame.transform.scale_by(img2, 2.5)
            img2.set_colorkey((255, 255, 255))
            img2 = img2.convert_alpha()
            _value.screen.blit(img2, (x-34.7, y-52.8))

def skill(a):
    _value.t=0
    _value.t2=0
    _value.ws=0
    _value.ad=0
    _value.kx=(-2)*(_value.flip-0.5)*_value.kx0[a]*50+_value.kxtest
    _value.ky=(-2)*(_value.flip-0.5)*_value.ky0[a]*50+_value.kytest
    _value.kxv=_value.kx1[a]
    _value.kyv=_value.ky1[a]
    _value.skillnum=a
    if _value.wazatype[a]==2:
        _value.kxtest+=(-2)*(_value.flip-0.5)*_value.kx0[a]*50
        _value.kytest+=_value.ky0[a]*50

def skillkirby(x,y,st):
    if _value.ka8_2[_value.skillnum]==0 or st==0 :
        if _value.buki==0:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルf.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x,y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルfボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルfファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-5, y))
        if _value.buki==1:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルh.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-2.3, y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルhボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルhファイター.png")
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
import sys, random
import pygame, time
import cv2
import numpy as np
import _value

def bgr_to_rgb(color_bgr):
    b, g, r = color_bgr
    return (r, g, b)
def settingkirby(x,y):
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
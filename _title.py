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

def step1():
        pygame.display.update()
        
        _value.screen.fill((200,200,255))

        
        text = font.render("コピーメーカー", False, (0,0,0))
        text_rect = text.get_rect(center=(400, 180))
        _value.screen.blit(text, text_rect)
        text = font.render("新規作成", False, (0,0,0))
        text_rect = text.get_rect(center=(700, 30))
        _value.screen.blit(text, text_rect)

        
        if _value.ky==_value.ground: _value.hob=0
        # 終了イベントを確認 --- (*5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN: 
                if _value.kaih==0:
                    if event.key == K_RETURN:
                        if _value.ky<_value.ground:
                            _value.hob=1
                            _value.hobc=18
                            _value.kyv=-5
                        else:
                            if _value.shagam==1:
                                if _value.sura==0:
                                    _value.sura=30
                            else:
                                _value.kyv=-17
                        if 620<_value.kx<730 and -10<_value.ky<40:
                            _value.step=2
                    if event.key == K_a and _value.skaih==0 and _value.kaih==0 and _value.sura==0:
                        _value.flip=1
                        if _value.guard==1:
                            _value.kaih=30
                    if event.key == K_d and _value.skaih==0 and _value.kaih==0 and _value.sura==0:
                        _value.flip=0
                        if _value.guard==1:
                            _value.kaih=30
                    if event.key == K_s:
                        if _value.guard==1 and _value.skaih==0 and _value.kaih==0 and _value.sura==0:
                            _value.skaih=30
                    if event.key == K_q:
                        if _value.ky<_value.ground and _value.hob==0 and _value.skaih==0 and _value.sura==0:
                            _value.skaih=20
            #
        pressed_keys = pygame.key.get_pressed()
        if _value.kaih==0 and _value.skaih==0 and _value.sura==0:
            if (pressed_keys[K_d] or pressed_keys[K_a]) and _value.guard==0:
                _value.posetime+=1
                if _value.posetime==6:
                    _value.posetime=0
                    _value.pose+=1
                    if _value.pose==9:
                        _value.pose=1
                if pressed_keys[K_d]:
                    if _value.hob==1:
                        _value.kx+=1
                    else:
                        _value.kx+=4
                    if _value.kx>750:
                        _value.kx=750
                if pressed_keys[K_a]:
                    if _value.hob==1:
                        _value.kx-=1
                    else:
                        _value.kx-=4
                    if _value.kx<0:
                        _value.kx=0
            else:
                _value.pose=0

            if pressed_keys[K_RSHIFT] and _value.hobc==0:
                if _value.hob==1:
                    _value.hob=0
                    _value.kyv=-6
            
            if pressed_keys[K_q] and _value.ky==_value.ground:
                _value.guard=1
            else:
                _value.guard=0

            if pressed_keys[K_s] and _value.ky==_value.ground and _value.guard==0:
                _value.shagam=1
            else:
                _value.shagam=0

        if _value.kaih>0 and _value.ky==_value.ground:
            if _value.flip==1:
                _value.kx-=_value.kaih/3
                if _value.kx<0:
                    _value.kx=0
            else:
                _value.kx+=_value.kaih/3    
                if _value.kx>750:
                    _value.kx=750
        if _value.sura>0 and _value.ky==_value.ground:
            if _value.flip==1:
                _value.kx-=_value.sura/3
                if _value.kx<0:
                    _value.kx=0
            else:
                _value.kx+=_value.sura/3    
                if _value.kx>750:
                    _value.kx=750

        
        if _value.ky>=_value.ground and _value.kyv>=0:
            _value.kyv=0
        else:     
            if _value.hob==1:
                _value.kyv+=0.2
                if _value.kyv>1.6:_value.kyv=1.6
            else:
                _value.kyv+=1
        _value.ky+=_value.kyv
        if _value.ky>_value.ground:
            _value.ky=_value.ground
        if _value.hobc>0:
            _value.hobc-=1
        else:
            _value.hobc=0
        if _value.kaih>0:
            _value.kaih-=1
        else:
            _value.kaih=0
        if _value.skaih>0:
            _value.skaih-=1
            _value.kyv=-1
        else:
            _value.skaih=0
        if _value.sura>0:
            _value.sura-=1
            _value.kyv=-1
        else:
            _value.sura=0

        _value.kxh=0
        _value.kyh=0
        if _value.pose==0:
            img1 = pygame.image.load("ノーマルf.png")
        if _value.shagam==1:
            img1 = pygame.image.load("しゃがみf.png").convert_alpha()
            _value.kxh=-8
            _value.kyh=22

        if _value.pose==1:
            img1 = pygame.image.load("ダッシュ1.png")
            _value.kxh=0
            _value.kyh=0
        if _value.pose==2:
            img1 = pygame.image.load("ダッシュ2.png")
            _value.kxh=0
            _value.kyh=0
        if _value.pose==3:
            img1 = pygame.image.load("ダッシュ3.png")
            _value.kxh=0
            _value.kyh=0
        if _value.pose==4:
            img1 = pygame.image.load("ダッシュ4.png")
            _value.kxh=0
            _value.kyh=0
        if _value.pose==5:
            img1 = pygame.image.load("ダッシュ5.png")
            _value.kxh=0
            _value.kyh=0
        if _value.pose==6:
            img1 = pygame.image.load("ダッシュ6.png")
            _value.kxh=0
            _value.kyh=0
        if _value.pose==7:
            img1 = pygame.image.load("ダッシュ7.png")
            _value.kxh=0
            _value.kyh=0
        if _value.pose==8:
            img1 = pygame.image.load("ダッシュ8.png")
            _value.kxh=0
            _value.kyh=0
        
        if _value.guard==1:
            img1 = pygame.image.load("静止ガード.gif")
        img1.set_colorkey((255, 255, 255))

        if _value.kyv<0:
            img1 = pygame.image.load("ジャンプ上.png")
        if _value.kyv>0:
            img1 = pygame.image.load("ジャンプ下.png")
        if _value.hob==1:
            if _value.hobc>0:
                img1 = pygame.image.load("ホバリングf5.png")
            if _value.hobc>2:
                img1 = pygame.image.load("ホバリングf4.png")
            if _value.hobc>4:
                img1 = pygame.image.load("ホバリングf3.png")
            if _value.hobc>8:
                img1 = pygame.image.load("ホバリングf2.png")
            if _value.hobc>16:
                img1 = pygame.image.load("ホバリングf1.png")
            if _value.hobc==0:
                img1 = pygame.image.load("ホバリングf1.png")
            if _value.hobc>0:
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
            _value.kxh=-3
            _value.kyh=-1
        
        


        if 6>_value.sura>0:
            img1 = pygame.image.load("スライディング3.png")
            img1.set_colorkey((255, 255, 255))
            img1 = img1.convert_alpha()
            _value.kxh=-8
            _value.kyh=10
        if _value.sura>=6:
            img1 = pygame.image.load("スライディング2.png")
            img1.set_colorkey((255, 255, 255))
            img1 = img1.convert_alpha()
            _value.kxh=-8
            _value.kyh=10


        img1.set_colorkey((255, 255, 255))
        img1 = img1.convert_alpha()
        if _value.flip==1:
            img1=pygame.transform.flip(img1, True, False)
        img1 = pygame.transform.scale_by(img1, 2)
        _value.screen.blit(img1, (_value.kx+_value.kxh, _value.ky+_value.kyh))
        time.sleep(0.01)
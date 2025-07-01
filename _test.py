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

def step7():
        pygame.display.update()
        
        _value.screen.fill((200,200,255))

        
        text = font.render("編集", False, (0,0,0))
        text_rect = text.get_rect(center=(700, 30))
        _value.screen.blit(text, text_rect)

        
        if _value.kytest==_value.ground: _value.hob=0
        # 終了イベントを確認 --- (*5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN: 
                if _value.kaih==0:
                    if event.key == K_RETURN:
                        if _value.kytest<_value.ground:
                            _value.hob=1
                            _value.hobc=18
                            _value.kytestv=-5
                        else:
                            if _value.shagam==1:
                                if _value.sura==0:
                                    _value.sura=30
                            else:
                                _value.kytestv=-17
                        if 620<_value.kxtest<730 and -10<_value.kytest<40:
                            _value.step=3
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
                        if _value.kytest<_value.ground and _value.hob==0 and _value.skaih==0 and _value.sura==0:
                            _value.skaih=20
                if event.key == pygame.K_ESCAPE:
                    _value.step=3
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
                        _value.kxtest+=1
                    else:
                        _value.kxtest+=4
                    if _value.kxtest>750:
                        _value.kxtest=750
                if pressed_keys[K_a]:
                    if _value.hob==1:
                        _value.kxtest-=1
                    else:
                        _value.kxtest-=4
                    if _value.kxtest<0:
                        _value.kxtest=0
            else:
                _value.pose=0

            if pressed_keys[K_RSHIFT] and _value.hobc==0:
                if _value.hob==1:
                    _value.hob=0
                    _value.kytestv=-6
            
            if pressed_keys[K_q] and _value.kytest==_value.ground:
                _value.guard=1
            else:
                _value.guard=0

            if pressed_keys[K_s] and _value.kytest==_value.ground and _value.guard==0:
                _value.shagam=1
            else:
                _value.shagam=0

        if _value.kaih>0 and _value.kytest==_value.ground:
            if _value.flip==1:
                _value.kxtest-=_value.kaih/3
                if _value.kxtest<0:
                    _value.kxtest=0
            else:
                _value.kxtest+=_value.kaih/3    
                if _value.kxtest>750:
                    _value.kxtest=750
        if _value.sura>0 and _value.kytest==_value.ground:
            if _value.flip==1:
                _value.kxtest-=_value.sura/3
                if _value.kxtest<0:
                    _value.kxtest=0
            else:
                _value.kxtest+=_value.sura/3    
                if _value.kxtest>750:
                    _value.kxtest=750

        
        if _value.kytest>=_value.ground and _value.kytestv>=0:
            _value.kytestv=0
        else:     
            if _value.hob==1:
                _value.kytestv+=0.2
                if _value.kytestv>1.6:_value.kytestv=1.6
            else:
                _value.kytestv+=1
        _value.kytest+=_value.kytestv
        if _value.kytest>_value.ground:
            _value.kytest=_value.ground
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
            _value.kytestv=-1
        else:
            _value.skaih=0
        if _value.sura>0:
            _value.sura-=1
            _value.kytestv=-1
        else:
            _value.sura=0

        _value.kxh=0
        _value.kyh=0
        bxh=0
        byh=0
        if _value.pose==0:
            if _value.buki==0:
                if _value.bosi==0:
                    img1 = pygame.image.load("ノーマルf.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ノーマルfボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ノーマルfファイター.png")
            if _value.buki==1:
                if _value.bosi==0:
                    img1 = pygame.image.load("ノーマルh.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ノーマルhボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ノーマルhファイター.png")
        if _value.shagam==1:
            if _value.buki==0:
                if _value.bosi==0:
                    img1 = pygame.image.load("しゃがみf.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("しゃがみfボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("しゃがみfファイター.png")
            if _value.buki==1:
                if _value.bosi==0:
                    img1 = pygame.image.load("しゃがみh.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("しゃがみhボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("しゃがみhファイター.png")
            _value.kxh=-8
            _value.kyh=22
        if _value.hob==0:
            if _value.pose==1:
                if _value.bosi==0:
                    img1 = pygame.image.load("ダッシュ1.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ダッシュ1ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ダッシュ1ファイター.png")
                _value.kxh=0
                _value.kyh=0
            if _value.pose==2:
                if _value.bosi==0:
                    img1 = pygame.image.load("ダッシュ2.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ダッシュ2ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ダッシュ2ファイター.png")
                _value.kxh=0
                _value.kyh=0
            if _value.pose==3:
                if _value.bosi==0:
                    img1 = pygame.image.load("ダッシュ3.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ダッシュ3ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ダッシュ3ファイター.png")
                _value.kxh=0
                _value.kyh=0
                bxh=2
            if _value.pose==4:
                if _value.bosi==0:
                    img1 = pygame.image.load("ダッシュ4.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ダッシュ4ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ダッシュ4ファイター.png")
                _value.kxh=0
                _value.kyh=0
                bxh=8
            if _value.pose==5:
                if _value.bosi==0:
                    img1 = pygame.image.load("ダッシュ5.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ダッシュ5ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ダッシュ5ファイター.png")
                _value.kxh=0
                _value.kyh=0
                bxh=7
            if _value.pose==6:
                if _value.bosi==0:
                    img1 = pygame.image.load("ダッシュ6.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ダッシュ6ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ダッシュ6ファイター.png")
                _value.kxh=0
                _value.kyh=0
                bxh=4
            if _value.pose==7:
                if _value.bosi==0:
                    img1 = pygame.image.load("ダッシュ7.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ダッシュ7ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ダッシュ7ファイター.png")
                _value.kxh=0
                _value.kyh=0
                bxh=2
            if _value.pose==8:
                if _value.bosi==0:
                    img1 = pygame.image.load("ダッシュ8.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ダッシュ8ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ダッシュ8ファイター.png")
                _value.kxh=0
                _value.kyh=0
        
        if _value.kytestv<0:
            if _value.bosi==0:
                img1 = pygame.image.load("ジャンプ上.png")
            if _value.bosi==1:
                img1 = pygame.image.load("ジャンプ上ボム.png")
            if _value.bosi==2:
                img1 = pygame.image.load("ジャンプ上ファイター.png")
        if _value.kytestv>0:
            if _value.bosi==0:
                img1 = pygame.image.load("ジャンプ下.png")
            if _value.bosi==1:
                img1 = pygame.image.load("ジャンプ下ボム.png")
            if _value.bosi==2:
                img1 = pygame.image.load("ジャンプ下ファイター.png")



        if _value.hob==1:
            if _value.buki==0:
                if _value.bosi==0:
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
                if _value.bosi==1:
                    if _value.hobc>0:
                        img1 = pygame.image.load("ホバリングf5ボム.png")
                    if _value.hobc>2:
                        img1 = pygame.image.load("ホバリングf4ボム.png")
                    if _value.hobc>4:
                        img1 = pygame.image.load("ホバリングf3ボム.png")
                    if _value.hobc>8:
                        img1 = pygame.image.load("ホバリングf2ボム.png")
                    if _value.hobc>16:
                        img1 = pygame.image.load("ホバリングf1ボム.png")
                    if _value.hobc==0:
                        img1 = pygame.image.load("ホバリングf1ボム.png")
                if _value.bosi==2:
                    if _value.hobc>0:
                        img1 = pygame.image.load("ホバリングf5ファイター.png")
                    if _value.hobc>2:
                        img1 = pygame.image.load("ホバリングf4ファイター.png")
                    if _value.hobc>4:
                        img1 = pygame.image.load("ホバリングf3ファイター.png")
                    if _value.hobc>8:
                        img1 = pygame.image.load("ホバリングf2ファイター.png")
                    if _value.hobc>16:
                        img1 = pygame.image.load("ホバリングf1ファイター.png")
                    if _value.hobc==0:
                        img1 = pygame.image.load("ホバリングf1ファイター.png")
            if _value.buki==1:
                if _value.bosi==0:
                    if _value.hobc>0:
                        img1 = pygame.image.load("ホバリングh5.png")
                    if _value.hobc>2:
                        img1 = pygame.image.load("ホバリングh4.png")
                    if _value.hobc>4:
                        img1 = pygame.image.load("ホバリングh3.png")
                    if _value.hobc>8:
                        img1 = pygame.image.load("ホバリングh2.png")
                    if _value.hobc>16:
                        img1 = pygame.image.load("ホバリングh1.png")
                    if _value.hobc==0:
                        img1 = pygame.image.load("ホバリングh1.png")
                if _value.bosi==1:
                    if _value.hobc>0:
                        img1 = pygame.image.load("ホバリングh5ボム.png")
                    if _value.hobc>2:
                        img1 = pygame.image.load("ホバリングh4ボム.png")
                    if _value.hobc>4:
                        img1 = pygame.image.load("ホバリングh3ボム.png")
                    if _value.hobc>8:
                        img1 = pygame.image.load("ホバリングh2ボム.png")
                    if _value.hobc>16:
                        img1 = pygame.image.load("ホバリングh1ボム.png")
                    if _value.hobc==0:
                        img1 = pygame.image.load("ホバリングh1ボム.png")
                if _value.bosi==2:
                    if _value.hobc>0:
                        img1 = pygame.image.load("ホバリングh5ファイター.png")
                    if _value.hobc>2:
                        img1 = pygame.image.load("ホバリングh4ファイター.png")
                    if _value.hobc>4:
                        img1 = pygame.image.load("ホバリングh3ファイター.png")
                    if _value.hobc>8:
                        img1 = pygame.image.load("ホバリングh2ファイター.png")
                    if _value.hobc>16:
                        img1 = pygame.image.load("ホバリングh1ファイター.png")
                    if _value.hobc==0:
                        img1 = pygame.image.load("ホバリングh1ファイター.png")
            _value.kxh=-3
            _value.kyh=-1
            byh=-2
        



        if 6>_value.sura>0:
            if _value.bosi==0:
                img1 = pygame.image.load("スライディング3.png")
            if _value.bosi==1:
                img1 = pygame.image.load("スライディング3ボム.png")
            if _value.bosi==2:
                img1 = pygame.image.load("スライディング3ファイター.png")
            img1.set_colorkey((255, 255, 255))
            img1 = pygame.transform.scale_by(img1, 1)
            img1 = img1.convert_alpha()
            _value.kxh=-8
            _value.kyh=10
        if _value.sura>=6:
            if _value.bosi==0:
                img1 = pygame.image.load("スライディング2.png")
            if _value.bosi==1:
                img1 = pygame.image.load("スライディング2ボム.png")
            if _value.bosi==2:
                img1 = pygame.image.load("スライディング2ファイター.png")
            img1.set_colorkey((255, 255, 255))
            img1 = pygame.transform.scale_by(img1, 1)
            img1 = img1.convert_alpha()
            _value.kxh=-8
            _value.kyh=10
        if _value.sura>=20:
            if _value.bosi==1:
                img1 = pygame.image.load("スライディング1ボム.png")
            if _value.bosi==2:
                img1 = pygame.image.load("スライディング1ファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = pygame.transform.scale_by(img1, 1)
                img1 = img1.convert_alpha()
                _value.kxh=-8
                _value.kyh=10
        


        
        img1.set_colorkey((255, 255, 255))
        img1 = pygame.transform.scale_by(img1, 1)
        img1 = img1.convert_alpha()
        if _value.flip==1:
            img1=pygame.transform.flip(img1, True, False)
        img1 = pygame.transform.scale_by(img1, 2)
        _value.screen.blit(img1, (_value.kxtest+_value.kxh, _value.kytest+_value.kyh))

        if _value.buki==1:
            img2 = pygame.image.load("buki.png")
            img2 = pygame.transform.scale_by(img2, 1.8)
            img2.set_colorkey((255, 255, 255))
            img2 = img2.convert_alpha()
            bxh-=20
            if _value.flip==1:
                bxh=-bxh
                bxh-=16
                img2=pygame.transform.flip(img2, True, False)
            _value.screen.blit(img2, (_value.kxtest+_value.kxh+bxh, _value.kytest-37+_value.kyh+byh))

        time.sleep(0.01)
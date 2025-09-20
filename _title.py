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

def step1():
        pygame.display.update()
        _value.screen.blit(_value.pekin, (-60,0))
        mouseX, mouseY = pygame.mouse.get_pos()

        
        text = _value.font.render("コピーメーカー", False, (0,0,0))
        text_rect = text.get_rect(center=(400, 180))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("新規作成", False, (0,0,0))
        text_rectr = text.get_rect(center=(700, 30))
        _value.screen.blit(text, text_rectr)
        text = _value.font.render("ロード", False, (0,0,0))
        text_rectl = text.get_rect(center=(100, 30))
        _value.screen.blit(text, text_rectl)

        
        if _value.ky==_value.ground: _value.hob=0
        
        _value.mouseclick=0
        # 終了イベントを確認 --- (*5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                _value.mouseclick=1
                if _value.help==0:
                    if text_rectr.collidepoint(mouseX,mouseY):
                        _value.step=2
                        _value.se_enter1.play()
                    if text_rectl.collidepoint(mouseX,mouseY):
                        _value.step=10
                        _value.se_enter1.play()
            
            if _value.help==0:
                if event.type == KEYDOWN: 
                    if _value.kaih==0:
                        if event.key == K_RETURN:
                            if _value.ky<_value.ground:
                                if _value.hobfc==0:
                                    _value.hob=1
                                    _value.hobc=18
                                    _value.kyv=-2.7
                                    _value.se_hob.play()
                            else:
                                if _value.shagam==1:
                                    if _value.sura==0:
                                        _value.sura=50
                                        _value.se_sura.play()
                                else:
                                    _value.kyv=-6
                                    _value.se_jump.play()
                            if 620<_value.kx<730 and -10<_value.ky<40:
                                _value.step=2
                                _value.se_enter1.play()
                            if 40<_value.kx<150 and -10<_value.ky<40:
                                _value.step=10
                                _value.se_enter1.play()
                        if event.key == K_a and _value.skaih==0 and _value.kaih==0 and _value.sura==0:
                            _value.fliplip=1
                            if _value.ky>=_value.ground:
                                _value.se_run.play()
                        if event.key == K_d and _value.skaih==0 and _value.kaih==0 and _value.sura==0:
                            _value.fliplip=0
                            if _value.ky>=_value.ground:
                                _value.se_run.play()
                        if event.key == K_s:
                            if _value.guard==1 and _value.skaih==0 and _value.kaih==0 and _value.sura==0:
                                _value.skaih=30
                        if event.key == K_q:
                            if _value.ky<_value.ground and _value.hob==0 and _value.skaih==0 and _value.sura==0:
                                _value.skaih=20
                #
        class Fakekeys:
            def __getitem__(self, key):
                return False

        if _value.help==0:
            pressed_keys = pygame.key.get_pressed()
        else:
            pressed_keys = Fakekeys()
        if _value.kaih==0 and _value.skaih==0 and _value.sura==0:
            if (pressed_keys[K_d] or pressed_keys[K_a]) and _value.guard==0 and _value.hobfc==0:
                _value.posetime+=1
                if _value.posetime==6:
                    _value.posetime=0
                    _value.pose+=1
                    if _value.pose==9:
                        _value.pose=1
                if pressed_keys[K_d]:
                    _value.flip=0
                    if _value.hob==1:
                        _value.kxv+=1.5
                        if _value.kxv>1.5:
                            _value.kxv=1.5
                    else:
                        _value.kxv=2
                        if _value.kxv>2:
                            _value.kxv=2
                    if _value.kx>750:
                        _value.kx=750
                if pressed_keys[K_a]:
                    _value.flip=1
                    if _value.hob==1:
                        _value.kxv-=1.5
                        if _value.kxv<-1.5:
                            _value.kxv=-1.5
                    else:
                        _value.kxv-=2
                        if _value.kxv<-2:
                            _value.kxv=-2
                    if _value.kx<0:
                        _value.kx=0
                if pressed_keys[K_d] and pressed_keys[K_a]:
                    _value.pose=0
                    _value.flip=1-_value.fliplip
            else:
                _value.pose=0

            if pressed_keys[K_RSHIFT] and _value.hobfc==0:
                if _value.hob==1:
                    _value.hob=0
                    _value.hobfc=10
                    _value.se_hobfin.play()

            
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
        if _value.sura>6 and _value.ky==_value.ground:
            if _value.flip==1:
                _value.kxv=-2
                if _value.kx<0:
                    _value.kx=0
            else:
                _value.kxv=2 
                if _value.kx>750:
                    _value.kx=750
        if 0<_value.sura<=6 and _value.ky==_value.ground:
            if _value.flip==1:
                _value.kxv=-0.5
                if _value.kx<0:
                    _value.kx=0
            else:
                _value.kxv=0.5
                if _value.kx>750:
                    _value.kx=750
        
        _value.kx+=_value.kxv
        if _value.kx>750:_value.kx=750
        if _value.kx<0:_value.kx=0
        if _value.kyv>0 and _value.hob==0:_value.kxv=0
        if _value.kyv==0:
            if _value.kxv>0.1:
                _value.kxv-=0.1
            elif _value.kxv<-0.1:
                _value.kxv+=0.1
            else:
                _value.kxv=0
        if _value.kyv>=0 and _value.hob==1:
            if _value.kxv>0.05:
                _value.kxv-=0.05
            elif _value.kxv<-0.05:
                _value.kxv+=0.05
            else:
                _value.kxv=0
        
        if _value.ky>=_value.ground and _value.kyv>=0:
            _value.kyv=0
        else:     
            if _value.hob==1:
                _value.kyv+=0.08
                if _value.kyv>1.4:_value.kyv=1.4
            else:
                if _value.hobfc<5:
                    _value.kyv+=0.2
                    if _value.kyv>6:_value.kyv=6
        _value.ky+=_value.kyv
        if _value.ky>_value.ground:
            _value.ky=_value.ground
        if _value.hobc>0:
            _value.hobc-=1
        else:
            _value.hobc=0
        if _value.hobfc>0:
            _value.hobfc-=1
        else:
            _value.hobfc=0
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
        
        _func.help(400,100,1,"このゲームはカービィのコピー能力を自作して動かすことができるだけのゲームです")
        time.sleep(0.01)
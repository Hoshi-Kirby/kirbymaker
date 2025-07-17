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
        if _value.ka8==0:
            fill=0,0,0
            fill2=(100,100,100)
            fill3=(100,100,100)
        elif _value.ka8==1:
            fill=(100,100,100)
            fill2=0,0,0
            fill3=(100,100,100)
        else:
            fill=(100,100,100)
            fill2=(100,100,100)
            fill3=0,0,0
        if _value.wazatype[_value.ka3]==0:
            tab=1
            if(_value.t2<10):
                _func.settingkirby(100,298,1)
            if(10<=_value.t2<15):
                _func.settingkirby(100,298,2)
            if(15<=_value.t2<20):
                _func.settingkirby(100,298,3)
            if(20<=_value.t2):
                _func.settingkirby(100,298,4)
            text = font.render("カービィ", False, fill)
            text_rect = text.get_rect(center=(500, 200))
            _value.screen.blit(text, text_rect)
            text = font.render(str(_value.ka8_2[_value.ka3]), False, fill)
            text_rect = text.get_rect(center=(550, 230))
            _value.screen.blit(text, text_rect)
            if _value.erabuki[_value.ka3]==0:
                text = font.render("武器を消す", False, fill2)
            if _value.erabuki[_value.ka3]==1:
                text = font.render("武器を描く→", False, fill2)
            text_rect = text.get_rect(center=(500, 300))
            _value.screen.blit(text, text_rect)
            
        if _value.wazatype[_value.ka3]==1:
            tab=2
            if(_value.t2<25):
                _func.settingkirby(100,298,1)
            if(25<=_value.t2<50):
                _func.settingkirby(100,298,2)
            if(50<=_value.t2<75):
                _func.settingkirby(100,298,3)
            if(75<=_value.t2):
                _func.settingkirby(100,298,4)
            text = font.render("カービィ", False, fill)
            text_rect = text.get_rect(center=(500, 200))
            _value.screen.blit(text, text_rect)
            text = font.render(str(_value.ka8_2[_value.ka3]), False, fill)
            text_rect = text.get_rect(center=(550, 230))
            _value.screen.blit(text, text_rect)
            text = font.render("飛び道具→", False, fill2)
            text_rect = text.get_rect(center=(500, 300))
            _value.screen.blit(text, text_rect)
            if _value.erabuki[_value.ka3]==0:
                text = font.render("武器を消す", False, fill3)
            if _value.erabuki[_value.ka3]==1:
                text = font.render("武器を描く→", False, fill3)
            text_rect = text.get_rect(center=(500, 400))
            _value.screen.blit(text, text_rect)
        if _value.wazatype[_value.ka3]==2:
            tab=1
            if(_value.t2<25):
                _func.settingkirby(100,298,1)
            if(25<=_value.t2<50):
                _func.settingkirby(100,298,2)
            if(50<=_value.t2<75):
                _func.settingkirby(100,298,3)
            if(75<=_value.t2):
                _func.settingkirby(100,298,4)
            text = font.render("カービィ", False, fill)
            text_rect = text.get_rect(center=(500, 200))
            _value.screen.blit(text, text_rect)
            text = font.render(str(_value.ka8_2[_value.ka3]), False, fill)
            text_rect = text.get_rect(center=(550, 230))
            _value.screen.blit(text, text_rect)
            if _value.erabuki[_value.ka3]==0:
                text = font.render("武器を消す", False, fill2)
            if _value.erabuki[_value.ka3]==1:
                text = font.render("武器を描く→", False, fill2)
            text_rect = text.get_rect(center=(500, 300))
            _value.screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    if _value.ka8==0:
                        _value.ka8_2[_value.ka3]+=1
                        if _value.ka8_2[_value.ka3]>17:_value.ka8_2[_value.ka3]=17
                    if _value.ka8==2:
                        _value.erabuki[_value.ka3]=1
                if event.key==pygame.K_LEFT:
                    if _value.ka8==0:
                        _value.ka8_2[_value.ka3]-=1
                        if _value.ka8_2[_value.ka3]<0:_value.ka8_2[_value.ka3]=0
                    if _value.ka8==2:
                        _value.erabuki[_value.ka3]=0
                if event.key==pygame.K_UP:
                    _value.ka8-=1
                    if _value.ka8<0:_value.ka8=0
                if event.key==pygame.K_DOWN:
                    _value.ka8+=1
                    if _value.ka8>tab:_value.ka8=tab
                if event.key==pygame.K_RETURN:
                    if _value.ka8==2:_value.step=4
                    _value.ka8+=1
                if event.key==pygame.K_ESCAPE:
                    _value.step=4
        _value.t+=1
        _value.t2+=1
        if _value.t>_value.kzi[_value.ka3]*100:
            _value.t=0
            _value.t2=0
            _value.ws=0
            _value.ad=0
            _value.kx=_value.kx0[_value.ka3]*50
            _value.ky=_value.ky0[_value.ka3]*50
            _value.kxv=_value.kx1[_value.ka3]
            _value.kyv=_value.ky1[_value.ka3]
        
        _value.kxv+=_value.kx2[_value.ka3]*0.05+_value.kad2[_value.ka3]*_value.ad*0.01
        _value.kyv+=_value.ky2[_value.ka3]*0.05+_value.kws2[_value.ka3]*_value.ws*0.01
        _value.kx+=_value.kxv+_value.kad1[_value.ka3]*_value.ad*0.5
        _value.ky+=_value.kyv+_value.kws1[_value.ka3]*_value.ws*0.5

        if _value.wazapene[_value.ka3]==0:
            if _value.ky>0:_value.t=_value.kzi[_value.ka3]*100
        if _value.wazapene[_value.ka3]==1:
            if _value.ky>0 and _value.kyv>0:_value.kyv=-_value.kyv
        
        if _value.wazapene[_value.ka3]==0:
            if _value.ky>0:_value.t2=_value.kzi[_value.ka3]*100

        time.sleep(0.01)
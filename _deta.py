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


def step4():
        pygame.display.update()
        _value.screen.fill((200,200,255))
        if _value.wazatype[_value.ka3]==2:
            _func.settingkirby(_value.kx+100,_value.ky+298)
        else:
            _func.settingkirby(100,298)

        if _value.wazatype[_value.ka3]==1:#kx2[ka3]*0.1*t*t+(kx1[ka3]+kad2[ka3]*0.02*ad)*t*1.5+kx0[ka3]*50+125+kad1[ka3]*ad*1.5,ky2[ka3]*0.1*t*t+(ky1[ka3]+kws2[ka3]*0.02*ws)*1.5*t+ky0[ka3]*50+315+kws1[ka3]*ws*1.5
            pygame.draw.circle(_value.screen,(0,0,0),(_value.kx+125,_value.ky+315),5)

        if _value.wazatype[_value.ka3]==0:
            rect_surface = pygame.Surface((abs(_value.kx0[_value.ka3]), abs(_value.ky2[_value.ka3])), pygame.SRCALPHA)
            rect_surface.fill((255, 0, 0, 128))  # ← A=128で半透明
            _value.screen.blit(rect_surface, (_value.kx2[_value.ka3] + 125,_value.kx1[_value.ka3] + 315))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 入力欄がクリックされたかどうか
                if _value.input_box.collidepoint(event.pos):
                    _value.ka4=0
                else:
                    _value.active = False
                _value.color = _value.color_active if _value.active else _value.color_inactive

            elif event.type == pygame.KEYDOWN:
                if _value.active:
                    if event.key == pygame.K_BACKSPACE:
                        _value.title = _value.title[:-1]
                    else:
                        if event.key!=pygame.K_RETURN:
                            _value.title += event.unicode
                    if event.key==pygame.K_RETURN:
                        _value.active=False
                        _value.color = _value.color_active if _value.active else _value.color_inactive
                        _value.title_list[_value.ka3] = _value.title
                if event.key == pygame.K_ESCAPE:
                    _value.step=3
                if event.key == pygame.K_UP:
                    _value.ka4-=1
                if event.key == pygame.K_DOWN:
                    if _value.title=="" or _value.ka4>0:
                        _value.ka4+=1
                        if _value.ka4>_value.tab4:
                            _value.ka4=_value.tab4
                if event.key==pygame.K_RETURN:
                    if _value.ka4==2:
                        _value.step=5
                    elif _value.ka4==7:
                        _value.step=6
                    else:
                        _value.ka4+=1
                        if _value.ka4>_value.tab4:
                            _value.ka4=_value.tab4
                if event.key==pygame.K_RIGHT:
                    if _value.ka4==1:
                        _value.wazatype[_value.ka3]+=1
                        if _value.wazatype[_value.ka3]>2:_value.wazatype[_value.ka3]=2
                        if _value.wazapene[_value.ka3]==2:_value.wazapene[_value.ka3]=1
                    if _value.ka4==3 and _value.wazatype[_value.ka3]!=0:
                        _value.wazapene[_value.ka3]+=1
                        if _value.wazapene[_value.ka3]>2:_value.wazapene[_value.ka3]=2
                        if _value.wazapene[_value.ka3]>1 and _value.wazatype[_value.ka3]==2:_value.wazapene[_value.ka3]=1
                    if _value.ka4==4:
                        _value.wazatuka[_value.ka3]+=1
                        if _value.wazatuka[_value.ka3]>1:_value.wazatuka[_value.ka3]=1
                    if _value.ka4==5:
                        _value.wazadame[_value.ka3]+=1
                        if _value.wazadame[_value.ka3]>100:_value.wazadame[_value.ka3]=100
                    if _value.ka4==6:
                        _value.wazahuto[_value.ka3]+=1
                    if _value.ka4==9:
                        _value.wazatame[_value.ka3]+=1
                if event.key==pygame.K_LEFT:
                    if _value.ka4==1:
                        _value.wazatype[_value.ka3]-=1
                        if _value.wazatype[_value.ka3]<0:_value.wazatype[_value.ka3]=0
                        if _value.wazapene==2:wazapene=0
                    if _value.ka4==3 and _value.wazatype[_value.ka3]!=0:
                        _value.wazapene[_value.ka3]-=1
                        if _value.wazapene[_value.ka3]<0:wazapene[_value.ka3]=0
                    if _value.ka4==4:
                        _value.wazatuka[_value.ka3]-=1
                        if _value.wazatuka[_value.ka3]<0:_value.wazatuka[_value.ka3]=0
                    if _value.ka4==5:
                        _value.wazadame[_value.ka3]-=1
                        if _value.wazadame[_value.ka3]<0:_value.wazadame[_value.ka3]=0
                    if _value.ka4==6:
                        _value.wazahuto[_value.ka3]-=1
                        if _value.wazahuto[_value.ka3]<0:_value.wazahuto[_value.ka3]=0
                    if _value.ka4==9:
                        _value.wazatame[_value.ka3]-=1
                        if _value.wazatame[_value.ka3]<0:_value.wazatame[_value.ka3]=0
                        if _value.ka3>=20:
                            if _value.wazatame[_value.ka3]<_value.wazatame[_value.ka3-10]:_value.wazatame[_value.ka3]=_value.wazatame[_value.ka3-10]
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w]:
            _value.ws=-1
        elif pressed_keys[K_s]:
            _value.ws=+1
        else:
            _value.ws=0
        if pressed_keys[K_a]:
            _value.ad=-1
        elif pressed_keys[K_d]:
            _value.ad=+1
        else:
            _value.ad=0
        if pressed_keys[K_RIGHT]:
            if _value.rightime>0:
                _value.rightime-=1
            else:
                if _value.ka4==5:
                    _value.wazadame[_value.ka3]+=1
                    if _value.wazadame[_value.ka3]>100:_value.wazadame[_value.ka3]=100
                if _value.ka4==6:
                    _value.wazahuto[_value.ka3]+=1 
                if _value.ka4==9:
                    _value.wazatame[_value.ka3]+=1 
        else:
            _value.rightime=10
        if pressed_keys[K_LEFT]:
            if _value.leftime>0:
                _value.leftime-=1
            else:
                if _value.ka4==5:
                    _value.wazadame[_value.ka3]-=1
                    if _value.wazadame[_value.ka3]<0:_value.wazadame[_value.ka3]=0
                if _value.ka4==6:
                    _value.wazahuto[_value.ka3]-=1 
                    if _value.wazahuto[_value.ka3]<0:_value.wazahuto[_value.ka3]=0
                if _value.ka4==9:
                    _value.wazatame[_value.ka3]-=1 
                    if _value.wazatame[_value.ka3]<0:_value.wazatame[_value.ka3]=0
        else:
            _value.leftime=10
        


        txt_surface = _value.font.render(_value.title, True, _value.color)
        width = max(400, txt_surface.get_width() + 10)
        _value.input_box.w = width
        _value.screen.blit(txt_surface, (_value.input_box.x + 5, _value.input_box.y + 5))
        pygame.draw.rect(_value.screen, _value.color, _value.input_box, 2)

        text = _value.font.render("→", False, (0,0,0))
        text_rect = text.get_rect(center=(350, 100+50*_value.ka4))
        if _value.ka4>0:
            _value.active=False
            _value.color = _value.color_active if _value.active else _value.color_inactive
            _value.screen.blit(text, text_rect)
        if _value.ka4<=0:
            _value.active = True
            _value.color = _value.color_active if _value.active else _value.color_inactive
            _value.ka4=0
        
        if _value.wazatype[_value.ka3]==0:
            text = _value.font.render("近距離", False, (0,0,0))
        else:
            text = _value.font.render("近距離", False, (100,100,100))
        text_rect = text.get_rect(center=(450, 150))
        _value.screen.blit(text, text_rect)

        if _value.wazatype[_value.ka3]==1:
            text = _value.font.render("遠距離", False, (0,0,0))
        else:
            text = _value.font.render("遠距離", False, (100,100,100))
        text_rect = text.get_rect(center=(550, 150))
        _value.screen.blit(text, text_rect)

        if _value.wazatype[_value.ka3]==2:
            text = _value.font.render("突進", False, (0,0,0))
        else:
            text = _value.font.render("突進", False, (100,100,100))
        text_rect = text.get_rect(center=(640, 150))
        _value.screen.blit(text, text_rect)

        if _value.wazatype[_value.ka3]==0:
            text = _value.font.render("攻撃範囲→", False, (0,0,0))
        else:
            text = _value.font.render("軌道→", False, (0,0,0))
        text_rect = text.get_rect(center=(470, 200))
        _value.screen.blit(text, text_rect)
        
        if _value.wazatype[_value.ka3]!=0:
            _value.font = pygame.font.SysFont("hg正楷書体pro", 20)
            text = _value.font.render("ぶつかったとき", False, (0,0,0))
            text_rect = text.get_rect(center=(480, 230))
            _value.screen.blit(text, text_rect)
            _value.font = pygame.font.SysFont("hg正楷書体pro", 30)
            if _value.wazatype[_value.ka3]==1:
                if _value.wazapene[_value.ka3]==0:
                    text = _value.font.render("消滅", False, (0,0,0))
                else:
                    text = _value.font.render("消滅", False, (100,100,100))
            if _value.wazatype[_value.ka3]==2:
                if _value.wazapene[_value.ka3]==0:
                    text = _value.font.render("停止", False, (0,0,0))
                else:
                    text = _value.font.render("停止", False, (100,100,100))
            text_rect = text.get_rect(center=(450, 250))
            _value.screen.blit(text, text_rect)


            if _value.wazapene[_value.ka3]==1:
                text = _value.font.render("反射", False, (0,0,0))
            else:
                text = _value.font.render("反射", False, (100,100,100))
            text_rect = text.get_rect(center=(550, 250))
            _value.screen.blit(text, text_rect)

            if _value.wazatype[_value.ka3]==1:
                if _value.wazapene[_value.ka3]==2:
                    text = _value.font.render("貫通", False, (0,0,0))
                else:
                    text = _value.font.render("貫通", False, (100,100,100))
                text_rect = text.get_rect(center=(640, 250))
                _value.screen.blit(text, text_rect)


        text = _value.font.render("掴み", False, (0,0,0))
        text_rect = text.get_rect(center=(450, 300))
        _value.screen.blit(text, text_rect)
        if _value.wazatuka[_value.ka3]==0:
            text = _value.font.render("なし", False, (0,0,0))
        else:
            text = _value.font.render("なし", False, (100,100,100))
        text_rect = text.get_rect(center=(550, 300))
        _value.screen.blit(text, text_rect)

        if _value.wazatuka[_value.ka3]==1:
            text = _value.font.render("あり→", False, (0,0,0))
        else:
            text = _value.font.render("あり", False, (100,100,100))
        text_rect = text.get_rect(center=(650, 300))
        _value.screen.blit(text, text_rect)


        text = _value.font.render("ダメージ量　　　　　％", False, (0,0,0))
        text_rect = text.get_rect(center=(570, 350))
        _value.screen.blit(text, text_rect)
        text = _value.font.render(str(_value.wazadame[_value.ka3]), False, (0,0,0))
        text_rect = text.get_rect(center=(670, 350))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("吹っ飛ばし力", False, (0,0,0))
        text_rect = text.get_rect(center=(500, 400))
        _value.screen.blit(text, text_rect)
        text = _value.font.render(str(_value.wazahuto[_value.ka3]), False, (0,0,0))
        text_rect = text.get_rect(center=(670, 400))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("反動→", False, (0,0,0))
        text_rect = text.get_rect(center=(450, 450))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("デザイン→", False, (0,0,0))
        text_rect = text.get_rect(center=(470, 500))
        _value.screen.blit(text, text_rect)
        if _value.ka3>=10:
            text = _value.font.render("溜め時間", False, (0,0,0))
            text_rect = text.get_rect(center=(470, 550))
            _value.screen.blit(text, text_rect)
            text = _value.font.render(str(_value.wazatame[_value.ka3]), False, (0,0,0))
            text_rect = text.get_rect(center=(670, 550))
            _value.screen.blit(text, text_rect)

        # all station
        _value.t+=1
        if _value.t>_value.kzi[_value.ka3]*100:
            _value.t=0
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

        if _value.wazapene[0]==0:
            if _value.ky>0:_value.t=_value.kzi[_value.ka3]*100
        if _value.wazapene[0]==1:
            if _value.ky>0 and _value.kyv>0:_value.kyv=-_value.kyv

        # pygame.display.flip()
        time.sleep(0.01)
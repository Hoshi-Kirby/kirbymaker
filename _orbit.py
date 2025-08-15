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

def step5():
        pygame.display.update()
        _value.screen.fill((200,200,255))
        pygame.draw.line(_value.screen,(0,0,0),(25,315),(225,315),1)
        pygame.draw.line(_value.screen,(0,0,0),(125,215),(125,415),1)
        if _value.wazatype[_value.ka3]==2:
            if(_value.t2<10):
                _func.settingkirby(_value.kx+100,_value.ky+298,1)
            if(10<=_value.t2<15):
                _func.settingkirby(_value.kx+100,_value.ky+298,2)
            if(15<=_value.t2<20):
                _func.settingkirby(_value.kx+100,_value.ky+298,3)
            if(20<=_value.t2):
                _func.settingkirby(_value.kx+100,_value.ky+298,4)
        else:
            if(_value.t2<10):
                _func.settingkirby(100,298,1)
            if(10<=_value.t2<15):
                _func.settingkirby(100,298,2)
            if(15<=_value.t2<20):
                _func.settingkirby(100,298,3)
            if(20<=_value.t2):
                _func.settingkirby(100,298,4)
        if _value.wazatype[_value.ka3]==0:
            fill=0,0,0
            text = font.render("rect        ,         ,         ,        ", False, (fill))
            text_rect = text.get_rect(center=(500, 200))
            _value.screen.blit(text, text_rect)
            text = font.render("(t<        )", False, (fill))
            text_rect = text.get_rect(center=(500, 400))
            _value.screen.blit(text, text_rect)
            # rect = pygame.Rect(int(_value.kx2[_value.ka3] + 125),int(_value.kx1[_value.ka3] + 315),int(_value.kx0[_value.ka3]),int(_value.ky2[_value.ka3]))
            rect_surface = pygame.Surface((abs(_value.kx0[_value.ka3]),abs( _value.ky2[_value.ka3])), pygame.SRCALPHA)

            rect_surface.fill((255, 0, 0, 128))  # ← A=128で半透明

            _value.screen.blit(rect_surface, (_value.kx2[_value.ka3] + 125,_value.kx1[_value.ka3] + 315))

            # pygame.draw.rect(_value.screen,(255,0,0),rect)
        else:
            if _value.ka5<7:
                fill=0,0,0
                fill2=(100,100,100)
                fill3=(100,100,100)
            elif 7<=_value.ka5<11:
                fill=(100,100,100)
                fill2=0,0,0
                fill3=(100,100,100)
            else:
                fill=(100,100,100)
                fill2=(100,100,100)
                fill3=0,0,0
            text = font.render("x方向     t^2+      t+                ", False, (fill))
            text_rect = text.get_rect(center=(500, 200))
            _value.screen.blit(text, text_rect)
            text = font.render("ad入力     t^2+      t+                 ", False, (fill2))
            text_rect = text.get_rect(center=(500,250))
            _value.screen.blit(text, text_rect)
            text = font.render("    y方向     t^2+      t+        (t<        )", False, (fill))
            text_rect = text.get_rect(center=(500, 400))
            _value.screen.blit(text, text_rect)
            text = font.render("ws入力     t^2+      t+                 ", False, (fill2))
            text_rect = text.get_rect(center=(500, 450))
            _value.screen.blit(text, text_rect)
            # 遠距離の弾
            if _value.wazatype[_value.ka3]==1:#kx2[_value.ka3]*0.1*t*t+(kx1[_value.ka3]+kad2[_value.ka3]*0.02*ad)*t*1.5+kx0[_value.ka3]*50+125+kad1[_value.ka3]*ad*1.5,ky2[_value.ka3]*0.1*t*t+(ky1[_value.ka3]+kws2[_value.ka3]*0.02*ws)*1.5*t+ky0[_value.ka3]*50+315+kws1[_value.ka3]*ws*1.5
                img1 = pygame.image.load(f"hado ({_value.ka3}).png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5*(1.02**(-_value.hados[_value.ka3])))
                _value.screen.blit(img1, (_value.kx+105+30-60*(1.02**(-_value.hados[_value.ka3])),_value.ky+282+30-60*(1.02**(-_value.hados[_value.ka3]))))
                text = font.render("弾数      個　間隔       秒", False, (fill3))
                text_rect = text.get_rect(center=(500, 100))
                _value.screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    _value.ka5-=1
                    if _value.ka5<0:_value.ka5=0
                    if _value.ka5==6:_value.ka5=7
                    if _value.ka5==10:_value.ka5=11
                if event.key==pygame.K_DOWN:
                    _value.ka5+=1
                    if _value.ka5==7:_value.ka5=6
                    if _value.ka5==11:_value.ka5=10
                    if _value.ka5==13:_value.ka5=12
                if event.key==pygame.K_RETURN:
                    _value.ka5+=1
                    if _value.ka5==7:_value.ka5=6
                    if _value.ka5==11:_value.step=4
                if event.key==pygame.K_ESCAPE:
                    _value.step=4
            for i in range(_value.tab5):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if _value.box_rects[i].collidepoint(event.pos):
                        _value.ka5=i
                    else:
                        _value.active2[i]=False
                if _value.active2[i] and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        _value.input_text[i] = _value.input_text[i][:-1]
                    elif event.unicode.isdigit():
                        _value.input_text[i] += event.unicode
                    elif event.key == pygame.K_PERIOD:
                        _value.input_text[i] += event.unicode
                    elif event.key == pygame.K_MINUS:
                        _value.input_text[i] += event.unicode
                    try:
                        value = float(_value.input_text[i])
                    except ValueError:
                        value = 0

                    match i:
                        case 0:_value.kx2[_value.ka3]=value
                        case 1:_value.kx1[_value.ka3]=value
                        case 2:_value.kx0[_value.ka3]=value
                        case 3:_value.ky2[_value.ka3]=value
                        case 4:_value.ky1[_value.ka3]=value
                        case 5:_value.ky0[_value.ka3]=value
                        case 6:_value.kzi[_value.ka3]=value
                        case 7:_value.kad2[_value.ka3]=value
                        case 8:_value.kad1[_value.ka3]=value
                        case 9:_value.kws2[_value.ka3]=value
                        case 10:_value.kws1[_value.ka3]=value
                    if _value.wazatype[_value.ka3]==0:
                        _value.kzi[_value.ka3]=_value.ky2[_value.ka3]
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
                    
        for i in range(_value.tab5):
            if _value.ka5==i:
                _value.active2[i]=True
            else:
                _value.active2[i]=False


            text_surface = font.render(_value.input_text[i], True, (0,0,0))
            _value.screen.blit(text_surface, (_value.box_rects[i].x + 5, _value.box_rects[i].y))
            pygame.draw.line(_value.screen, (0,0,0),
                        (_value.box_rects[i].x, _value.box_rects[i].bottom),
                        (_value.box_rects[i].right, _value.box_rects[i].bottom), 2)
            if _value.active2[i] and pygame.time.get_ticks() % 1000 < 500:
                cursor_x = _value.box_rects[i].x + 5 + text_surface.get_width()
                pygame.draw.line(_value.screen, (0,0,0),
                                (cursor_x, _value.box_rects[i].y + 5),
                                (cursor_x, _value.box_rects[i].y + 25), 2)
        # if wazatype[_value.ka3]==0:
        # else:
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

        if _value.wazatype[_value.ka3]>0:
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
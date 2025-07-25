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

def step2():
        image = cv2.imread(r"C:\python\kirby\buki.png")
        if _value.flip==0:
            image = cv2.imread(r"C:\python\kirby\buki.png")
        if _value.flip==1:
            image = cv2.imread(r"C:\python\kirby\buki2.png")
        pygame.display.update()
        _value.screen.fill((200,200,255))
        mouseX, mouseY = pygame.mouse.get_pos()
        _func.settingkirby(100,298,0)

        if _value.step2==0:
            if _value.ka==0:
                text = font.render("帽子　←　　　　　→", False, (150,50,50))
            else:
                text = font.render("帽子　←　　　　　→", False, (0,0,0))
            text_rect = text.get_rect(center=(440, 200))
            _value.screen.blit(text, text_rect)
            if _value.bosi==0:
                text = font.render("なし", False, (0,0,0))
            if _value.bosi==1:
                text = font.render("ボム", False, (0,0,0))
            if _value.bosi==2:
                text = font.render("ファイター", False, (0,0,0))
            text_rect = text.get_rect(center=(480, 200))
            _value.screen.blit(text, text_rect)

            if _value.ka==1:
                text = font.render("武器　←　　→", False, (150,50,50))
            else:
                text = font.render("武器　←　　→", False, (0,0,0))
            text_rect = text.get_rect(center=(400, 400))
            _value.screen.blit(text, text_rect)
            if _value.buki==0:
                text = font.render("なし", False, (0,0,0))
            if _value.buki==1:
                text = font.render("あり", False, (0,0,0))
            text_rect = text.get_rect(center=(450, 400))
            _value.screen.blit(text, text_rect)
            if _value.buki==1:
                if _value.ka==2:
                    text = font.render("武器を変更する", False, (150,50,50))
                else:
                    text = font.render("武器を変更する", False, (0,0,0))
                text_rect = text.get_rect(center=(500, 450))
                _value.screen.blit(text, text_rect)
            if _value.esch==1:
                pygame.draw.rect(_value.screen, (140,140,180),(100,80,600,440))
                text=font.render("本当に戻ってよろしいですか？", False, (0,0,0))
                text_rect = text.get_rect(center=(400, 300))
                _value.screen.blit(text, text_rect)
        elif _value.step2==1:
            x=250
            y=50
            text=font.render("裏", False, (0,0,0))
            text_rect = text.get_rect(center=(400, 550))
            _value.screen.blit(text, text_rect)
            for i in range(45):
                for i2 in range(32):
                    if _value.flip==0:
                        i3=i2
                    else:
                        i3=31-i2
                    fill=_func.bgr_to_rgb(image[i,i2])

                    if fill==(255,255,255):fill=_value.back
                    pygame.draw.rect(_value.screen,fill,(i3*10+x,i*10+y,10,10))
                    if i2*10+x<mouseX<i2*10+x+10 and i*10+y<mouseY<i*10+y+10:
                        _value.mx=i3
                        _value.my=i
            if mouseX<x or 320+x<mouseX or mouseY<y or 450+y<mouseY:
                _value.mx=-1
                _value.my=-1
            if _value.cr==255 and _value.cg==255 and _value.cb==255:
                fill=(254,254,254)
            else:
                fill=(_value.cr,_value.cg,_value.cb)
            pygame.draw.rect(_value.screen,fill,(700,100,20,20))
            pygame.draw.line(_value.screen,(255,0,0),(650,150),(750,150),3)
            pygame.draw.line(_value.screen,(0,255,0),(650,200),(750,200),3)
            pygame.draw.line(_value.screen,(0,0,255),(650,250),(750,250),3)
            pygame.draw.circle(_value.screen,(255,255,255),(650+_value.cr*100/255,150),5)
            pygame.draw.circle(_value.screen,(255,255,255),(650+_value.cg*100/255,200),5)
            pygame.draw.circle(_value.screen,(255,255,255),(650+_value.cb*100/255,250),5)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN: 
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if _value.ka==0:
                        _value.bosi-=1
                        if _value.bosi<0:_value.bosi=0
                    if _value.ka==1:
                        _value.buki=0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if _value.ka==0:
                        _value.bosi+=1
                        if _value.bosi>2:_value.bosi=2
                    if _value.ka==1:
                        _value.buki=1
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if _value.step2==0:
                        _value.ka-=1
                    if _value.ka<0:_value.ka=0
                    

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if _value.step2==0:
                        _value.ka+=1
                        if _value.ka>1+_value.buki:_value.ka=1+_value.buki
                
                if event.key == pygame.K_RSHIFT:
                    _value.esch=0
                if event.key == pygame.K_RETURN:
                    if _value.step2==0:
                        if _value.ka<2:
                            _value.step=3
                        else:
                            _value.step2=1
                        if _value.esch==1:_value.step=1
                    else:
                        _value.step2=0
                if event.key == pygame.K_ESCAPE:
                    if _value.step2==0:
                        _value.esch=1
                    else:
                        _value.step2=0
            elif event.type == MOUSEBUTTONDOWN:
                if 350<mouseX<450 and 500<mouseY<600:
                    _value.flip=1-_value.flip
                if event.button == 1 and _value.step2==1:  # 左クリック
                    _value.drag = 1
                if event.button == 3 and _value.step2==1:  # 左クリック
                    _value.drag = 3
                    if _value.my>=0:
                        bgr = tuple(int(c) for c in image[_value.my, _value.mx])
                        fill = _func.bgr_to_rgb(bgr)
                        _value.cr,_value.cg,_value.cb=fill
                if event.button == 2 and _value.step2==1:
                    if _value.back==(255,255,255):_value.back=(0,0,0)
                    elif _value.back==(0,0,0):_value.back=(255,255,255)
            elif event.type == MOUSEBUTTONUP:
                if event.button ==1 and _value.drag==1:
                    _value.drag = 0
                if event.button ==3 and _value.drag==3:
                    _value.drag = 0
        if _value.drag==1:
            if _value.mx>=0:
                if _value.cr==255 and _value.cg==255 and _value.cb==255:
                    _value.cr2=254
                    _value.cg2=254
                    _value.cb2=254
                else:
                    _value.cr2=_value.cr
                    _value.cg2=_value.cg
                    _value.cb2=_value.cb
                image[_value.my,_value.mx]=[_value.cb2,_value.cg2,_value.cr2]
                if _value.flip==0:
                    cv2.imwrite("buki.png", image)
                    cv2.imwrite("buki2.png", image)
                if _value.flip==1:
                    cv2.imwrite("buki2.png", image)
            if 650<mouseX<750 and 140<mouseY<160:
                _value.cr=(mouseX-650)*2.55
            if 650<mouseX<750 and 190<mouseY<210:
                _value.cg=(mouseX-650)*2.55
            if 650<mouseX<750 and 240<mouseY<260:
                _value.cb=(mouseX-650)*2.55
        if _value.drag==3:
            if _value.my>=0:
                image[_value.my,_value.mx]=[255,255,255]
                if _value.flip==0:
                    cv2.imwrite("buki.png", image)
                if _value.flip==1:
                    cv2.imwrite("buki2.png", image)
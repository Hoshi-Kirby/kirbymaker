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

def step3():
        pygame.display.update()
        mouseX, mouseY = pygame.mouse.get_pos()
        _value.screen.fill((200,200,255))
        _func.settingkirby(100,298,0)
        if _value.ka3<10:
            fill=(0,0,0)
        elif _value.ka3<20:
            fill=(100,0,0)
        else:
            fill=(255,0,0)

        text = font.render("→", False, (fill))
        text_rect = text.get_rect(center=(300, 300))
        _value.screen.blit(text, text_rect)

        text = font.render("B", False, (fill))
        text_rect = text.get_rect(center=(400, 300+_value.sc))
        _value.screen.blit(text, text_rect)
        text = font.render("上B", False, (fill))
        text_rect = text.get_rect(center=(400, 350+_value.sc))
        _value.screen.blit(text, text_rect)
        text = font.render("下B", False, (fill))
        text_rect = text.get_rect(center=(400, 400+_value.sc))
        _value.screen.blit(text, text_rect)
        text = font.render("DB", False, (fill))
        text_rect = text.get_rect(center=(400, 450+_value.sc))
        _value.screen.blit(text, text_rect)
        text = font.render("空B", False, (fill))
        text_rect = text.get_rect(center=(400, 500+_value.sc))
        _value.screen.blit(text, text_rect)
        text = font.render("空上B", False, (fill))
        text_rect = text.get_rect(center=(400, 550+_value.sc))
        _value.screen.blit(text, text_rect)
        text = font.render("空下B", False, (fill))
        text_rect = text.get_rect(center=(400, 600+_value.sc))
        _value.screen.blit(text, text_rect)
        text = font.render("空DB", False, (fill))
        text_rect = text.get_rect(center=(400, 650+_value.sc))
        _value.screen.blit(text, text_rect)
        text = font.render("コマンド", False, (fill))
        text_rect = text.get_rect(center=(400, 700+_value.sc))
        _value.screen.blit(text, text_rect)


        for i in range(_value.tab):
            if _value.title_list[i]=="":
                text = font.render("設定なし", False, (fill))
            else:
                text = font.render(_value.title_list[i], False, (fill))
            text_rect = text.get_rect(center=(550, 300+50*i+_value.sc))
            _value.screen.blit(text, text_rect)
        
        x=50
        y=460
        pygame.draw.rect(_value.screen, (200,50,50), (x,y,80,40), width=3,border_radius=5)
        pygame.draw.rect(_value.screen, (100,100,200), (100+x,y,100,40), width=3,border_radius=5)
        text = font.render("保存", False, (fill))
        text_rect = text.get_rect(center=(x+40,y+20))
        _value.screen.blit(text, text_rect)
        text = font.render("プレイ", False, (fill))
        text_rect = text.get_rect(center=(x+150,y+20))
        _value.screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if x<mouseX<80+x and y<mouseY<40+mouseY:
                        #保存
                        a=1
                    if x+100<mouseX<x+200 and y<mouseY<y+40:
                        _value.step=7
            if event.type == KEYDOWN: 
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if _value.sctime==0:
                        _value.ka3-=1
                        if _value.ka3<0:_value.ka3=0
                        if _value.ka3==9:_value.ka3=10
                        if _value.ka3==19:_value.ka3=20
                        _value.sctime=10
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if _value.sctime==0:
                        _value.ka3+=1
                        if _value.ka3==_value.tab:_value.ka3=_value.tab-1
                        if _value.ka3==_value.tab+10:_value.ka3=_value.tab-1+10
                        if _value.ka3==_value.tab+20:_value.ka3=_value.tab-1+20
                        _value.sctime=-10
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if _value.ka3<20:
                        _value.ka3+=10
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if _value.ka3>=10:
                        _value.ka3-=10
                if event.key == pygame.K_ESCAPE:
                    _value.step=2
                if event.key == pygame.K_RETURN:
                    _value.step=4
        if _value.sctime<0:
            _value.sctime+=1
            _value.sc-=5
            if _value.sc<-50*_value.tab+50:_value.sc=-50*_value.tab+50
        if _value.sctime>0:
            _value.sctime-=1
            _value.sc+=5
            if _value.sc>0:_value.sc=0
        # if _value.ka3%10==1:_value.sc=-50*_value.tab+50
        # if _value.ka3%10==_value.tab:_value.sc=0


        # time.sleep(0.01)
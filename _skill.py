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

def step3():
        pygame.display.update()
        mouseX, mouseY = pygame.mouse.get_pos()
        _value.screen.fill((200,200,255))
        if _value.wazatype[_value.ka3]==2 and _value.t>_value.kzi[_value.ka3]*100:
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

        if _value.wazatype[_value.ka3]==1:#kx2[ka3]*0.1*t*t+(kx1[ka3]+kad2[ka3]*0.02*ad)*t*1.5+kx0[ka3]*50+125+kad1[ka3]*ad*1.5,ky2[ka3]*0.1*t*t+(ky1[ka3]+kws2[ka3]*0.02*ws)*1.5*t+ky0[ka3]*50+315+kws1[ka3]*ws*1.5
            if _value.t>_value.kzi[_value.ka3]*100:
                img1 = pygame.image.load(f"hado ({_value.ka3}).png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5*(1.02**(-_value.hados[_value.ka3])))
                _value.screen.blit(img1, (_value.kx+105+30-60*(1.02**(-_value.hados[_value.ka3])),_value.ky+282+30-60*(1.02**(-_value.hados[_value.ka3]))))

        if _value.wazatype[_value.ka3]==0:
            rect_surface = pygame.Surface((abs(_value.kx0[_value.ka3]), abs(_value.ky2[_value.ka3])), pygame.SRCALPHA)
            rect_surface.fill((255, 0, 0, 128))  # ← A=128で半透明
            _value.screen.blit(rect_surface, (_value.kx2[_value.ka3] + 125,_value.kx1[_value.ka3] + 315))
        if _value.ka3<10:
            fill=(0,0,0)
        elif _value.ka3<20:
            fill=(100,0,0)
        else:
            fill=(255,0,0)

        text = _value.font.render("→", False, (fill))
        text_rect = text.get_rect(center=(300, 300))
        _value.screen.blit(text, text_rect)

        text = _value.font.render("B", False, (fill))
        text_rect = text.get_rect(center=(400, 300+_value.sc))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("上B", False, (fill))
        text_rect = text.get_rect(center=(400, 350+_value.sc))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("下B", False, (fill))
        text_rect = text.get_rect(center=(400, 400+_value.sc))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("DB", False, (fill))
        text_rect = text.get_rect(center=(400, 450+_value.sc))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("空B", False, (fill))
        text_rect = text.get_rect(center=(400, 500+_value.sc))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("空上B", False, (fill))
        text_rect = text.get_rect(center=(400, 550+_value.sc))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("空下B", False, (fill))
        text_rect = text.get_rect(center=(400, 600+_value.sc))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("空DB", False, (fill))
        text_rect = text.get_rect(center=(400, 650+_value.sc))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("コマンド", False, (fill))
        text_rect = text.get_rect(center=(400, 700+_value.sc))
        _value.screen.blit(text, text_rect)

        mouseka3=-1
        for i in range(_value.tab-1):
            if _value.title_list[i]=="":
                text = _value.font.render("設定なし", False, (fill))
            else:
                text = _value.font.render(_value.title_list[i], False, (fill))
            text_rect = text.get_rect(center=(550, 300+50*i+_value.sc))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka3=i
                if _value.title_list[i]=="":
                    text = _value.font.render("設定なし", False, (tuple(int(255-(255-c)*0.8) for c in fill)))
                else:
                    text = _value.font.render(_value.title_list[i], False, (tuple(int(255-(255-c)*0.8) for c in fill)))
                text_rect = text.get_rect(center=(550, 300+50*i+_value.sc))
            _value.screen.blit(text, text_rect)
        if _value.title_list[_value.tab-1]=="":
            text = _value.font.render("設定なし", False, (fill))
            text_rect = text.get_rect(center=(550, 300+50*(_value.tab-1)+_value.sc))
        else:
            text = _value.font.render(_value.title_list[_value.tab-1], False, (fill))
            text_rect = text.get_rect(center=(550, 300+50*_value.tab+_value.sc))
        _value.screen.blit(text, text_rect)
        
        x=50
        y=510
        y2=460-y
        if x<mouseX<80+x and y<mouseY<40+y:
            hozon=(200,100,100)
        else:
            hozon=(0,0,0)
        if x+100<mouseX<x+200 and y<mouseY<y+40:
            purei=(100,100,200)
        else:
            purei=(0,0,0)
        if 50<mouseX<80+50 and y+y2<mouseY<40+y+y2:
            modoru=(100,100,100)
        else:
            modoru=(0,0,0)
        pygame.draw.rect(_value.screen, (200,50,50), (x,y,80,40), width=3,border_radius=5)
        pygame.draw.rect(_value.screen, (100,100,200), (100+x,y,100,40), width=3,border_radius=5)
        pygame.draw.rect(_value.screen, (100,100,100), (50,y+y2,80,40), width=3,border_radius=5)
        text = _value.font.render("保存", False, (hozon))
        text_rect = text.get_rect(center=(x+40,y+20))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("プレイ", False, (purei))
        text_rect = text.get_rect(center=(x+150,y+20))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("戻る", False, (modoru))
        text_rect = text.get_rect(center=(90,y+20+y2))
        _value.screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if x<mouseX<80+x and y<mouseY<40+y:
                        #保存
                        _value.stepbefore=3
                        _value.step=9
                    if x+100<mouseX<x+200 and y<mouseY<y+40:
                        _value.stepbefore=3
                        _value.step=7
                    if 50<mouseX<130 and y+y2<mouseY<y+40+y2:
                        _value.step=2
                    if mouseka3!=-1:
                        if _value.ka3==mouseka3:
                            _value.step=4
                        _value.sctime=(_value.ka3-mouseka3)*10
                        _value.ka3=mouseka3
                if event.button == 4:
                    if _value.sctime==0:
                        _value.ka3-=1
                        if _value.ka3<0:_value.ka3=0
                        if _value.ka3==9:_value.ka3=10
                        if _value.ka3==19:_value.ka3=20
                        _value.sctime=10
                if event.button == 5:
                    if _value.sctime==0:
                        _value.ka3+=1
                        if _value.ka3==_value.tab:_value.ka3=_value.tab-1
                        if _value.ka3==_value.tab+10:_value.ka3=_value.tab-1+10
                        if _value.ka3==_value.tab+20:_value.ka3=_value.tab-1+20
                        _value.sctime=-10
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
        
        # all station
        _value.t+=1
        _value.t2+=1
        if _value.t>_value.kzi2[_value.ka3]*100:
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
            if _value.ky>0:_value.t=_value.kzi2[_value.ka3]*100
        if _value.wazapene[_value.ka3]==1:
            if _value.ky>0 and _value.kyv>0:_value.kyv=-_value.kyv

        if _value.wazapene[_value.ka3]==0:
            if _value.ky>0:_value.t2=_value.kzi2[_value.ka3]*100
        # pygame.display.flip()
        time.sleep(0.01)
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
        mouseka4=-1
        for i in range (_value.tab4):
            text = _value.font.render("遠遠遠遠遠距距離離離離離", False, (200,150,150))
            text_rect = text.get_rect(center=(570, 150+i*50))
            if text_rect.collidepoint(mouseX,mouseY):
                if _value.wazatype[_value.ka3]!=0 or _value.ka4!=3:
                    mouseka4=i+1
        
        if _value.ka4==1:
            mouseka4_2=_value.wazatype[_value.ka3]
            text = _value.font.render("近距離", False, (100,100,100))
            text_rect = text.get_rect(center=(450, 150))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka4_2=0
            text = _value.font.render("遠距離", False, (100,100,100))
            text_rect = text.get_rect(center=(550, 150))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka4_2=1
            text = _value.font.render("突進", False, (100,100,100))
            text_rect = text.get_rect(center=(640, 150))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka4_2=2
        if _value.ka4==2:
            mouseka4_2=0
            if _value.wazatype[_value.ka3]==0:
                text = _value.font.render("攻撃範囲→", False, (0,0,0))
            else:
                text = _value.font.render("軌道→", False, (0,0,0))
            text_rect = text.get_rect(center=(470, 200))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka4_2=1
        if _value.ka4==3 and _value.wazatype[_value.ka3]!=0:
            mouseka4_2=_value.wazapene[_value.ka3]
            text = _value.font.render("停止", False, (100,100,100))
            text_rect = text.get_rect(center=(450, 250))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka4_2=0

            text = _value.font.render("反射", False, (100,100,100))
            text_rect = text.get_rect(center=(550, 250))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka4_2=1

            if _value.wazatype[_value.ka3]==1:
                text = _value.font.render("貫通", False, (100,100,100))
                text_rect = text.get_rect(center=(640, 250))
                if text_rect.collidepoint(mouseX,mouseY):
                    mouseka4_2=2
        if _value.ka4==4:
            mouseka4_2=_value.wazatuka[_value.ka3]
            text = _value.font.render("無視", False, (100,100,100))
            text_rect = text.get_rect(center=(550, 300))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka4_2=0

            text = _value.font.render("受ける", False, (100,100,100))
            text_rect = text.get_rect(center=(650, 300))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka4_2=1
        if _value.ka4==7:
            mouseka4_2=0
            text = _value.font.render("反動→", False, (0,0,0))
            text_rect = text.get_rect(center=(450, 450))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka4_2=1
        if _value.ka4==8:
            mouseka4_2=0
            text = _value.font.render("デザイン→", False, (0,0,0))
            text_rect = text.get_rect(center=(470, 500))
            if text_rect.collidepoint(mouseX,mouseY):
                mouseka4_2=1
        if _value.ka4==9:
            mouseka4_2=_value.wazatame[_value.ka3]
            if _value.ka3<10:
                text = _value.font.render("押した時", False, (100,100,100))
                text_rect = text.get_rect(center=(550, 550))
                if text_rect.collidepoint(mouseX,mouseY):
                    mouseka4_2=0

                text = _value.font.render("離した時", False, (100,100,100))
                text_rect = text.get_rect(center=(690, 550))
                if text_rect.collidepoint(mouseX,mouseY):
                    mouseka4_2=1
        




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

        _value.mouseclick=0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:     #
                _value.mouseclick=1               #
            if _value.help==0:                           #
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if x<mouseX<80+x and y<mouseY<40+y:
                            #保存
                            _value.stepbefore=4
                            _value.step=9
                        if x+100<mouseX<x+200 and y<mouseY<y+40:
                            _value.stepbefore=4
                            _value.step=7
                        if 50<mouseX<130 and y+y2<mouseY<y+40+y2:
                            _value.step=3
                        

                        if _value.ka4==1:
                            _value.wazatype[_value.ka3]=mouseka4_2
                        if _value.ka4==2:
                            if mouseka4_2==1:_value.step=5
                        if _value.ka4==3 and _value.wazatype[_value.ka3]!=0:
                            _value.wazapene[_value.ka3]=mouseka4_2
                        if _value.ka4==4:
                            _value.wazatuka[_value.ka3]=mouseka4_2
                        if _value.ka4==7:
                            if mouseka4_2==1:_value.step=6
                        if _value.ka4==8:
                            if mouseka4_2==1:_value.step=8
                        if _value.ka4==9:
                            _value.wazatame[_value.ka3]=mouseka4_2

                        if mouseka4!=-1:
                            if _value.ka4==mouseka4:
                                1
                            _value.ka4=mouseka4
                    if event.button == 4:
                        _value.ka4-=1
                        if _value.ka4<1:_value.ka4=1
                        if _value.wazatype[_value.ka3]==0 and _value.ka4==3:
                            _value.ka4=2
                    if event.button == 5:
                        if _value.ka4>0:
                            _value.ka4+=1
                            if _value.ka4>_value.tab4:
                                _value.ka4=_value.tab4
                            if _value.wazatype[_value.ka3]==0 and _value.ka4==3:
                                _value.ka4=4
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
                            if event.key!=pygame.K_RETURN and _value.title_len[_value.ka3]<14:
                                if _value.ka3%10==8:
                                    if event.key == pygame.K_w:
                                        _value.title += "↑"
                                    if event.key == pygame.K_a:
                                        _value.title += "←"
                                    if event.key == pygame.K_s:
                                        _value.title += "↓"
                                    if event.key == pygame.K_d:
                                        _value.title += "→"
                                    if event.key == pygame.K_RSHIFT:
                                        _value.title += "B"
                                    if event.key == pygame.K_RIGHTBRACKET:
                                        _value.title += "Y"
                                else:
                                    _value.title += event.unicode
                        
                        _value.title_len[_value.ka3]=len(_value.title)
                        if event.key==pygame.K_RETURN:
                            _value.active=False
                            _value.color = _value.color_active if _value.active else _value.color_inactive
                            _value.title_list[_value.ka3%10] = _value.title
                    if event.key == pygame.K_ESCAPE:
                        _value.step=3
                    if event.key == pygame.K_UP:
                        _value.ka4-=1
                        if _value.wazatype[_value.ka3]==0 and _value.ka4==3:
                            _value.ka4=2
                    if event.key == pygame.K_DOWN:
                        if _value.title=="" or _value.ka4>0:
                            _value.ka4+=1
                            if _value.ka4>_value.tab4:
                                _value.ka4=_value.tab4
                            if _value.wazatype[_value.ka3]==0 and _value.ka4==3:
                                _value.ka4=4
                    if event.key==pygame.K_RETURN:
                        if _value.ka4==2:
                            _value.step=5
                        elif _value.ka4==7:
                            _value.step=6
                        elif _value.ka4==8:
                            _value.step=8
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
                            if _value.wazatame[_value.ka3]>1 and _value.ka3<10:_value.wazatame[_value.ka3]=1
                    if event.key==pygame.K_LEFT:
                        if _value.ka4==1:
                            _value.wazatype[_value.ka3]-=1
                            if _value.wazatype[_value.ka3]<0:_value.wazatype[_value.ka3]=0
                            if _value.wazapene[_value.ka3]==2:_value.wazapene[_value.ka3]=1
                        if _value.ka4==3 and _value.wazatype[_value.ka3]!=0:
                            _value.wazapene[_value.ka3]-=1
                            if _value.wazapene[_value.ka3]<0:_value.wazapene[_value.ka3]=0
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
                            if _value.ka3>=30:
                                if _value.wazatame[_value.ka3]<_value.wazatame[_value.ka3-10]:_value.wazatame[_value.ka3]=_value.wazatame[_value.ka3-10]
        class Fakekeys:                           #
            def __getitem__(self, key):           #
                return False                      #

        if _value.help==0:                        #
            pressed_keys = pygame.key.get_pressed()
        else:                                     #
            pressed_keys = Fakekeys()             #
            
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
            font = pygame.font.SysFont("hg正楷書体pro", 20)
            text = font.render("ぶつかったとき", False, (0,0,0))
            text_rect = text.get_rect(center=(480, 230))
            _value.screen.blit(text, text_rect)
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


        text = _value.font.render("慣性", False, (0,0,0))
        text_rect = text.get_rect(center=(450, 300))
        _value.screen.blit(text, text_rect)
        if _value.wazatuka[_value.ka3]==0:
            text = _value.font.render("無視", False, (0,0,0))
        else:
            text = _value.font.render("無視", False, (100,100,100))
        text_rect = text.get_rect(center=(550, 300))
        _value.screen.blit(text, text_rect)

        if _value.wazatuka[_value.ka3]==1:
            text = _value.font.render("受ける", False, (0,0,0))
        else:
            text = _value.font.render("受ける", False, (100,100,100))
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
        if _value.ka3<10:
            text = _value.font.render("発動", False, (0,0,0))
            text_rect = text.get_rect(center=(430, 550))
            _value.screen.blit(text, text_rect)
            if _value.wazatame[_value.ka3]==0:
                text = _value.font.render("押した時", False, (0,0,0))
            else:
                text = _value.font.render("押した時", False, (100,100,100))
            text_rect = text.get_rect(center=(550, 550))
            _value.screen.blit(text, text_rect)

            if _value.wazatame[_value.ka3]==1:
                text = _value.font.render("離した時", False, (0,0,0))
            else:
                text = _value.font.render("離した時", False, (100,100,100))
            text_rect = text.get_rect(center=(690, 550))
            _value.screen.blit(text, text_rect)

        if _value.ka3>=10:
            text = _value.font.render("溜め時間", False, (0,0,0))
            text_rect = text.get_rect(center=(470, 550))
            _value.screen.blit(text, text_rect)
            text = _value.font.render(str(_value.wazatame[_value.ka3])+"00ms", False, (0,0,0))
            text_rect = text.get_rect(center=(670, 550))
            _value.screen.blit(text, text_rect)

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

        _func.help(700,100,1,"名前を入れないと技として反映されないので、気を付けてください。逆に名前だけを消すことで一時的に技を削除することもできます。")
        time.sleep(0.01)
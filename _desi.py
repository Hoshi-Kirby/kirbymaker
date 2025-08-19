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

def step8():
        pygame.display.update()
        _value.screen.fill((200,200,255))
        mouseX, mouseY = pygame.mouse.get_pos()
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
        
        if _value.step2==0:
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
                text = _value.font.render("カービィ", False, fill)
                text_rect = text.get_rect(center=(500, 200))
                _value.screen.blit(text, text_rect)
                text = _value.font.render(str(_value.ka8_2[_value.ka3]), False, fill)
                text_rect = text.get_rect(center=(550, 230))
                _value.screen.blit(text, text_rect)
                if _value.erabuki[_value.ka3]==0:
                    text = _value.font.render("武器を消す", False, fill2)
                if _value.erabuki[_value.ka3]==1:
                    text = _value.font.render("武器を描く→", False, fill2)
                text_rect = text.get_rect(center=(500, 300))
                _value.screen.blit(text, text_rect)
            
            if _value.wazatype[_value.ka3]==1:
                tab=2
                if(_value.t2<10):
                    _func.settingkirby(100,298,1)
                if(10<=_value.t2<15):
                    _func.settingkirby(100,298,2)
                if(15<=_value.t2<20):
                    _func.settingkirby(100,298,3)
                if(20<=_value.t2):
                    _func.settingkirby(100,298,4)
                text = _value.font.render("カービィ", False, fill)
                text_rect = text.get_rect(center=(500, 200))
                _value.screen.blit(text, text_rect)
                text = _value.font.render(str(_value.ka8_2[_value.ka3]), False, fill)
                text_rect = text.get_rect(center=(550, 230))
                _value.screen.blit(text, text_rect)
                text = _value.font.render("飛び道具→", False, fill2)
                text_rect = text.get_rect(center=(500, 300))
                _value.screen.blit(text, text_rect)
                if _value.erabuki[_value.ka3]==0:
                    text = _value.font.render("武器を消す", False, fill3)
                if _value.erabuki[_value.ka3]==1:
                    text = _value.font.render("武器を描く→", False, fill3)
                text_rect = text.get_rect(center=(500, 400))
                _value.screen.blit(text, text_rect)
            if _value.wazatype[_value.ka3]==2:
                tab=1
                if(_value.t2<10):
                    _func.settingkirby(100,298,1)
                if(10<=_value.t2<15):
                    _func.settingkirby(100,298,2)
                if(15<=_value.t2<20):
                    _func.settingkirby(100,298,3)
                if(20<=_value.t2):
                    _func.settingkirby(100,298,4)
                text = _value.font.render("カービィ", False, fill)
                text_rect = text.get_rect(center=(500, 200))
                _value.screen.blit(text, text_rect)
                text = _value.font.render(str(_value.ka8_2[_value.ka3]), False, fill)
                text_rect = text.get_rect(center=(550, 230))
                _value.screen.blit(text, text_rect)
                if _value.erabuki[_value.ka3]==0:
                    text = _value.font.render("武器を消す", False, fill2)
                if _value.erabuki[_value.ka3]==1:
                    text = _value.font.render("武器を描く→", False, fill2)
                text_rect = text.get_rect(center=(500, 300))
                _value.screen.blit(text, text_rect)
        
        if _value.step2==1:
            _func.settingkirby(100,298,3)
            if _value.flip==0:
                image=_value.image1
            if _value.flip==1:
                image=_value.image2
            x=250
            y=50
            text=_value.font.render("裏", False, (0,0,0))
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

            pygame.draw.line(_value.screen,fill,(700+_value.bukix[_value.ka3]/1.5,400),(700+_value.bukix[_value.ka3]/1.5,500),3)
            pygame.draw.line(_value.screen,fill,(650,450+_value.bukiy[_value.ka3]/1.5),(750,450+_value.bukiy[_value.ka3]/1.5),3)
            pygame.draw.circle(_value.screen,(255,255,255),(700+_value.bukix[_value.ka3]/1.5,450+_value.bukiy[_value.ka3]/1.5),5)
        
        if _value.step2==2:
            _func.settingkirby(100,298,3)
            if _value.flip==0:
                image=_value.image3
            if _value.flip==1:
                image=_value.image4
            x=180
            y=40
            text=_value.font.render("裏", False, (0,0,0))
            text_rect = text.get_rect(center=(400, 550))
            _value.screen.blit(text, text_rect)
            for i in range(46):
                for i2 in range(45):
                    if _value.flip==0:
                        i3=i2
                    else:
                        i3=44-i2
                    fill=_func.bgr_to_rgb(image[i,i2])

                    if fill==(255,255,255):fill=_value.back
                    pygame.draw.rect(_value.screen,fill,(i3*10+x,i*10+y,10,10))
                    if i2*10+x<mouseX<i2*10+x+10 and i*10+y<mouseY<i*10+y+10:
                        _value.mx=i3
                        _value.my=i
            if mouseX<x or 450+x<mouseX or mouseY<y or 460+y<mouseY:
                _value.mx=-1
                _value.my=-1
            if _value.cr==255 and _value.cg==255 and _value.cb==255:
                fill=(254,254,254)
            else:
                fill=(_value.cr,_value.cg,_value.cb)
            
            if _value.t>_value.kzi[_value.ka3]*100:
                img1 = pygame.image.load(f"hado ({_value.ka3}).png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5*(1.02**(-_value.hados[_value.ka3])))
                _value.screen.blit(img1, (_value.kx+105+30-60*(1.02**(-_value.hados[_value.ka3])),_value.ky+282+30-60*(1.02**(-_value.hados[_value.ka3]))))

            pygame.draw.rect(_value.screen,fill,(700,100,20,20))
            pygame.draw.line(_value.screen,(255,0,0),(650,150),(750,150),3)
            pygame.draw.line(_value.screen,(0,255,0),(650,200),(750,200),3)
            pygame.draw.line(_value.screen,(0,0,255),(650,250),(750,250),3)
            pygame.draw.circle(_value.screen,(255,255,255),(650+_value.cr*100/255,150),5)
            pygame.draw.circle(_value.screen,(255,255,255),(650+_value.cg*100/255,200),5)
            pygame.draw.circle(_value.screen,(255,255,255),(650+_value.cb*100/255,250),5)

            pygame.draw.line(_value.screen,fill,(700,400),(700,500),3)
            pygame.draw.circle(_value.screen,(255,255,255),(700,450+_value.hados[_value.ka3]),5)



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if _value.step2==0:
                    if event.key==pygame.K_RIGHT:
                        if _value.ka8==0:
                            _value.ka8_2[_value.ka3]+=1
                            if _value.ka8_2[_value.ka3]>17:_value.ka8_2[_value.ka3]=17
                        if (_value.wazatype[_value.ka3]==1 and _value.ka8==2)or(_value.wazatype[_value.ka3]!=1 and _value.ka8==1):
                            _value.erabuki[_value.ka3]=1
                    if event.key==pygame.K_LEFT:
                        if _value.ka8==0:
                            _value.ka8_2[_value.ka3]-=1
                            if _value.ka8_2[_value.ka3]<0:_value.ka8_2[_value.ka3]=0
                        if (_value.wazatype[_value.ka3]==1 and _value.ka8==2)or(_value.wazatype[_value.ka3]!=1 and _value.ka8==1):
                            _value.erabuki[_value.ka3]=0
                    if event.key==pygame.K_UP:
                        _value.ka8-=1
                        if _value.ka8<0:_value.ka8=0
                    if event.key==pygame.K_DOWN:
                        _value.ka8+=1
                        if _value.ka8>tab:_value.ka8=tab
                    if event.key==pygame.K_RETURN:
                        if _value.ka8==0:_value.ka8+=1
                        if (_value.wazatype[_value.ka3]==1 and _value.ka8==2)or(_value.wazatype[_value.ka3]!=1 and _value.ka8==1):
                            if _value.erabuki[_value.ka3]==1:_value.step2=1
                        if _value.wazatype[_value.ka3]==1 and _value.ka8==1:
                            _value.step2=2
                    if event.key==pygame.K_ESCAPE:
                        _value.step=4
                    if _value.step2==1:
                        if event.key == pygame.K_c:
                            for i in range(45):
                                for i2 in range(32):
                                    image[i,i2]=(255,255,255)
                    if _value.step2==2:
                        if event.key == pygame.K_c:
                            for i in range(46):
                                for i2 in range(45):
                                    image[i,i2]=(255,255,255)
                else:
                    if event.key==pygame.K_RETURN:
                        _value.step2=0
                    if event.key==pygame.K_ESCAPE:
                        _value.step2=0
            elif event.type == MOUSEBUTTONDOWN:
                if 350<mouseX<450 and 500<mouseY<600:
                    _value.flip=1-_value.flip
                if event.button == 1 and _value.step2>=1:  # 左クリック
                    _value.drag = 1
                if event.button == 3 and _value.step2>=1:  # 左クリック
                    _value.drag = 3
                    if _value.my>=0:
                        bgr = tuple(int(c) for c in image[_value.my, _value.mx])
                        fill = _func.bgr_to_rgb(bgr)
                        _value.cr,_value.cg,_value.cb=fill
                if event.button == 2 and _value.step2>=1:
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
                if _value.step2==1:
                    if _value.flip==0:
                        cv2.imwrite(f"buki ({_value.ka3}).png", image)
                        cv2.imwrite(f"buki2 ({_value.ka3}).png", image)
                        _value.image1 = image
                        _value.image2 = image
                    if _value.flip==1:
                        cv2.imwrite(f"buki2 ({_value.ka3}).png", image)
                        _value.image2 = image
                if _value.step2==2:
                    if _value.flip==0:
                        cv2.imwrite(f"hado ({_value.ka3}).png", image)
                        cv2.imwrite(f"hado2 ({_value.ka3}).png", image)
                        _value.image3 = image
                        _value.image4 = image
                    if _value.flip==1:
                        cv2.imwrite(f"hado2 ({_value.ka3}).png", image)
                        _value.image4 = image
            if 650<mouseX<750 and 140<mouseY<160:
                _value.cr=(mouseX-650)*2.55
            if 650<mouseX<750 and 190<mouseY<210:
                _value.cg=(mouseX-650)*2.55
            if 650<mouseX<750 and 240<mouseY<260:
                _value.cb=(mouseX-650)*2.55

            if _value.step2==1:
                if 650<mouseX<750 and 400<mouseY<500:
                    _value.bukix[_value.ka3]=(mouseX-700)*1.5
                    _value.bukiy[_value.ka3]=(mouseY-450)*1.5
            if _value.step2==2:
                if 680<mouseX<720 and 400<mouseY<500:
                    _value.hados[_value.ka3]=(mouseX-700)
                    _value.hados[_value.ka3]=(mouseY-450)
        if _value.drag==3:
            if _value.my>=0:
                image[_value.my,_value.mx]=[255,255,255]
                if _value.step2==1:
                    if _value.flip==0:
                        cv2.imwrite(f"buki ({_value.ka3}).png", image)
                        cv2.imwrite(f"buki2 ({_value.ka3}).png", image)
                        _value.image1 = image
                        _value.image2 = image
                    if _value.flip==1:
                        cv2.imwrite(f"buki2 ({_value.ka3}).png", image)
                        _value.image2 = image
                if _value.step2==2:
                    if _value.flip==0:
                        cv2.imwrite(f"hado ({_value.ka3}).png", image)
                        cv2.imwrite(f"hado2 ({_value.ka3}).png", image)
                        _value.image3 = image
                        _value.image4 = image
                    if _value.flip==1:
                        cv2.imwrite(f"hado2 ({_value.ka3}).png", image)
                        _value.image4 = image
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

        time.sleep(0.01)
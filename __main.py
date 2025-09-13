import sys, random
import pygame, time
import cv2
import numpy as np
from pygame.locals import *
pygame.init()
pygame.mixer.init()


import _func
import _value
import _title
import _appe
import _skill
import _deta
import _orbit
import _reco
import _test
import _desi
import _savedata
import _name
import _save
import _load

pygame.display.set_caption("k")


pygame.mixer.init()

while True:
    if _value.step==1:
        _value.kx=225
        _value.ky=_value.ground
        _value.ka=0
        _value.ka3=0
        _value.t=0

        _value.buki=0
        _value.bosi=0
        _value.title_list = [""]*(_value.tab+20)
        _value.title_len = [0]*(_value.tab+20)
        _value.wazatype=[0]*(_value.tab+20)
        _value.kx2=[0]*(_value.tab+20)
        _value.kx1=[0]*(_value.tab+20)
        _value.kx0=[0]*(_value.tab+20)
        _value.ky2=[0]*(_value.tab+20)
        _value.ky1=[0]*(_value.tab+20)
        _value.ky0=[0]*(_value.tab+20)
        _value.kzi=[0]*(_value.tab+20)
        _value.kzi2=[1]*(_value.tab+20)
        _value.kad2=[0]*(_value.tab+20)
        _value.kws2=[0]*(_value.tab+20)
        _value.kad1=[0]*(_value.tab+20)
        _value.kws1=[0]*(_value.tab+20)
        _value.kx2h=[0]*(_value.tab+20)
        _value.kx1h=[0]*(_value.tab+20)
        _value.kx0h=[0]*(_value.tab+20)
        _value.ky2h=[0]*(_value.tab+20)
        _value.ky1h=[0]*(_value.tab+20)
        _value.ky0h=[0]*(_value.tab+20)
        _value.kzih=[0.1]*(_value.tab+20)
        _value.kad2h=[0]*(_value.tab+20)
        _value.kws2h=[0]*(_value.tab+20)
        _value.kad1h=[0]*(_value.tab+20)
        _value.kws1h=[0]*(_value.tab+20)
        _value.kds=[0]*(_value.tab+20)
        _value.kkk=[0]*(_value.tab+20)
        
        _value.wazapene=[0]*(_value.tab+20)
        _value.wazatuka=[0]*(_value.tab+20)
        _value.wazadame=[0]*(_value.tab+20)
        _value.wazahuto=[0]*(_value.tab+20)
        _value.wazatame=[0]*(_value.tab+20)
        _value.ka8_2=[0]*(_value.tab+20)
        _value.bukix=[-34.7]*(_value.tab+20)
        _value.bukiy=[-52.8]*(_value.tab+20)
        _value.hados=[0]*(_value.tab+20)
        _value.erabuki=[0]*(_value.tab+20)
        image = cv2.imread(r"C:\python\kirby\h.png")
        cv2.imwrite("buki.png", image)
        cv2.imwrite("buki2.png", image)
        for i in range(30):
            cv2.imwrite(f"buki ({i}).png", image)
            cv2.imwrite(f"buki2 ({i}).png", image)
        image = cv2.imread(r"C:\python\kirby\s.png")
        for i in range(30):
            cv2.imwrite(f"hado ({i}).png", image)
            cv2.imwrite(f"hado2 ({i}).png", image) 

        _value.ka8=0
        pygame.mixer.music.stop()
        pygame.mixer.music.load("title.mp3")
        pygame.mixer.music.play(-1)

    while _value.step==1:

        _title.step1()

    # 新規作成
    if _value.step==2:
        _value.ka=0
        _value.esch=0
        _value.step2=0
        _value.drag=0
        _value.cr=255
        _value.cg=255
        _value.cb=255
        _value.mx=-1
        _value.my=-1
        _value.back=(255,255,255)
        _value.drag=0
        _value.flip=0
        _value.image1=cv2.imread(r"C:\python\kirby\buki.png")
        _value.image2=cv2.imread(r"C:\python\kirby\buki2.png")
        pygame.mixer.music.stop()
        pygame.mixer.music.load("setting.mp3")
        pygame.mixer.music.play(-1)
    while _value.step==2:

        _appe.step2()
                    
    # 変更する技選択
    while _value.step==3:
        
        _skill.step3()
    
    # わざせってい
    if _value.step==4:
        _value.ka4=1
        _value.input_box = pygame.Rect(50, 80, 400, 40)
        _value.color_inactive = pygame.Color(0,0,0)
        _value.color_active = pygame.Color(150,50,50)
        _value.color = _value.color_inactive
        _value.active = False
        _value.title = _value.title_list[_value.ka3%10]
        
        _value.ws=0
        _value.t=0
        _value.ad=0
        _value.kx=_value.kx0[_value.ka3]*50
        _value.ky=_value.ky0[_value.ka3]*50
        _value.kxv=_value.kx1[_value.ka3]
        _value.kyv=_value.ky1[_value.ka3]

        _value.running = True
        
        _value.tab4=9


    while _value.step==4:
        
        _deta.step4()

    # 攻撃範囲、軌道
    if _value.step==5:
        if _value.wazatype[_value.ka3]==0:
            _value.box_rects = [pygame.Rect(371+i*95, 185, 40, 30) for i in range(5)]
            _value.box_rects[4]=pygame.Rect(485, 385, 40, 30)
        else:
            _value.box_rects = [pygame.Rect(371+i*100, 185, 40, 30) for i in range(14)]
            for i in range(3):
                _value.box_rects[i+3]=pygame.Rect(371+i*100, 385, 40, 30)
            for i in range(2):
                _value.box_rects[i+6]=pygame.Rect(651+i*80, 385, 40, 30)
            for i in range(2):
                _value.box_rects[i+8]=pygame.Rect(371+i*100, 235, 40, 30)
            for i in range(2):
                _value.box_rects[i+10]=pygame.Rect(371+i*100, 435, 40, 30)
            for i in range(2):
                _value.box_rects[i+12]=pygame.Rect(401+i*200, 85, 40, 30)
            
        active=[False]*14
        _value.input_text=["0"]*14
        if _value.wazatype[_value.ka3]==0:
            _value.input_text[0]=str(_value.kx2[_value.ka3])
            _value.input_text[1]=str(_value.kx1[_value.ka3])
            _value.input_text[2]=str(_value.kx0[_value.ka3])
            _value.input_text[3]=str(_value.ky2[_value.ka3])
            _value.input_text[4]=str(_value.kzi2[_value.ka3])
            _value.input_text[5]=str(_value.ky0[_value.ka3])
            _value.input_text[6]=str(_value.kzi[_value.ka3])
            _value.input_text[7]=str(_value.kzi2[_value.ka3])
            _value.input_text[8]=str(_value.kad2[_value.ka3])
            _value.input_text[9]=str(_value.kad1[_value.ka3])
            _value.input_text[10]=str(_value.kws2[_value.ka3])
            _value.input_text[11]=str(_value.kws1[_value.ka3])
            _value.input_text[12]=str(_value.kds[_value.ka3])
            _value.input_text[13]=str(_value.kkk[_value.ka3])
        else:
            _value.input_text[0]=str(_value.kx2[_value.ka3])
            _value.input_text[1]=str(_value.kx1[_value.ka3])
            _value.input_text[2]=str(_value.kx0[_value.ka3])
            _value.input_text[3]=str(_value.ky2[_value.ka3])
            _value.input_text[4]=str(_value.ky1[_value.ka3])
            _value.input_text[5]=str(_value.ky0[_value.ka3])
            _value.input_text[6]=str(_value.kzi[_value.ka3])
            _value.input_text[7]=str(_value.kzi2[_value.ka3])
            _value.input_text[8]=str(_value.kad2[_value.ka3])
            _value.input_text[9]=str(_value.kad1[_value.ka3])
            _value.input_text[10]=str(_value.kws2[_value.ka3])
            _value.input_text[11]=str(_value.kws1[_value.ka3])
            _value.input_text[12]=str(_value.kds[_value.ka3])
            _value.input_text[13]=str(_value.kkk[_value.ka3])

        _value.ka5=0
        _value.ws=0
        _value.ad=0
        _value.kx=_value.kx0[_value.ka3]*50
        _value.ky=_value.ky0[_value.ka3]*50
        _value.kxv=_value.kx1[_value.ka3]
        _value.kyv=_value.ky1[_value.ka3]

        if _value.wazatype[_value.ka3]==1:
            _value.tab5=13
        if _value.wazatype[_value.ka3]==2:
            _value.tab5=11
        if _value.wazatype[_value.ka3]==0:
            _value.tab5=5
    while _value.step==5:
        _orbit.step5()

    if _value.step==6:
        _value.box_rects = [pygame.Rect(371+i*100, 185, 40, 30) for i in range(11)]
        for i in range(4):
            _value.box_rects[i+3]=pygame.Rect(371+i*100, 385, 40, 30)
        for i in range(2):
            _value.box_rects[i+7]=pygame.Rect(371+i*100, 235, 40, 30)
        for i in range(2):
            _value.box_rects[i+9]=pygame.Rect(371+i*100, 435, 40, 30)
            
        active=[False]*14
        _value.input_text=["0"]*14
        _value.input_text[0]=str(_value.kx2h[_value.ka3])
        _value.input_text[1]=str(_value.kx1h[_value.ka3])
        _value.input_text[2]=str(_value.kx0h[_value.ka3])
        _value.input_text[3]=str(_value.ky2h[_value.ka3])
        _value.input_text[4]=str(_value.ky1h[_value.ka3])
        _value.input_text[5]=str(_value.ky0h[_value.ka3])
        _value.input_text[6]=str(_value.kzih[_value.ka3])
        _value.input_text[7]=str(_value.kad2h[_value.ka3])
        _value.input_text[8]=str(_value.kad1h[_value.ka3])
        _value.input_text[9]=str(_value.kws2h[_value.ka3])
        _value.input_text[10]=str(_value.kws1h[_value.ka3])

        _value.ka6=0
        _value.ws=0
        _value.ad=0
        _value.kx=_value.kx0h[_value.ka3]*50
        _value.ky=_value.ky0h[_value.ka3]*50
        _value.kxv=_value.kx1h[_value.ka3]
        _value.kyv=_value.ky1h[_value.ka3]
        if _value.ka3>=20:
            if _value.wazatame[_value.ka3]<_value.wazatame[_value.ka3-10]:
                _value.wazatame[_value.ka3]=_value.wazatame[_value.ka3-10]
    while _value.step==6:
        _reco.step6()
        
    #テストプレイ
    if _value.step==7:

        _value.kxtest=225
        _value.kytest=_value.ground
        _value.t=-1
        _value.t2=-1
        _value.kxtestv=0
        _value.kytestv=0
        _value.skillnum=-1
        _value.ttest=0
        _value.hando=0
        
    while _value.step==7:
        _test.step7()

    # デザイン
    if _value.step==8:
        a=0
        ka8=0
        _value.flip=0
        _value.image1=cv2.imread(rf"C:\python\kirby\buki ({_value.ka3}).png")
        _value.image2=cv2.imread(rf"C:\python\kirby\buki2 ({_value.ka3}).png")
        _value.image3=cv2.imread(rf"C:\python\kirby\hado ({_value.ka3}).png")
        _value.image4=cv2.imread(rf"C:\python\kirby\hado2 ({_value.ka3}).png")
        
    while _value.step==8:
        _desi.step8()
    
    #保存
    if _value.step==9:
        _value.savestep=0
        _name.nameload()
    while _value.step==9:
        while _value.savestep==0:
            _savedata.savedata()
        
        if _value.savestep==1:
            if _value.nameload[_value.ka9]=="データなし":
                _value.title=""
            else:
                _value.title=_value.nameload[_value.ka9]
        while _value.savestep==1:
            _name.name()

        if _value.savestep==2:
            if _value.nameload[_value.ka9]=="データなし":
                _value.savestep=3
        
        if _value.savestep==2:
            _save.savebb()
        while _value.savestep==2:
            _save.saveb()

        if _value.savestep==3:
            _save.save()
            _value.se_1up.play()
        while _value.savestep==3:
            _save.savea()
    
    #ロード
    if _value.step==10:
        _value.loadstep=0
        _name.nameload()
        pygame.mixer.music.stop()
        pygame.mixer.music.load("select.mp3")
        pygame.mixer.music.play(-1)
    while _value.step==10:
        while _value.loadstep==0:
            _load.loaddata()
        while _value.loadstep==1:
            _load.loadb()
        if _value.loadstep==2:
            _load.load()
            _value.se_copy.play()
        while _value.loadstep==2:
            _load.loada()
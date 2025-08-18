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

def step7():
        pygame.display.update()
        
        _value.screen.fill((200,200,255))

        
        text = _value.font.render("編集", False, (0,0,0))
        text_rect = text.get_rect(center=(700, 30))
        _value.screen.blit(text, text_rect)

        
        if _value.kytest==_value.ground: _value.hob=0
        # 終了イベントを確認 --- (*5)
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if _value.t==-1 or (_value.t>=0 and _value.wazatuka[_value.skillnum]==1):
                    command=""
                    command2=""
                    if event.key == K_RETURN and _value.skilltime==-1:
                        if _value.kytest<_value.ground:
                            if _value.hobfc==0:
                                _value.hob=1
                                _value.hobc=18
                                _value.kytestv=-2.7
                        else:
                            if _value.shagam==1:
                                if _value.sura==0:
                                    _value.sura=50
                            else:
                                _value.kytestv=-6
                        if 620<_value.kxtest<730 and -10<_value.kytest<40:
                            _value.step=3
                    if event.key == K_a and _value.skaih==0 and _value.kaih==0 and _value.sura==0:
                        _value.flip=1
                        command="←"
                        command2="→"
                        if _value.guard==1:
                            _value.kaih=30
                    if event.key == K_d and _value.skaih==0 and _value.kaih==0 and _value.sura==0:
                        _value.flip=0
                        command="→"
                        command2="←"
                        if _value.guard==1:
                            _value.kaih=30
                    if event.key == K_w and _value.sura==0:
                        command=command2="↑"
                    if event.key == K_s and _value.sura==0:
                        command=command2="↓"
                        if _value.guard==1 and _value.skaih==0 and _value.kaih==0 and _value.sura==0:
                            _value.skaih=30
                    if event.key == K_RSHIFT and _value.sura==0:
                        command=command2="B"
                    if event.key == K_RIGHTBRACKET and _value.sura==0:
                        command = command2 = "Y"
                    
                    if _value.comt<_value.title_len[8]:
                        if _value.title_list[8][int(_value.comt)]==command:
                            if _value.comt<_value.title_len[8]-1:
                                _value.comt=_value.comt//1+2
                            else:
                                _value.comt=0
                                _value.skillnum=8
                                _func.skill(8)
                    if _value.comtr<_value.title_len[8]:
                        if _value.title_list[8][int(_value.comtr)]==command2:
                            if _value.comtr<_value.title_len[8]-1:
                                _value.comtr=_value.comtr//1+2
                            else:
                                _value.comtr=0
                                _value.skillnum=8
                                _func.skill(8)

                if _value.t==-1:
                    if event.key==K_RSHIFT and _value.t==-1 and _value.skillnum==-1:
                        if _value.hob==0:
                            if (pressed_keys[K_a] or pressed_keys[K_d])and _value.title_list[7]!="" and _value.kytest>_value.ground:
                                _value.skillnum=7
                            elif (pressed_keys[K_a] or pressed_keys[K_d])and _value.title_list[3]!="":
                                _value.skillnum=3
                            elif pressed_keys[K_s]and _value.title_list[6]!="" and _value.kytest<_value.ground:
                                _value.skillnum=6
                            elif pressed_keys[K_s]and _value.title_list[2]!="":
                                _value.skillnum=2
                            elif pressed_keys[K_w]and _value.title_list[5]!="" and _value.kytest<_value.ground:
                                _value.skillnum=5
                            elif pressed_keys[K_w]and _value.title_list[1]!="":
                                _value.skillnum=1
                            elif _value.title_list[4]!="" and _value.kytest<_value.ground:
                                _value.skillnum=4
                            elif _value.title_list[0]!="":
                                _value.skillnum=0
                            else:
                                _value.skillnum=-1
                            if _value.skillnum>=0:
                                if _value.wazatame[_value.skillnum]==0:
                                    _func.skill(_value.skillnum)
                                _value.skilltime=0
                if event.key == pygame.K_ESCAPE:
                    _value.step=3
            if event.type == KEYUP:
                if event.key == K_RSHIFT:
                    if 0<=_value.skillnum<9 and _value.skilltime>=0:
                        if _value.wazatame[_value.skillnum+20]<=_value.skilltime and _value.wazatame[_value.skillnum+20]>0:
                            _func.skill(_value.skillnum+20)
                        elif _value.wazatame[_value.skillnum+10]<=_value.skilltime and _value.wazatame[_value.skillnum+10]>0:
                            _func.skill(_value.skillnum+10)
                        elif _value.wazatame[_value.skillnum]==1:
                            _func.skill(_value.skillnum)
                    _value.skilltime=-1
            #
            
        # 
        if _value.kaih==0 and _value.skaih==0 and _value.sura==0:
            if (pressed_keys[K_d] or pressed_keys[K_a]) and _value.hobfc==0 and _value.skilltime==-1:
                _value.posetime+=1
                if _value.posetime==6:
                    _value.posetime=0
                    _value.pose+=1
                    if _value.pose==9:
                        _value.pose=1
                if pressed_keys[K_d]:
                    _value.flip=0
                    if _value.hob==1:
                        _value.kxtestv=1.5
                        if _value.kxtestv>1.5:
                            _value.kxtestv=1.5
                    else:
                        if _value.t>0:
                            _value.ad=1
                        #反動ないなら
                        if _value.t==-1 or (_value.t>=0 and _value.wazatuka[_value.skillnum]==1):
                            _value.kxtestv+=2
                        if _value.kxtestv>2:
                            _value.kxtestv=2
                    if _value.kxtest>750:
                        _value.kxtest=750
                if pressed_keys[K_a]:
                    _value.flip=1
                    if _value.hob==1:
                        _value.kxtestv-=1.5
                        if _value.kxtestv<-1.5:
                            _value.kxtestv=-1.5
                    else:
                        if _value.t>0:
                            _value.ad=-1
                        #反動ないなら
                        if _value.t==-1 or (_value.t>=0 and _value.wazatuka[_value.skillnum]==1):
                            _value.kxtestv-=2
                        if _value.kxtestv<-2:
                            _value.kxtestv=-2
                    if _value.kxtest<0:
                        _value.kxtest=0
            else:
                _value.pose=0

            if pressed_keys[K_RSHIFT] and _value.hobfc==0:
                if _value.hob==1:
                    _value.hob=0
                    _value.hobfc=10
            
            
            if pressed_keys[K_w]:
                if _value.t>0:_value.ws=-1

            if pressed_keys[K_s] and _value.kytest==_value.ground and _value.guard==0:
                if _value.t>0:
                    _value.ws=1
                if _value.t==-1 or (_value.t>=0 and _value.wazatuka[_value.skillnum]==1):
                    _value.shagam=1
            else:
                _value.shagam=0

        if _value.kaih>0 and _value.kytest==_value.ground:
            if _value.flip==1:
                _value.kxtest-=_value.kaih/3
                if _value.kxtest<0:
                    _value.kxtest=0
            else:
                _value.kxtest+=_value.kaih/3    
                if _value.kxtest>750:
                    _value.kxtest=750
        if _value.sura>6 and _value.kytest==_value.ground:
            if _value.flip==1:
                _value.kxtestv=-2
                if _value.kxtest<0:

                    _value.kxtest=0
            else:
                _value.kxtestv=2   
                if _value.kxtest>750:
                    _value.kxtest=750
        if 0<_value.sura<=6 and _value.kytest==_value.ground:
            if _value.flip==1:
                _value.kxtestv=-0.5
                if _value.kxtest<0:
                    _value.kxtest=0
            else:
                _value.kxtestv=0.5
                if _value.kxtest>750:
                    _value.kxtest=750
    
        #慣性
        if _value.t>=0 and _value.wazatuka[_value.skillnum]==0:
            _value.kxtestv=0
            _value.kytestv=0

        _value.kxtest+=_value.kxtestv
        if _value.kxtest>750:_value.kxtest=750
        if _value.kxtest<0:_value.kxtest=0
        if _value.kytestv>0 and _value.hob==0:_value.kxtestv=0
        if _value.kytestv==0:
            if _value.kxtestv>0.1:
                _value.kxtestv-=0.1
            elif _value.kxtestv<-0.1:
                _value.kxtestv+=0.1
            else:
                _value.kxtestv=0
        if _value.kytestv>=0 and _value.hob==1:
            if _value.kxtestv>0.05:
                _value.kxtestv-=0.05
            elif _value.kxtestv<-0.05:
                _value.kxtestv+=0.05
            else:
                _value.kxtestv=0
        
        if _value.kytest>=_value.ground and _value.kytestv>=0:
            _value.kytestv=0
        else:     
            # 落下の加速度
            if _value.t==-1 or _value.wazatuka[_value.skillnum]==1:
                if _value.hob==1:
                    _value.kytestv+=0.08
                    if _value.kytestv>1.4:_value.kytestv=1.4
                else:
                    if _value.hobfc<5:
                        _value.kytestv+=0.2
                        if _value.kytestv>6:_value.kytestv=6
        _value.kytest+=_value.kytestv
        if _value.kytest>_value.ground:
            _value.kytest=_value.ground
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
            _value.kytestv=-1
        else:
            _value.skaih=0
        if _value.sura>0:
            _value.sura-=1
        else:
            _value.sura=0
        if _value.skilltime>=0:
            _value.skilltime+=0.1
        else:
            _value.skilltime=-1
        if _value.comt>0:
            _value.comt-=0.01
        else:
            _value.comt=0
        if _value.comtr>0:
            _value.comtr-=0.01
        else:
            _value.comtr=0
        if _value.comt%1<0.9:
            _value.comt=0
        if _value.comtr%1<0.9:
            _value.comtr=0
        _value.kxh=0
        _value.kyh=0
        bxh=0
        byh=0
        if 0<_value.t2<25:
            if(0<=_value.t2<10):
                _func.skillkirby(_value.kxtest,_value.kytest,1)
            if(10<=_value.t2<15):
                _func.skillkirby(_value.kxtest,_value.kytest,2)
            if(15<=_value.t2<20):
                _func.skillkirby(_value.kxtest,_value.kytest,3)
            if(20<=_value.t2):
                _func.skillkirby(_value.kxtest,_value.kytest,4)
        elif _value.skilltime>=0:
            if _value.skillnum>=0:
                if _value.wazatame[_value.skillnum+20]<=_value.skilltime and _value.wazatame[_value.skillnum+20]>0:
                    _func.tamekirby(_value.kxtest,_value.kytest,_value.ttest,2)
                elif _value.wazatame[_value.skillnum+10]<=_value.skilltime and _value.wazatame[_value.skillnum+10]>0:
                    _func.tamekirby(_value.kxtest,_value.kytest,_value.ttest,1)
                else:
                    _func.tamekirby(_value.kxtest,_value.kytest,_value.ttest,0)
            else:
                _func.skillkirby(_value.kxtest,_value.kytest,1)
        else:

            if _value.pose==0:
                if _value.buki==0:
                    if _value.bosi==0:
                        img1 = pygame.image.load("ノーマルf.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("ノーマルfボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("ノーマルfファイター.png")
                if _value.buki==1:
                    if _value.bosi==0:
                        img1 = pygame.image.load("ノーマルh.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("ノーマルhボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("ノーマルhファイター.png")
                bxh=-2
            if _value.shagam==1:
                if _value.buki==0:
                    if _value.bosi==0:
                        img1 = pygame.image.load("しゃがみf.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("しゃがみfボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("しゃがみfファイター.png")
                if _value.buki==1:
                    if _value.bosi==0:
                        img1 = pygame.image.load("しゃがみh.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("しゃがみhボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("しゃがみhファイター.png")
                if _value.bosi==0:_value.kxh=-4
                if _value.bosi==1:_value.kxh=1
                if _value.bosi==2:_value.kxh=-2
                _value.kyh=22
                bxh=-2

            if _value.hob==0:
                if _value.pose==1:
                    if _value.bosi==0:
                        img1 = pygame.image.load("ダッシュ1.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("ダッシュ1ボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("ダッシュ1ファイター.png")
                    _value.kxh=0
                    _value.kyh=0
                if _value.pose==2:
                    if _value.bosi==0:
                        img1 = pygame.image.load("ダッシュ2.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("ダッシュ2ボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("ダッシュ2ファイター.png")
                    _value.kxh=0
                    _value.kyh=0
                if _value.pose==3:
                    if _value.bosi==0:
                        img1 = pygame.image.load("ダッシュ3.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("ダッシュ3ボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("ダッシュ3ファイター.png")
                    _value.kxh=0
                    _value.kyh=0
                    bxh=2
                if _value.pose==4:
                    if _value.bosi==0:
                        img1 = pygame.image.load("ダッシュ4.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("ダッシュ4ボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("ダッシュ4ファイター.png")
                    _value.kxh=0
                    _value.kyh=0
                    bxh=8
                if _value.pose==5:
                    if _value.bosi==0:
                        img1 = pygame.image.load("ダッシュ5.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("ダッシュ5ボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("ダッシュ5ファイター.png")
                    _value.kxh=0
                    _value.kyh=0
                    bxh=7
                if _value.pose==6:
                    if _value.bosi==0:
                        img1 = pygame.image.load("ダッシュ6.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("ダッシュ6ボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("ダッシュ6ファイター.png")
                    _value.kxh=0
                    _value.kyh=0
                    bxh=4
                if _value.pose==7:
                    if _value.bosi==0:
                        img1 = pygame.image.load("ダッシュ7.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("ダッシュ7ボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("ダッシュ7ファイター.png")
                    _value.kxh=0
                    _value.kyh=0
                    bxh=2
                if _value.pose==8:
                    if _value.bosi==0:
                        img1 = pygame.image.load("ダッシュ8.png")
                    if _value.bosi==1:
                        img1 = pygame.image.load("ダッシュ8ボム.png")
                    if _value.bosi==2:
                        img1 = pygame.image.load("ダッシュ8ファイター.png")
                    _value.kxh=0
                    _value.kyh=0
            
            if _value.kytestv<0:
                if _value.bosi==0:
                    img1 = pygame.image.load("ジャンプ上.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ジャンプ上ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ジャンプ上ファイター.png")
            if _value.kytestv>0:
                if _value.bosi==0:
                    img1 = pygame.image.load("ジャンプ下.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("ジャンプ下ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("ジャンプ下ファイター.png")



            if _value.hob==1:
                if _value.buki==0:
                    if _value.bosi==0:
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
                    if _value.bosi==1:
                        if _value.hobc>0:
                            img1 = pygame.image.load("ホバリングf5ボム.png")
                        if _value.hobc>2:
                            img1 = pygame.image.load("ホバリングf4ボム.png")
                        if _value.hobc>4:
                            img1 = pygame.image.load("ホバリングf3ボム.png")
                        if _value.hobc>8:
                            img1 = pygame.image.load("ホバリングf2ボム.png")
                        if _value.hobc>16:
                            img1 = pygame.image.load("ホバリングf1ボム.png")
                        if _value.hobc==0:
                            img1 = pygame.image.load("ホバリングf1ボム.png")
                    if _value.bosi==2:
                        if _value.hobc>0:
                            img1 = pygame.image.load("ホバリングf5ファイター.png")
                        if _value.hobc>2:
                            img1 = pygame.image.load("ホバリングf4ファイター.png")
                        if _value.hobc>4:
                            img1 = pygame.image.load("ホバリングf3ファイター.png")
                        if _value.hobc>8:
                            img1 = pygame.image.load("ホバリングf2ファイター.png")
                        if _value.hobc>16:
                            img1 = pygame.image.load("ホバリングf1ファイター.png")
                        if _value.hobc==0:
                            img1 = pygame.image.load("ホバリングf1ファイター.png")
                if _value.buki==1:
                    if _value.bosi==0:
                        if _value.hobc>0:
                            img1 = pygame.image.load("ホバリングh5.png")
                        if _value.hobc>2:
                            img1 = pygame.image.load("ホバリングh4.png")
                        if _value.hobc>4:
                            img1 = pygame.image.load("ホバリングh3.png")
                        if _value.hobc>8:
                            img1 = pygame.image.load("ホバリングh2.png")
                        if _value.hobc>16:
                            img1 = pygame.image.load("ホバリングh1.png")
                        if _value.hobc==0:
                            img1 = pygame.image.load("ホバリングh1.png")
                    if _value.bosi==1:
                        if _value.hobc>0:
                            img1 = pygame.image.load("ホバリングh5ボム.png")
                        if _value.hobc>2:
                            img1 = pygame.image.load("ホバリングh4ボム.png")
                        if _value.hobc>4:
                            img1 = pygame.image.load("ホバリングh3ボム.png")
                        if _value.hobc>8:
                            img1 = pygame.image.load("ホバリングh2ボム.png")
                        if _value.hobc>16:
                            img1 = pygame.image.load("ホバリングh1ボム.png")
                        if _value.hobc==0:
                            img1 = pygame.image.load("ホバリングh1ボム.png")
                    if _value.bosi==2:
                        if _value.hobc>0:
                            img1 = pygame.image.load("ホバリングh5ファイター.png")
                        if _value.hobc>2:
                            img1 = pygame.image.load("ホバリングh4ファイター.png")
                        if _value.hobc>4:
                            img1 = pygame.image.load("ホバリングh3ファイター.png")
                        if _value.hobc>8:
                            img1 = pygame.image.load("ホバリングh2ファイター.png")
                        if _value.hobc>16:
                            img1 = pygame.image.load("ホバリングh1ファイター.png")
                        if _value.hobc==0:
                            img1 = pygame.image.load("ホバリングh1ファイター.png")
                _value.kxh=-4
                _value.kyh=-1
                byh=-2
            



            if 6>_value.sura>0:
                if _value.bosi==0:
                    img1 = pygame.image.load("スライディング3.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("スライディング3ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("スライディング3ファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = pygame.transform.scale_by(img1, 1)
                img1 = img1.convert_alpha()
                _value.kxh=-8
                _value.kyh=10
            if _value.sura>=6:
                if _value.bosi==0:
                    img1 = pygame.image.load("スライディング2.png")
                if _value.bosi==1:
                    img1 = pygame.image.load("スライディング2ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("スライディング2ファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = pygame.transform.scale_by(img1, 1)
                img1 = img1.convert_alpha()
                _value.kxh=-8
                _value.kyh=10
            if _value.sura>=20:
                if _value.bosi==1:
                    img1 = pygame.image.load("スライディング1ボム.png")
                if _value.bosi==2:
                    img1 = pygame.image.load("スライディング1ファイター.png")
                    img1.set_colorkey((255, 255, 255))
                    img1 = pygame.transform.scale_by(img1, 1)
                    img1 = img1.convert_alpha()
                    _value.kxh=-8
                    _value.kyh=10
                
            
            


            
            img1.set_colorkey((255, 255, 255))
            img1 = pygame.transform.scale_by(img1, 1)
            img1 = img1.convert_alpha()
            if _value.flip==1:
                img1=pygame.transform.flip(img1, True, False)
            img1 = pygame.transform.scale_by(img1, 2)
            _value.screen.blit(img1, (_value.kxtest+_value.kxh, _value.kytest+_value.kyh))

        if (_value.buki==1 and _value.t<10)or(_value.skillnum>=0 and _value.erabuki[_value.skillnum]==1 and _value.t2>=10):
            if _value.t2<10:
                if _value.flip==1:
                    img2 = pygame.image.load("buki2.png")
                else:
                    img2 = pygame.image.load("buki.png")
            else:
                if _value.flip==1:
                    img2 = pygame.image.load(f"buki2 ({_value.skillnum}).png")
                else:
                    img2 = pygame.image.load(f"buki ({_value.skillnum}).png")
            img2 = pygame.transform.scale_by(img2, 1.8)
            img2.set_colorkey((255, 255, 255))
            img2 = img2.convert_alpha()
            bxh-=20
            if _value.bosi==1:
                bxh+=6
                byh+=6
            if _value.t>=10:
                bxh+=(_value.bukix[_value.skillnum]+25)*0.72
                byh+=(_value.bukiy[_value.skillnum]+38)*0.72
            if _value.flip==1:
                bxh=-bxh
                bxh-=10
                img2=pygame.transform.flip(img2, True, False)
            
            _value.screen.blit(img2, (_value.kxtest+_value.kxh+bxh, _value.kytest-37+_value.kyh+byh))

        if _value.t>=0:_value.t+=1
        if _value.t2>=0:_value.t2+=1
        if _value.skillnum>=0 and _value.t>_value.kzi[_value.skillnum]*100:
            _value.t=-1
            _value.t2=-1
            _value.skillnum=-1
        if _value.t==-1:_value.flip2=_value.flip
        if _value.skillnum>=0 and _value.wazatype[_value.skillnum]>0:
            if _value.t>=0:
                _value.kxv+=_value.kx2[_value.skillnum]*0.05+_value.kad2[_value.skillnum]*_value.ad*0.01
                _value.kyv+=_value.ky2[_value.skillnum]*0.05+_value.kws2[_value.skillnum]*_value.ws*0.01
                # 遠距離
                if _value.wazatype[_value.skillnum]==1:
                    if _value.flip2==0:
                        img1 = pygame.image.load(f"hado ({_value.skillnum}).png")
                    else:
                        img1 = pygame.image.load(f"hado2 ({_value.skillnum}).png")
                    img1.set_colorkey((255, 255, 255))
                    img1 = img1.convert_alpha()
                    img1 = pygame.transform.scale_by(img1, 1.8*(1.02**(-_value.hados[_value.skillnum])))
                    if _value.flip2==0:
                        _value.kx+=_value.kxv+_value.kad1[_value.skillnum]*_value.ad*0.5
                    else:
                        img1=pygame.transform.flip(img1, True, False)
                        _value.kx-=_value.kxv+_value.kad1[_value.skillnum]*_value.ad*0.5
                    _value.ky+=_value.kyv+_value.kws1[_value.skillnum]*_value.ws*0.5
                    _value.screen.blit(img1, (_value.kx-7+21.6-43.2*(1.02**(-_value.hados[_value.skillnum])),_value.ky-16+21.6-43.2*(1.02**(-_value.hados[_value.skillnum]))))
                    if _value.wazapene[_value.skillnum]==0:
                        if _value.ky-16>_value.ground:_value.t=_value.kzi[_value.skillnum]*100
                    if _value.wazapene[_value.skillnum]==1:
                        if _value.ky-16>_value.ground and _value.kyv>0:_value.kyv=-_value.kyv

                    if _value.wazapene[_value.skillnum]==0:
                        if _value.ky-16>_value.ground:_value.t2=_value.kzi[_value.skillnum]*100
                # 突進
                if _value.wazatype[_value.skillnum]==2:
                    if _value.flip2==0:
                        _value.kxtest+=_value.kxv+_value.kad1[_value.skillnum]*_value.ad*0.5
                    else:
                        _value.kxtest-=_value.kxv+_value.kad1[_value.skillnum]*_value.ad*0.5
                    _value.kytest+=_value.kyv+_value.kws1[_value.skillnum]*_value.ws*0.5
                    if _value.wazapene[_value.skillnum]==0:
                        if _value.kytest>_value.ground:_value.t=_value.kzi[_value.skillnum]*100
                    if _value.wazapene[_value.skillnum]==1:


                        if _value.kytest>_value.ground and _value.kyv>0:_value.kyv=-_value.kyv
                
                    # if _value.wazapene[_value.skillnum]==0:
                    #     if _value.kytest>_value.ground:_value.t2=_value.kzi[_value.skillnum]*100
        if _value.kxtest>750:_value.kxtest=750
        if _value.kxtest<0:_value.kxtest=0
        _value.ttest+=1
        if _value.ttest==120:_value.ttest=0
        time.sleep(0.01)
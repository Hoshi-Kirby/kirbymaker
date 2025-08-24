import sys, random
import pygame, time
import cv2
import numpy as np
import _value

def bgr_to_rgb(color_bgr):
    b, g, r = color_bgr
    return (r, g, b)
def settingkirby(x,y,st):
    if _value.ka8_2[_value.ka3]==0 or st==0 :
        if _value.buki==0:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルf.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x,y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルfボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルfファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-5, y))
        if _value.buki==1:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルh.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.55)
                _value.screen.blit(img1, (x-2.3, y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルhボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルhファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-5, y))
    elif 0<st<=4:
        img1 = pygame.image.load(f"{_value.ka8_2[_value.ka3]}_{st}.png")
        img1.set_colorkey((255, 255, 255))
        img1 = img1.convert_alpha()
        img1 = pygame.transform.scale_by(img1, 2.5)
        s=3.2
        match _value.ka8_2[_value.ka3]:
            case 1:
                x-=6*s
                y-=4*s
            case 2:
                x-=5*s
                y-=5*s
            case 3:
                x-=1*s
                y-=0*s
            case 4:
                x-=3*s
                y-=1*s
            case 5:
                x-=4*s
                y-=3*s
            case 6:
                x-=8*s
                y-=10*s
            case 7:
                x-=9*s
                y-=4*s
            case 8:
                x-=0*s
                y-=1*s
            case 9:
                x-=4*s
                y-=1*s
            case 10:
                x-=4*s
                y-=7*s
            case 11:
                x-=1*s
                y-=11*s
            case 12:
                x-=3*s
                y-=12*s
            case 13:
                x-=6*s
                y-=7*s
            case 14:
                x-=3*s
                y-=11*s
            case 15:
                x-=3*s
                y-=8*s
            case 16:
                x-=4*s
                y-=8*s
            case 17:
                x-=7*s
                y-=15*s

        _value.screen.blit(img1, (x,y))
    if _value.erabuki[_value.ka3]==1:
        img2 = pygame.image.load(f"buki ({_value.ka3}).png")
        img2 = pygame.transform.scale_by(img2, 2.5)
        img2.set_colorkey((255, 255, 255))
        img2 = img2.convert_alpha()
        _value.screen.blit(img2, (x+_value.bukix[_value.ka3], y+_value.bukiy[_value.ka3]))

def standingkirby(x,y,st):
    if _value.ka8_2[_value.ka3]==0 or st==0 :
        if _value.buki==0:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルf.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x,y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルfボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルfファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-5, y))
        if _value.buki==1:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルh.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.55)
                _value.screen.blit(img1, (x-2.3, y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルhボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルhファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2.5)
                _value.screen.blit(img1, (x-5, y))
                
            img2 = pygame.image.load("buki.png")
            img2 = pygame.transform.scale_by(img2, 2.5)
            img2.set_colorkey((255, 255, 255))
            img2 = img2.convert_alpha()
            _value.screen.blit(img2, (x-34.7, y-52.8))
    elif 0<st<=4:
        img1 = pygame.image.load(f"{_value.ka8_2[_value.ka3]}_{st}.png")
        img1.set_colorkey((255, 255, 255))
        img1 = img1.convert_alpha()
        img1 = pygame.transform.scale_by(img1, 2.5)
        s=3.2
        match _value.ka8_2[_value.ka3]:
            case 1:
                x-=6*s
                y-=4*s
            case 2:
                x-=5*s
                y-=5*s
            case 3:
                x-=1*s
                y-=0*s
            case 4:
                x-=3*s
                y-=1*s
            case 5:
                x-=4*s
                y-=3*s
            case 6:
                x-=8*s
                y-=10*s
            case 7:
                x-=9*s
                y-=4*s
            case 8:
                x-=0*s
                y-=1*s
            case 9:
                x-=4*s
                y-=1*s
            case 10:
                x-=4*s
                y-=7*s
            case 11:
                x-=1*s
                y-=11*s
            case 12:
                x-=3*s
                y-=12*s
            case 13:
                x-=6*s
                y-=7*s
            case 14:
                x-=3*s
                y-=11*s
            case 15:
                x-=3*s
                y-=8*s
            case 16:
                x-=4*s
                y-=8*s
            case 17:
                x-=7*s
                y-=15*s

        _value.screen.blit(img1, (x,y))
        if _value.buki==1:
            img2 = pygame.image.load("buki.png")
            img2 = pygame.transform.scale_by(img2, 2.5)
            img2.set_colorkey((255, 255, 255))
            img2 = img2.convert_alpha()
            _value.screen.blit(img2, (x-34.7, y-52.8))

def skill(a):
    _value.t=0
    _value.t2=0
    _value.ws=0
    _value.ad=0
    _value.kx=(-2)*(_value.flip-0.5)*_value.kx0[a]*50+_value.kxtest
    _value.ky=_value.ky0[a]*50+_value.kytest
    _value.kxv=_value.kx1[a]
    _value.kyv=_value.ky1[a]
    _value.skillnum=a
    _value.kxtestbef=_value.kxtest
    _value.kytestbef=_value.kytest
    if _value.wazatype[a]==2:
        _value.kxtest+=(-2)*(_value.flip-0.5)*_value.kx0[a]*50
        _value.kytest+=_value.ky0[a]*50

def hando(a):
    _value.th=0
    _value.ws=0
    _value.ad=0
    _value.kxha=(-2)*(_value.flip-0.5)*_value.kx0h[a]*50+_value.kxtest
    _value.kyha=_value.ky0h[a]*50+_value.kytest
    _value.kxvha=_value.kx1h[a]
    _value.kyvha=_value.ky1h[a]
    _value.skillnum=a
    _value.kxtest+=(-2)*(_value.flip-0.5)*_value.kx0h[a]*50
    _value.kytest+=_value.ky0h[a]*50


def skillkirby(x,y,st):
    if _value.ka8_2[_value.skillnum]==0 or st==0 :
        if _value.buki==0:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルf.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x,y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルfボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルfファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-5, y))
        if _value.buki==1:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルh.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-2.3, y))
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルhボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-10, y-10))
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルhファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                _value.screen.blit(img1, (x-5, y))
    elif 0<st<=4:
        img1 = pygame.image.load(f"{_value.ka8_2[_value.skillnum]}_{st}.png")
        img1.set_colorkey((255, 255, 255))
        img1 = img1.convert_alpha()
        img1 = pygame.transform.scale_by(img1, 2)
        s=2.3
        match _value.ka8_2[_value.ka3]:
            case 1:
                x-=6*s
                y-=4*s
            case 2:
                x-=5*s
                y-=5*s
            case 3:
                x-=1*s
                y-=0*s
            case 4:
                x-=3*s
                y-=1*s
            case 5:
                x-=4*s
                y-=3*s
            case 6:
                x-=8*s
                y-=10*s
            case 7:
                x-=9*s
                y-=4*s
            case 8:
                x-=0*s
                y-=1*s
            case 9:
                x-=4*s
                y-=1*s
            case 10:
                x-=4*s
                y-=7*s
            case 11:
                x-=1*s
                y-=11*s
            case 12:
                x-=3*s
                y-=12*s
            case 13:
                x-=6*s
                y-=7*s
            case 14:
                x-=3*s
                y-=11*s
            case 15:
                x-=3*s
                y-=8*s
            case 16:
                x-=4*s
                y-=8*s
            case 17:
                x-=7*s
                y-=15*s

        if _value.flip==1:
            img1=pygame.transform.flip(img1, True, False)
        _value.screen.blit(img1, (x,y))


def tamekirby(x,y,t,step):
    if _value.ka8_2[_value.skillnum]==0:
        if _value.buki==0:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルf.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルfボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                x=-10
                y-=10
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルfファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                x-=5
        if _value.buki==1:
            if _value.bosi==0:
                img1 = pygame.image.load("ノーマルh.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                x-=2.3
            if _value.bosi==1:
                img1 = pygame.image.load("ノーマルhボム.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                x-=10
                y-=10
            if _value.bosi==2:
                img1 = pygame.image.load("ノーマルhファイター.png")
                img1.set_colorkey((255, 255, 255))
                img1 = img1.convert_alpha()
                img1 = pygame.transform.scale_by(img1, 2)
                if _value.flip==1:
                    img1=pygame.transform.flip(img1, True, False)
                x-=5
    else:
        img1 = pygame.image.load(f"{_value.ka8_2[_value.skillnum+step*10]}_1.png")
        img1 = pygame.transform.scale_by(img1, 2)
        if _value.flip==1:
            img1=pygame.transform.flip(img1, True, False)
    if (step==1 and (t-t%10)%30==0)or(step==2 and (t-t%10)%20==0):
        arr = pygame.surfarray.array3d(img1)
        arr = np.transpose(arr, (1, 0, 2))  # 転置して (height, width, 3)
        # 白画像作成
        white = np.full_like(arr, 255)
        # OpenCVで白をブレンド
        blended = cv2.addWeighted(arr, 0.6, white, 0.4, 0)
        # NumPy配列 → Surfaceに戻す
        blended = np.transpose(blended, (1, 0, 2))  # 転置戻す
        img1 = pygame.surfarray.make_surface(blended)
    img1.set_colorkey((255, 255, 255))
    img1 = img1.convert_alpha()
    _value.screen.blit(img1, (x,y))

#型自動判定
def infer_sqlite_type(value):
    if isinstance(value, int):
        return "INTEGER"
    elif isinstance(value, float):
        return "REAL"
    elif isinstance(value, str):
        return "TEXT"
    else:
        return "BLOB"  # その他（画像など）も対応可能
import sys, random
import pygame, time
import cv2
import numpy as np
import sqlite3
import os
from PIL import Image
image = cv2.imread(r"C:\python\kirby\h.png")
cv2.imwrite("buki.png", image)
from pygame.locals import *
pygame.init()
pygame.mixer.init()


import _func
import _value

def loaddata():
    pygame.display.update()
    _value.screen.fill((200,200,255))
    mouseX, mouseY = pygame.mouse.get_pos()
    text = _value.font.render("データを選択してください", False, (0,0,0))
    text_rect = text.get_rect(center=(400, 70))
    _value.screen.blit(text, text_rect)
    ka9=-1
    for i in range(2):
        for ii in range(3):
            if 80+i*350<mouseX<80+i*350+300 and 130+ii*150<mouseY<130+ii*150+100 and _value.nameload[i*3+ii]!="データなし":
                pygame.draw.rect(_value.screen,(220,220,230),(80+i*350,130+ii*150,300,100),border_radius=5)
                ka9=i*3+ii
            else:
                if _value.nameload[i*3+ii]=="データなし":
                    pygame.draw.rect(_value.screen,(180,180,180),(80+i*350,130+ii*150,300,100),border_radius=5)
                else:
                    pygame.draw.rect(_value.screen,(255,255,255),(80+i*350,130+ii*150,300,100),border_radius=5)
            text = _value.font.render(str(i*3+ii+1), False, (0,0,0))
            text_rect = text.get_rect(center=(80+i*350+20,130+ii*150+20))
            _value.screen.blit(text, text_rect)
            text = _value.font.render(_value.nameload[i*3+ii], False, (0,0,0))
            text_rect = text.get_rect(center=(80+i*350+150,130+ii*150+50))
            _value.screen.blit(text, text_rect)
            if _value.nameload[i*3+ii]!="データなし":
                _func.loadkirby(80+i*350+20,130+ii*150+50,_value.bukiload[i*3+ii],_value.bosiload[i*3+ii],i*3+ii)
    _value.ka9=ka9

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and ka9>=0:
                if _value.nameload[ka9]!="データなし":
                    _value.se_enter1.play()
                    _value.loadstep=1
                else:
                    _value.se_bubu.play()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                _value.se_esc.play()
                _value.loadstep=-1
                _value.step=1
    
    time.sleep(0.01)

def loadb():
    pygame.display.update()
    mouseX, mouseY = pygame.mouse.get_pos()
    pygame.draw.rect(_value.screen, (255,255,255),(50,200,700,200))
    text=_value.font.render(_value.nameload[_value.ka9], False, (0,0,0))
    text_rect = text.get_rect(center=(400, 250))
    _value.screen.blit(text, text_rect)
    text=_value.font.render("このデータをロードしますか", False, (0,0,0))
    text_rect = text.get_rect(center=(400, 300))
    _value.screen.blit(text, text_rect)
    x=85
    y=350
    if x+540<mouseX<100+x+540 and y<mouseY<40+y:
        hozon=(200,100,100)
    else:
        hozon=(0,0,0)
    if x<mouseX<x+100 and y<mouseY<y+40:
        purei=(100,100,200)
    else:
        purei=(0,0,0)
    pygame.draw.rect(_value.screen, (200,50,50), (x+540,y,100,40), width=3,border_radius=5)
    pygame.draw.rect(_value.screen, (100,100,200), (x,y,100,40), width=3,border_radius=5)
    text = _value.font.render("ロード", False, (hozon))
    text_rect = text.get_rect(center=(x+50+540,y+20))
    _value.screen.blit(text, text_rect)
    text = _value.font.render("やめる", False, (purei))
    text_rect = text.get_rect(center=(x+50,y+20))
    _value.screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if x<mouseX<100+x and y<mouseY<40+y:
                    _value.loadstep=0
                    _value.se_esc.play()
                if x+540<mouseX<x+540+100 and y<mouseY<y+40:
                    _value.loadstep=2
                    _value.se_enter1.play()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                    _value.se_enter1.play()
                    _value.loadstep=2
            if event.key==pygame.K_ESCAPE:
                    _value.se_esc.play()
                    _value.loadstep=0

def load():
    pygame.draw.rect(_value.screen, (255,255,255),(50,200,700,200))
    text=_value.font.render("ロード中...", False, (0,0,0))
    text_rect = text.get_rect(center=(400,280))
    _value.screen.blit(text, text_rect)
    pygame.display.update()
    conn = sqlite3.connect(os.path.join("save", "save.db"))

    slot=_value.ka9
    #ロード
    try:
        cursor = conn.cursor()

        cursor.execute(f"PRAGMA table_info(save{slot})")
        columns_info = cursor.fetchall()
        columns = [col[1] for col in columns_info]

        cursor.execute(f"SELECT * FROM save{slot} WHERE col1 = ?", (slot,))
        row = cursor.fetchone()

        data = list(row)

        _, _value.title, _value.buki, _value.bosi = data[:4]
        value = data[4:34]
        x=0
        _value.title_list  = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.title_len  = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.wazatype = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kx2 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kx1 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kx0 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.ky2 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.ky1 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.ky0 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kzi = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kzi2 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kad2 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kws2 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kad1 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kws1 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kx2h = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kx1h = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kx0h = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.ky2h = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.ky1h = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.ky0h = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kzih = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kad2h = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kws2h = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kad1h = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kws1h = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kds = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.kkk = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.wazapene = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.wazatuka = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.wazadame = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.wazahuto = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.wazatame = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.ka8_2 = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.bukix = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.bukiy = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.hados = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]
        x+=1
        _value.erabuki = data[4+(_value.tab+20)*x:4+(_value.tab+20)*(x+1)]


        
    except sqlite3.OperationalError as e:
        print(f"SQLの実行に失敗しました: {e}")

    except sqlite3.DatabaseError as e:
        print(f"データベースエラー: {e}")

    except ValueError as e:
        print(f"ロード失敗: {e}")

    except Exception as e:
        print(f"予期しないエラー: {e}")
    finally:
        conn.close()

    save_folder = "save"


    filename = f"{slot}-buki.png"
    load_path = os.path.join(save_folder, filename)
    if os.path.isfile(load_path):
        img=Image.open(load_path)
        img.save("buki.png")

    filename = f"{slot}-buki2.png"
    load_path = os.path.join(save_folder, filename)
    if os.path.isfile(load_path):
        img=Image.open(load_path)
        img.save("buki2.png")

    for i in range(30):
        filename = f"{slot}-buki ({i}).png"
        load_path = os.path.join(save_folder, filename)
        if os.path.isfile(load_path):
            img=Image.open(load_path)
            img.save(f"buki ({i}).png")

        filename = f"{slot}-buki2 ({i}).png"
        load_path = os.path.join(save_folder, filename)
        if os.path.isfile(load_path):
            img=Image.open(load_path)
            img.save(f"buki2 ({i}).png")

        filename = f"{slot}-hado ({i}).png"
        load_path = os.path.join(save_folder, filename)
        if os.path.isfile(load_path):
            img=Image.open(load_path)
            img.save(f"hado ({i}).png")

        filename = f"{slot}-hado2 ({i}).png"
        load_path = os.path.join(save_folder, filename)
        if os.path.isfile(load_path):
            img=Image.open(load_path)
            img.save(f"hado2 ({i}).png")

def loada():
    pygame.display.update()
    _value.screen.fill((200,200,255))
    mouseX, mouseY = pygame.mouse.get_pos()
    text = _value.font.render("カービィメーカー", False, (0,0,0))
    text_rect = text.get_rect(center=(400, 70))
    _value.screen.blit(text, text_rect)
    list=["編集","削除"]
    le=len(list)
    interval=100
    
    text_rect=[None]*le
    for i in range (le):
        text = _value.font.render(list[i], False, (0,0,0))
        text_rect[i] = text.get_rect(center=(400, 350-interval*le/2 + i*interval))
        if text_rect[i].collidepoint(mouseX,mouseY):
            _value.ka10=i
        if _value.ka10==i:
            text = _value.font.render(list[i], False, (100,100,100))
            text_rect[i] = text.get_rect(center=(400, 350-interval*le/2 + i*interval))
        _value.screen.blit(text, text_rect[i])
    
    
    if _value.step2==1:
        x=85
        y=350
        pygame.draw.rect(_value.screen, (255,255,255),(50,200,700,200))
        text=_value.font.render("本当にこのデータを削除しますか", False, (0,0,0))
        text_rect = text.get_rect(center=(400, 300))
        _value.screen.blit(text, text_rect)
        if x+540<mouseX<100+x+540 and y<mouseY<40+y:
            hozon=(200,100,100)
        else:
            hozon=(0,0,0)
        if x<mouseX<x+100 and y<mouseY<y+40:
            purei=(100,100,200)
        else:
            purei=(0,0,0)
        pygame.draw.rect(_value.screen, (200,50,50), (x+550,y,80,40), width=3,border_radius=5)
        pygame.draw.rect(_value.screen, (100,100,200), (x,y,100,40), width=3,border_radius=5)
        text = _value.font.render("削除", False, (hozon))
        text_rect = text.get_rect(center=(x+50+540,y+20))
        _value.screen.blit(text, text_rect)
        text = _value.font.render("やめる", False, (purei))
        text_rect = text.get_rect(center=(x+50,y+20))
        _value.screen.blit(text, text_rect)
    if _value.step2==2:
        x=400-40
        y=350
        pygame.draw.rect(_value.screen, (255,255,255),(50,200,700,200))
        text=_value.font.render("削除しました", False, (0,0,0))
        text_rect = text.get_rect(center=(400, 300))
        _value.screen.blit(text, text_rect)
        if x<mouseX<x+100 and y<mouseY<y+40:
            purei=(100,100,200)
        else:
            purei=(0,0,0)
        pygame.draw.rect(_value.screen, (100,100,200), (x,y,80,40), width=3,border_radius=5)
        text = _value.font.render("戻る", False, (purei))
        text_rect = text.get_rect(center=(x+40,y+20))
        _value.screen.blit(text, text_rect)

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if _value.step2==0:
                    if event.button == 1:
                        click=-1
                        for i in range (le):
                            if text_rect[i].collidepoint(event.pos):
                                click=i
                        match click:
                            case -1:
                                1
                            
                            case 0:
                                _value.se_enter1.play()
                                _value.step=2
                                _value.loadstep=0
                            case 1:
                                _value.step2=1
                                _value.se_enter1.play()
                elif _value.step2==1:
                    if event.button == 1:
                        if x<mouseX<100+x and y<mouseY<40+y:
                            _value.step2=0
                            _value.se_esc.play()
                        if x+540<mouseX<x+540+100 and y<mouseY<y+40:
                            _value.se_enter1.play()
                            _value.se_enter1.play()
                            slot=_value.ka9
                            # データベースのテーブル削除
                            db_path = os.path.join("save", "save.db")
                            if os.path.exists(db_path):
                                conn = sqlite3.connect(db_path)
                                cursor = conn.cursor()
                                cursor.execute(f"DROP TABLE IF EXISTS save{slot}")
                                conn.commit()
                                conn.close()

                            # 画像ファイルの削除
                            for i in range(30):
                                image_files = [
                                    f"{slot}-buki ({i}).png",
                                    f"{slot}-buki2 ({i}).png",
                                    f"{slot}-hado ({i}).png",
                                    f"{slot}-hado2 ({i}).png",
                                ]
                                for path in image_files:
                                    if os.path.exists(path):
                                        os.remove(path)
                            _value.step2=2
                elif _value.step2==2:
                    if event.button == 1:
                        if x<mouseX<100+x and y<mouseY<40+y:
                            _value.se_esc.play()
                            _value.step=1
                            _value.loadstep=0
            if event.type == KEYDOWN: 
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    _value.ka10-=1
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    _value.ka10+=1
                if event.key == pygame.K_RETURN:
                    match _value.ka10:
                        case -1:
                            1
                        
                        case 0:
                            _value.se_enter1.play()
                            _value.step=2
                            _value.loadstep=0
                        case 1:
                            _value.se_enter1.play()
                            _value.step2=1

            
            if _value.ka10<0:
                _value.ka10=0
            if _value.ka10>le-1:
                _value.ka10=le-1
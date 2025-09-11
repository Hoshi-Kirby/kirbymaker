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

#セーブ前
def savebb():
    pygame.display.update()
    pygame.draw.rect(_value.screen, (255,255,255),(50,200,700,200))
    text=_value.font.render("セーブデータを上書きしますがよろしいですか", False, (0,0,0))
    text_rect = text.get_rect(center=(400, 250))
    _value.screen.blit(text, text_rect)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
def saveb():
    pygame.display.update()
    mouseX, mouseY = pygame.mouse.get_pos()

    x=90
    y=350
    if x+540<mouseX<80+x+540 and y<mouseY<40+y:
        hozon=(200,100,100)
    else:
        hozon=(0,0,0)
    if x<mouseX<x+80 and y<mouseY<y+40:
        purei=(100,100,200)
    else:
        purei=(0,0,0)
    pygame.draw.rect(_value.screen, (200,50,50), (x+540,y,80,40), width=3,border_radius=5)
    pygame.draw.rect(_value.screen, (100,100,200), (x,y,80,40), width=3,border_radius=5)
    text = _value.font.render("OK", False, (hozon))
    text_rect = text.get_rect(center=(x+40+540,y+20))
    _value.screen.blit(text, text_rect)
    text = _value.font.render("戻る", False, (purei))
    text_rect = text.get_rect(center=(x+40,y+20))
    _value.screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if x<mouseX<80+x and y<mouseY<40+y:
                    _value.savestep=1
                    _value.se_esc.play()
                if x+540<mouseX<x+540+80 and y<mouseY<y+40:
                    _value.savestep=3
                    _value.se_enter1.play()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                _value.savestep=3
                _value.se_enter1.play()
            if event.key==pygame.K_ESCAPE:
                _value.savestep=1
                _value.se_esc.play()
    
    time.sleep(0.01)

#一度切り
def save():
    text = _value.font.render("保存中...", False, (0,0,0))
    text_rect = text.get_rect(center=(400,350+20))
    _value.screen.blit(text, text_rect)
    pygame.display.update()

    if _value.ka9>=0:
        #セーブスロット
        slot=_value.ka9
        #データ
        data = [slot,
                _value.title,
                _value.buki,
                _value.bosi,
                *_value.title_list [:_value.tab+20],
                *_value.title_len [:_value.tab+20],
                *_value.wazatype[:_value.tab+20],
                *_value.kx2[:_value.tab+20],
                *_value.kx1[:_value.tab+20],
                *_value.kx0[:_value.tab+20],
                *_value.ky2[:_value.tab+20],
                *_value.ky1[:_value.tab+20],
                *_value.ky0[:_value.tab+20],
                *_value.kzi[:_value.tab+20],
                *_value.kzi2[:_value.tab+20],
                *_value.kad2[:_value.tab+20],
                *_value.kws2[:_value.tab+20],
                *_value.kad1[:_value.tab+20],
                *_value.kws1[:_value.tab+20],
                *_value.kx2h[:_value.tab+20],
                *_value.kx1h[:_value.tab+20],
                *_value.kx0h[:_value.tab+20],
                *_value.ky2h[:_value.tab+20],
                *_value.ky1h[:_value.tab+20],
                *_value.ky0h[:_value.tab+20],
                *_value.kzih[:_value.tab+20],
                *_value.kad2h[:_value.tab+20],
                *_value.kws2h[:_value.tab+20],
                *_value.kad1h[:_value.tab+20],
                *_value.kws1h[:_value.tab+20],
                *_value.kds[:_value.tab+20],
                *_value.kkk[:_value.tab+20],
                *_value.wazapene[:_value.tab+20],
                *_value.wazatuka[:_value.tab+20],
                *_value.wazadame[:_value.tab+20],
                *_value.wazahuto[:_value.tab+20],
                *_value.wazatame[:_value.tab+20],
                *_value.ka8_2[:_value.tab+20],
                *_value.bukix[:_value.tab+20],
                *_value.bukiy[:_value.tab+20],
                *_value.hados[:_value.tab+20],
                *_value.erabuki[:_value.tab+20],
                ]

        #セーブ
        os.makedirs("save", exist_ok=True) # フォルダがなければ作成
        conn = sqlite3.connect(os.path.join("save", "save.db"))  # データベースに接続（なければ作成）
        cursor = conn.cursor()             # SQLを操作するためのカーソルを取得

        #要素数が変わるときにいるけど要素数が変わらないならいらない
        cursor.execute(f"DROP TABLE IF EXISTS save{slot}")

        num_columns = len(data)
        columns = [f"col{i}" for i in range(1, num_columns + 1)]
        column_type = [_func.infer_sqlite_type(val) for val in data]

        col_defs = ",\n    ".join([
            f"{columns[0]} INTEGER PRIMARY KEY"
        ] + [f"{name} {column_type}" for name in columns[1:]])

        sql = f"CREATE TABLE IF NOT EXISTS save{slot} (\n    {col_defs}\n)"
        cursor.execute(sql)

        placeholders = ', '.join(['?'] * len(data))  # "?, ?, ?, ..., ?" を自動生成

        sql = f"INSERT INTO save{slot} VALUES ({placeholders})"
        cursor.execute(sql, data)


        conn.commit()  # 保存（変更を確定）
        conn.close()   # 接続を終了


        save_folder = "save"

        img = Image.open("buki.png")
        filename = f"{slot}-buki.png"
        save_path = os.path.join(save_folder, filename)
        img.save(save_path)

        img = Image.open("buki2.png")
        filename = f"{slot}-buki2.png"
        save_path = os.path.join(save_folder, filename)
        img.save(save_path)

        for i in range(30):
            img = Image.open(f"buki ({i}).png")
            filename = f"{slot}-buki ({i}).png"
            save_path = os.path.join(save_folder, filename)
            img.save(save_path)

            img = Image.open(f"buki2 ({i}).png")
            filename = f"{slot}-buki2 ({i}).png"
            save_path = os.path.join(save_folder, filename)
            img.save(save_path)

            img = Image.open(f"hado ({i}).png")
            filename = f"{slot}-hado ({i}).png"
            save_path = os.path.join(save_folder, filename)
            img.save(save_path)

            img = Image.open(f"hado2 ({i}).png")
            filename = f"{slot}-hado2 ({i}).png"
            save_path = os.path.join(save_folder, filename)
            img.save(save_path)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    time.sleep(0.01)

#セーブ後
def savea():
    pygame.display.update()
    _value.screen.fill((200,200,255))
    mouseX, mouseY = pygame.mouse.get_pos()
    pygame.draw.rect(_value.screen, (255,255,255),(50,200,700,200))
    text=_value.font.render("保存しました", False, (0,0,0))
    text_rect = text.get_rect(center=(400, 250))
    _value.screen.blit(text, text_rect)
    text=_value.font.render("編集を続けますか", False, (0,0,0))
    text_rect = text.get_rect(center=(400, 280))
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
    text = _value.font.render("続ける", False, (hozon))
    text_rect = text.get_rect(center=(x+50+540,y+20))
    _value.screen.blit(text, text_rect)
    text = _value.font.render("終わる", False, (purei))
    text_rect = text.get_rect(center=(x+50,y+20))
    _value.screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if x<mouseX<100+x and y<mouseY<40+y:
                    _value.savestep=0
                    _value.step=1
                    _value.se_esc.play()
                if x+540<mouseX<x+540+100 and y<mouseY<y+40:
                    _value.savestep=0
                    _value.step=3
                    _value.se_enter1.play()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                    _value.savestep=0
                    _value.step=3
                    _value.se_enter1.play()
            if event.key==pygame.K_ESCAPE:
                    _value.savestep=0
                    _value.step=1
                    _value.se_esc.play()
    
    time.sleep(0.01)
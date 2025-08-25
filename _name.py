import sys, random
import pygame, time
import cv2
import numpy as np
import sqlite3
import os
image = cv2.imread(r"C:\python\kirby\h.png")
cv2.imwrite("buki.png", image)
from pygame.locals import *
pygame.init()
pygame.mixer.init()


import _func
import _value

def nameload():
    _value.nameload = []
    _value.bukiload = []
    _value.bosiload = []
    if os.path.isdir("save") and os.path.isfile(os.path.join("save", "save.db")):
        
        conn = sqlite3.connect(os.path.join("save", "save.db"))
        for slot in range(6):
            #ロード
            table_name = f"save{slot}"
            cursor = conn.cursor()

            # テーブルの存在チェック
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
            table_exists = cursor.fetchone()

            if not table_exists:
                _value.nameload.append("データなし")  # テーブルが存在しない
                _value.bukiload.append(0)
                _value.bosiload.append(0)
                continue


            cursor.execute(f"PRAGMA table_info({table_name})")

            columns_info = cursor.fetchall()
            columns = [col[1] for col in columns_info]

            cursor.execute(f"SELECT col2,col3,col4 FROM {table_name} WHERE col1 = ?", (slot,))
            row = cursor.fetchone()

            if row:
                _value.nameload.append(row[0])
            else:
                _value.nameload.append("")
            _value.bukiload.append(row[1])
            _value.bosiload.append(row[2])

        conn.close()
    else:
        _value.nameload = ["データなし"]*6
        _value.bukiload = []
        _value.bosiload = []

def name():
    pygame.display.update()
    _value.screen.fill((200,200,255))
    mouseX, mouseY = pygame.mouse.get_pos()

    txt_surface = _value.font.render(_value.title, True, _value.color)
    width = max(300, txt_surface.get_width() + 10)
    _value.input_box.w = width
    _value.screen.blit(txt_surface, (250, 260))
    pygame.draw.line(_value.screen, _value.color, (250,300),(250+width,300), 2)
    
    text = _value.font.render("能力名を決めてね", False, (0,0,0))
    text_rect = text.get_rect(center=(400, 70))
    _value.screen.blit(text, text_rect)

    if pygame.time.get_ticks() % 1000 < 500:
        cursor_x = 250 + 5 + txt_surface.get_width()
        pygame.draw.line(_value.screen, (0,0,0),(cursor_x, 262),(cursor_x, 294), 2)

    x=50
    y=460
    if x+620<mouseX<80+x+620 and y<mouseY<40+y:
        hozon=(200,100,100)
    else:
        hozon=(0,0,0)
    if x<mouseX<x+80 and y<mouseY<y+40:
        purei=(100,100,200)
    else:
        purei=(0,0,0)
    pygame.draw.rect(_value.screen, (200,50,50), (x+620,y,80,40), width=3,border_radius=5)
    pygame.draw.rect(_value.screen, (100,100,200), (x,y,80,40), width=3,border_radius=5)
    text = _value.font.render("保存", False, (hozon))
    text_rect = text.get_rect(center=(x+40+620,y+20))
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
                    _value.savestep=0
                if x+620<mouseX<x+620+80 and y<mouseY<y+40:
                    _value.savestep=2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                _value.title = _value.title[:-1]
            else:
                if event.key!=pygame.K_RETURN and event.key!=pygame.K_ESCAPE and event.key!=pygame.K_TAB and len(_value.title)<20:
                    _value.title += event.unicode
            if event.key == pygame.K_ESCAPE:
                _value.savestep=0
    
    time.sleep(0.01)
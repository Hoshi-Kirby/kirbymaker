import sys, random
import pygame, time
import cv2
import numpy as np
image = cv2.imread(r"C:\python\kirby\h.png")
cv2.imwrite("buki.png", image)
from pygame.locals import *
pygame.init()
pygame.mixer.init()

step=1
white = (255,255,255)
black = (0,0,0)
red=(255,0,0)
blue=(0,0,255)
pose=0
posetime=0
flip=0
ground=400
kx=225
ky=ground
kyv=0
kxh=0
kyh=0
hob=0
hobc=0
kaih=0
skaih=0
shagam=0
sura=0

sctime=0
sc=0
tab=9
rightime=0
leftime=0

screen = pygame.display.set_mode((800, 600))

ka=0
ka3=0
title_list = [""]*(tab+20)
wazatype=[0]*(tab+20)
kx2=[0]*(tab+20)
kx1=[0]*(tab+20)
kx0=[0]*(tab+20)
ky2=[0]*(tab+20)
ky1=[0]*(tab+20)
ky0=[0]*(tab+20)
kzi=[1]*(tab+20)
kad2=[0]*(tab+20)
kws2=[0]*(tab+20)
kad1=[0]*(tab+20)
kws1=[0]*(tab+20)
kds=[0]*(tab+20)#弾数
kkk=[0]*(tab+20)#間隔
kx2h=[0]*(tab+20)
kx1h=[0]*(tab+20)
kx0h=[0]*(tab+20)
ky2h=[0]*(tab+20)
ky1h=[0]*(tab+20)
ky0h=[0]*(tab+20)
kzih=[1]*(tab+20)
kad2h=[0]*(tab+20)
kws2h=[0]*(tab+20)
kad1h=[0]*(tab+20)
kws1h=[0]*(tab+20)

wazapene=[0]*(tab+20)
wazatuka=[0]*(tab+20)
wazadame=[0]*(tab+20)
wazahuto=[0]*(tab+20)
wazatame=[0]*(tab+20)
buki=0
bosi=0
running=True
drag=0
step2=0

ka=0
esch=0
step2=0
drag=0
cr=255
cg=255
cb=255
mx=-1
my=-1
back=(255,255,255)

ka4=1
tab4=8
input_box = pygame.Rect(50, 80, 400, 40)
color_inactive = pygame.Color(0,0,0)
color_active = pygame.Color(150,50,50)
color = color_inactive
active = False
title = title_list[ka3]

ws=0
t=0
ad=0
kx=kx0[ka3]*50
ky=ky0[ka3]*50
kxv=kx1[ka3]
kyv=ky1[ka3]

box_rects = [pygame.Rect(371+i*100, 185, 40, 30) for i in range(13)]
for i in range(4):
    box_rects[i+3]=pygame.Rect(371+i*100, 385, 40, 30)
for i in range(2):
    box_rects[i+7]=pygame.Rect(371+i*100, 235, 40, 30)
for i in range(2):
    box_rects[i+9]=pygame.Rect(371+i*100, 435, 40, 30)
for i in range(2):
    box_rects[i+11]=pygame.Rect(401+i*200, 85, 40, 30)
active2=[False]*13
input_text=["0"]*13
input_text[0]=str(kx2[ka3])
input_text[1]=str(kx1[ka3])
input_text[2]=str(kx0[ka3])
input_text[3]=str(ky2[ka3])
input_text[4]=str(ky1[ka3])
input_text[5]=str(ky0[ka3])
input_text[6]=str(kzi[ka3])
input_text[7]=str(kad2[ka3])
input_text[8]=str(kad1[ka3])
input_text[9]=str(kws2[ka3])
input_text[10]=str(kws1[ka3])
input_text[11]=str(kds[ka3])
input_text[12]=str(kkk[ka3])
ka5=0
tab5=0


ka6=0

kxtest=225
kytest=ground
kxtestv=0
kytestv=0








font = pygame.font.SysFont("hg正楷書体pro", 30)
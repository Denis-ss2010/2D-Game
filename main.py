import pygame
from pygame import *
#from pygame.examples.go_over_there import screen
from Dragon_create import *
#from pygame.examples.go_over_there import clock
from keyword import *
from zmini import *
from random import *
import time as t

init()

window = display.set_mode(size_window)
clock = time.Clock()


green_coin = transform.scale(image.load("photo/D_coin/Green.png"), (50,50))
class Block:
    def __init__(self, pos_x,pos_y,type,r_x,r_y,photo):
        self.img = transform.scale(image.load(photo), (r_x,r_y))
        self.rect = pygame.Rect(pos_x, pos_y, r_x, r_y)
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.type = type

    def show(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

dragon_red_at = transform.scale(image.load('photo/F_at/Red.png'),(40,40))
dragon_red_at = pygame.Rect(50, 50, 40, 40)

dragon_green_at = transform.scale(image.load('photo/F_at/Green.png'),(40,40))
dragon_green_at = pygame.Rect(10, 10, 40, 40)

Fon = transform.scale(image.load('photo/Fon/Brown.png'),(80,80))

def fon_full():
    for y in range(0, size_window[1], 80):
        for x in range(0, size_window[0], 80):
            window.blit(Fon, (x, y))


#'photo/block/dern16x16.png'
def bloks_create(s_y,st_y,povtor,st_x,start_number,photo1):
    while povtor > 0:
        (block, start_number)= Block(st_x,s_y,1,50,50,photo1)
        (block, start_number).show()
        povtor -= 1
        start_number += 1
        st_x += 50

block0 = Block(0,850,1,50,50,'photo/block/dern16x16.png')
block1 = Block(50,850,1,50,50,'photo/block/dern16x16.png')
block2 = Block(100,850,1,50,50,'photo/block/dern16x16.png')
block3 = Block(150,850,1,50,50,'photo/block/dern16x16.png')
block4 = Block(200,850,1,50,50,'photo/block/dern16x16.png')
block5 = Block(250,850,1,50,50,'photo/block/dern16x16.png')
block6 = Block(300,850,1,50,50,'photo/block/dern16x16.png')
block7 = Block(350,850,1,50,50,'photo/block/dern16x16.png')
block8 = Block(400,850,1,50,50,'photo/block/dern16x16.png')
block9 = Block(450,850,1,50,50,'photo/block/dern16x16.png')
block10 = Block(500,850,1,50,50,'photo/block/dern16x16.png')
block11 = Block(550,850,1,50,50,'photo/block/dern16x16.png')
block12 = Block(600,850,1,50,50,'photo/block/dern16x16.png')
block13 = Block(650,850,1,50,50,'photo/block/dern16x16.png')
block14 = Block(700,850,1,50,50,'photo/block/dern16x16.png')
block15 = Block(750,850,1,50,50,'photo/block/dern16x16.png')
block16 = Block(800,850,1,50,50,'photo/block/dern16x16.png')
block17 = Block(850,850,1,50,50,'photo/block/dern16x16.png')
block18 = Block(900,850,1,50,50,'photo/block/dern16x16.png')
block19 = Block(950,850,1,50,50,'photo/block/dern16x16.png')
block20 = Block(1000,850,1,50,50,'photo/block/dern16x16.png')
block21 = Block(1050,850,1,50,50,'photo/block/dern16x16.png')
block22 = Block(1100,850,1,50,50,'photo/block/dern16x16.png')
block23 = Block(1150,850,1,50,50,'photo/block/dern16x16.png')
block24 = Block(1200,850,1,50,50,'photo/block/dern16x16.png')
block25 = Block(1250,850,1,50,50,'photo/block/dern16x16.png')
block26 = Block(1300,850,1,50,50,'photo/block/dern16x16.png')
block27 = Block(1350,850,1,50,50,'photo/block/dern16x16.png')
block28 = Block(1400,850,1,50,50,'photo/block/dern16x16.png')
block29= Block(1450,850,1,50,50,'photo/block/dern16x16.png')
block30= Block(1500,850,1,50,50,'photo/block/dern16x16.png')
block31= Block(1550,850,1,50,50,'photo/block/dern16x16.png')
block32= Block(1600,850,1,50,50,'photo/block/dern16x16.png')
block33= Block(1650,850,1,50,50,'photo/block/dern16x16.png')
block34= Block(1700,850,1,50,50,'photo/block/dern16x16.png')
block35= Block(1750,850,1,50,50,'photo/block/dern16x16.png')
block36 = Block(1800,850,1,50,50,'photo/block/dern16x16.png')
block37 = Block(1850,850,1,50,50,'photo/block/dern16x16.png')
block38 = Block(1900,850,1,50,50,'photo/block/dern16x16.png')
block39 = Block(0,900,1,50,50,'photo/block/1.png')
block40 = Block(50,900,1,50,50,'photo/block/1.png')
block41 = Block(100,900,1,50,50,'photo/block/1.png')
block42 = Block(150,900,1,50,50,'photo/block/1.png')
block43 = Block(200,900,1,50,50,'photo/block/1.png')
block49 = Block(500,825,2,50,25,'photo/block/ship.png')
block50 = Block(1400,825,2,50,25,'photo/block/ship.png')
block51 = Block(500,825,2,50,25,'photo/block/ship.png')
block52 = Block(1400,825,2,50,25,'photo/block/ship.png')
block53 = Block(500,825,2,50,25,'photo/block/ship.png')
block54 = Block(1400,825,2,50,25,'photo/block/ship.png')
block55 = Block(0,0,1,50,50,'photo/block/1.png')
block56 = Block(0,0,1,50,50,'photo/block/1.png')
block57 = Block(0,0,1,50,50,'photo/block/1.png')
block58 = Block(0,0,1,50,50,'photo/block/1.png')
block59 = Block(0,0,1,50,50,'photo/block/1.png')
block60 = Block(0,0,1,50,50,'photo/block/1.png')
block61 = Block(0,0,1,50,50,'photo/block/1.png')
block62 = Block(0,0,1,50,50,'photo/block/1.png')
block63 = Block(0,0,1,50,50,'photo/block/1.png')
block64 = Block(0,0,1,50,50,'photo/block/1.png')
block65 = Block(0,0,1,50,50,'photo/block/1.png')
block66 = Block(0,0,1,50,50,'photo/block/1.png')
block67 = Block(0,0,1,50,50,'photo/block/1.png')
block68 = Block(0,0,1,50,50,'photo/block/1.png')
block69 = Block(0,0,1,50,50,'photo/block/1.png')
block70 = Block(0,0,1,50,50,'photo/block/1.png')
block71 = Block(0,0,1,50,50,'photo/block/1.png')
block72 = Block(0,0,1,50,50,'photo/block/1.png')
block73 = Block(0,0,1,50,50,'photo/block/1.png')
block74 = Block(0,0,1,50,50,'photo/block/1.png')
block75 = Block(0,0,1,50,50,'photo/block/1.png')
block76 = Block(1250,600,1,50,50,'photo/block/1.png')
block77 = Block(1750,0,1,50,50,'photo/block/1.png')
block78 = Block(1750,50,1,50,50,'photo/block/1.png')
block79 = Block(1750,100,1,50,50,'photo/block/1.png')
block80 = Block(1650,550,1,50,50,'photo/block/1.png')
block81 = Block(1600,600,1,50,50,'photo/block/1.png')
block82 = Block(1400,650,1,50,50,'photo/block/1.png')
block83 = Block(1500,600,1,50,50,'photo/block/1.png')
block84= Block(1650,800,1,50,50,'photo/block/1.png')
block85= Block(1600,750,1,50,50,'photo/block/1.png')
block86= Block(1550,800,1,50,50,'photo/block/1.png')
block87= Block(1600,200,1,50,50,'photo/block/1.png')
block88= Block(1600,400,1,50,50,'photo/block/1.png')
block89= Block(1450,250,1,50,50,'photo/block/1.png')
block90= Block(1750,250,1,50,50,'photo/block/1.png')
block91 = Block(1550,300,1,50,50,'photo/block/1.png')
block92 = Block(1850,300,1,50,50,'photo/block/1.png')
block93 = Block(1800,300,1,50,50,'photo/block/1.png')
block94= Block(1750,300,1,50,50,'photo/block/1.png')
block95= Block(1700,300,1,50,50,'photo/block/1.png')
block96= Block(1650,350,1,50,50,'photo/block/1.png')
block97= Block(1700,250,1,50,50,'photo/block/1.png')
block98 = Block(1700,200,1,50,50,'photo/block/1.png')
block99 = Block(1800,150,1,50,50,'photo/block/1.png')
block100 = Block(1850,150,1,50,50,'photo/block/1.png')



block44 = Block(1850,100,3,50,50,'photo/block/Dore.png')
block45 = Block(1050,600,7,50,50,'photo/D_coin/Red.png')
block46 = Block(1300,250,5,50,50,'photo/D_coin/Yellow.png')
block47 = Block(1850,250,6,50,50,'photo/D_coin/Blue.png')
block48 = Block(1850,800,8,50,50,'photo/block/key.png')






blocks = [block0,block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20,block21,block22,block23,block24,block25,block26,block27,block28,block29,block30,block31,block32,block33,block34,block35,block36,block37,block38,block39,block40,block41,block42,block43,block44,block45,block46,block47,block48,block49,block50,block51,block52,block53,block54,block55,block56,block57,block58,block59,block50,block61,block62,block63,block64,block65,block66,block67,block68,block69,block70,block71,block72,block73,block74,block75,block76,block77,block78,block79,block80,block81,block82,block83,block84,block85,block86,block87,block88,block89,block90,block91,block92,block93,block94,block95,block96,block97,block98,block99,block100]


tt = 0
bottom_side_dragon = Dragon.copy()
bottom_side_dragon.y += 20
play = True
while play == True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == KEYDOWN:
            if e.key == K_d:
               Dragon_fon = dragon_photo
            elif e.key == K_a:

                Dragon_fon = transform.flip(dragon_photo, True, False)

    keys = key.get_pressed()
    fon_full()
    window.blit(Dragon_fon, (Dragon.x, Dragon.y))

    if keys[K_1]:
        if green_dragon == True:
            if not dragon_r == 1:
                dragon_photo = transform.scale(image.load('photo/Dragon/Green Dragon/DinoSprites - Green1.png'),(50,50))
                dragon_r = 1
    elif keys[K_2]:
        if red_dragon == True:
            if not dragon_r == 2:
                dragon_photo = transform.scale(image.load('photo/Dragon/Red Dragon/DinoSprites - Red1.png'),(50,50))
                dragon_r = 2
    elif keys[K_3]:
        if red_dragon == True:
            if not dragon_r == 3:
                dragon_photo = transform.scale(image.load('photo/Dragon/Yelow Dragon/DinoSprites - Yelow1.png'),(50,50))
                dragon_r = 3
    elif keys[K_4]:
        if red_dragon == True:
            if not dragon_r == 4:
                dragon_photo = transform.scale(image.load('photo/Dragon/Blue Dragon/DinoSprites_Blue1.png'),(50,50))
                dragon_r = 4

    for block in blocks:
        block.show()

    if keys[K_f]:
        Dragon.x = start_x
        Dragon.y = start_y
    if keys[K_d]:
        bottom_side_dragon.x = Dragon.x
        right_side_dragon = Dragon.copy()
        right_side_dragon.x += 5
        right_side_dragon.height -= 10
        if not right_side_dragon.collidelistall(blocks):
            Dragon.x += speed
    elif keys[K_a]:
        bottom_side_dragon.x = Dragon.x
        left_side_dragon = Dragon.copy()
        left_side_dragon.x -= 5
        left_side_dragon.height -= 10
        if not left_side_dragon.collidelistall(blocks):
            Dragon.x -= speed



    bottom_side_dragon.y = Dragon.y
    if not bottom_side_dragon.collidelistall(blocks):
        Dragon.y += 2

    if not jump:
        if keys[K_w]:
            jump = True
    else:
        Dragon.y -= jump_size

        jump_size -= 0.5
        for block in blocks:
            if Dragon.colliderect(block.rect):
                jump = False
                jump_size = 10
                Dragon.y = block.rect.y - Dragon.height

    for block in blocks:
        if Dragon.colliderect(block):
            if block.type == 1:
                Dragon.x += 0
            elif block.type == 2:
                Dragon.x = start_x
                Dragon.y = start_y
                speed = 0
                tt = 60
            elif block.type == 3:
                if key_dore == True:
                   play = False
            elif block.type == 4:
                yelow_dragon = True
            elif block.type == 5:
                green_dragon = True
            elif block.type == 6:
                blue_dragon = True
            elif block.type == 7:
                red_dragon = True
            elif block.type == 8:
                key_dore = True
        else:
          Dragon.y += 0

    if Dragon.y >= 1000:
        Dragon.y = start_y - 10
        Dragon.x = start_x


    if speed == 0:
        if tt >= 0:
            if tt > 0:
                tt -= 1
            elif tt == 0 :
                speed = 5
    display.update()
    clock.tick(60)
print('you won')
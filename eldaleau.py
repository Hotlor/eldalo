# -*- coding: utf-8 -*-
import random, pygame
from pygame.locals import *

fenetre = pygame.display.set_mode((1080,720))
running = True
pos = (540,360)
img = pygame.image.load("10E.jpg").convert()
trigimg = pygame.image.load("10E.jpg").convert()
bg = pygame.image.load("bg.jpg").convert()
bg = pygame.transform.scale(bg,(1080,720))
pos = img.get_rect()

def coucou(img) :
    global bg
    fenetre.blit(bg,(0,0))
    fenetre.blit(img,(1080,445))
    position = img.get_rect()
    for event in pygame.event.get() :
        if event.type == KEYDOWN :
            if event.key == K_C:
                i=0
                while i<50 :
                    position=(position[0]-1,position[1])
                    fenetre.blit(img,position)
                    
    
    
while running:
    fenetre.blit(bg,(0,0))
    for event in pygame.event.get() :
        if event.type == MOUSEMOTION :
            pos = (event.pos[0],event.pos[1])
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            running = False      #On arrête la boucle
        '''if event.type == KEYDOWN :
            if event.key == K_LEFT:
                pos = pos.move(-30,0)
            if event.key == K_RIGHT:
                pos = pos.move(30,0)
            if event.key == K_UP:
                pos = pos.move(0,-30)
            if event.key == K_DOWN:
                pos = pos.move(0,30)'''
        
    fenetre.blit(img,pos)
    print (pos)
    pygame.display.flip()
# -*- coding: utf-8 -*-
import random, pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1080,720))

running = True

img = pygame.image.load("10E.jpg").convert()
trigimg = pygame.image.load("10E.jpg").convert()
fenetre.blit(trigimg,(1080,445))
fenetre.blit(img,(520,360))
posimg = img.get_rect()
postrigimg = trigimg.get_rect()

bg = pygame.image.load("bg.jpg").convert()
bg = pygame.transform.scale(bg,(1080,720))

posimg.move

def coucou() :
    global bg, trigimg, postrigimg
    fenetre.blit(bg,(0,0))
    #fenetre.blit(trigimg,(1080,445))
    i=0
    while i<50 :
        fenetre.blit(bg,(0,0))
        postrigimg=postrigimg.move(20,0)        
        fenetre.blit(trigimg,postrigimg)
        i+=1
        print(i,postrigimg)
    fenetre.blit(trigimg,(1080,445))
                    
pos = img.get_rect()
    
while running:

    
    for event in pygame.event.get() :
        #key = pygame.key.get_pressed
        '''if event.type == MOUSEMOTION :
            pos = (event.pos[0],event.pos[1])'''
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            running = False      #On arrête la boucle
        if event.type == KEYDOWN :
            if event.key == K_LEFT:
                posimg=posimg.move(-30,0)
                print (posimg)
                print ("left")
            if event.key == K_RIGHT:
                posimg=posimg.move(30,0)
                print (posimg)
            if event.key == K_UP:
                posimg=posimg.move(0,-30)
                print (posimg)
            if event.key == K_DOWN:
                posimg=posimg.move(0,30)
                print (posimg)
            if event.key == K_c:
                print("coucou")
                coucou()
                
        '''if testrect.collidelist(formosa.boxcollider) == -1:
                        angus.position.x -= 2
                        angus.collision.x -= 2'''
    
    fenetre.blit(bg,(0,0))
    fenetre.blit(img,posimg)
    pygame.display.flip()
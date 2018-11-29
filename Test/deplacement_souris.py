import pygame, sys
import time
from pygame.locals import *
from math import *
pygame.init()
xmax=400                                                                                   # La fenêtre et le fond aura une dimension (x,y)
ymax=300
grandeur_carre=10
fenetre = pygame.display.set_mode((xmax, ymax),RESIZABLE)                                     # Creation de la fenetre, taille modifiable
pygame.display.set_caption('Test!')                                                     # Titre de la fenêtre                
image_fond = pygame.image.load("Sol.jpg")                                               # Import de l'image de fond
fond = image_fond.convert()                                                             # Fond de même dimension que la fenêtre
fond = pygame.transform.scale(fond, (xmax, ymax))         
fenetre.blit(fond,(0,0))                                                                # On peut afficher des images sur le fond                            
noir = (0, 0, 0)
dimension_carre = [(xmax/2)+(grandeur_carre/2), (ymax/2)+(grandeur_carre/2), grandeur_carre, grandeur_carre]
coin_haut_gauche_carre=(0,0)
coin_haut_droite_carre=(10,0)
coin_bas_gauche_carre=(0,10)
coin_bas_droit_carre=(10,10)


pygame.draw.rect(fenetre, noir, dimension_carre)
"""
def incx_si_droite(actux,actuy,arrivx,arrivy):
    if (arrivx>actux):
            while (arrivx!= actux):
                fenetre.blit(fond,(0,0))
                pygame.draw.rect(fenetre, noir, (actux,actuy,grandeur_carre,grandeur_carre))
                actux=actux+grandeur_carre

def decx_si_gauche(actux,actuy,arrivx,arrivy):
    if (arrivx<actux):
            while (arrivx!= actux): 
                fenetre.blit(fond,(0,0))
                pygame.draw.rect(fenetre, noir, (actux,actuy,grandeur_carre,grandeur_carre))
                actux=actux-grandeur_carre
                
def incy_si_bas(actux,actuy,arrivx,arrivy):
    if (arrivy>actuy):
            while (arrivy!= actuy): 
                fenetre.blit(fond,(0,0))
                pygame.draw.rect(fenetre, noir, (actux,actuy,grandeur_carre,grandeur_carre))
                actuy=actuy+grandeur_carre
                
def decy_si_haut(actux,actuy,arrivx,arrivy):
    if (arrivy<actuy):
            while (arrivy!= actuy): 
                fenetre.blit(fond,(0,0))
                pygame.draw.rect(fenetre, noir, (actux,actuy,grandeur_carre,grandeur_carre))
                actuy=actuy-grandeur_carre
"""

def getPosition(x, y):
    if pygame.mouse.get_pressed()[0]:
        x=pygame.mouse.get_pos()[0]
        y=pygame.mouse.get_pos()[1]

    return x, y

def allervers(jx, jy, mx, my):
    vect = (mx - jx, my - jy)
    dist = sqrt(vect[0] ** 2 + vect[1] ** 2)
    if dist < 2.0:
        return jx, jy

    vectn = (vect[0] / dist, vect[1] / dist)
    speed = 0.05

    return jx + vectn[0] * speed, jy + vectn[1] * speed

def afficher(jx, jy):
    fenetre.blit(fond,(0,0))
    pygame.draw.rect(fenetre, noir, (jx, jy, grandeur_carre,grandeur_carre))

jx, jy = (xmax/2)+(grandeur_carre/2), (ymax/2)+(grandeur_carre/2)
mx, my = jx, jy
while True: # main game loop
    mx, my = getPosition(mx, my)
    jx, jy = allervers(jx, jy, mx, my)
    afficher(jx, jy)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
    pygame.display.update()




##import pygame, sys
##from pygame.locals import *
##pygame.init()
##x=400                                               # La fenêtre et le fond aura une dimension (x,y)
##y=300                       
##fenetre = pygame.display.set_mode((x, y),RESIZABLE) # Creation de la fenetre, taille modifiable
##pygame.display.set_caption('Test!')                 # Titre de la fenêtre                
##image_fond = pygame.image.load("Sol.jpg")           # Import de l'image de fond
##fond = image_fond.convert()                         # Fond de même dimension que la fenêtre
##fond = pygame.transform.scale(fond, (x, y))         
##fenetre.blit(fond,(0,0))                            # On peut afficher des images sur le fond                            
##noir = (0, 0, 0)
##dimension_carre= ((x/2)-5, (y/2)-5, 10, 10)
##pygame.draw.rect(fenetre, noir, dimension_carre)
##while True: # main game loop
##    pos = dimension_carre
##    if pygame.mouse.get_pressed()[0]:
##        pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
##        fenetre.blit(fond,(0,0))
##        pygame.draw.rect(fenetre, noir, (pos[0],pos[1],10,10))
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            sys.exit() 
##    pygame.display.update()

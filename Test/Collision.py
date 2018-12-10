import pygame, sys
import time
from pygame.locals import *
from math import *
pygame.init()
xmax=400                                                                                   # La fenêtre et le fond aura une dimension (x,y)
ymax=300
fenetre = pygame.display.set_mode((xmax, ymax),RESIZABLE)                                     # Creation de la fenetre, taille modifiable
pygame.display.set_caption('Test!')                                                     # Titre de la fenêtre                
image_fond = pygame.image.load("Sol.jpg")
fond = image_fond.convert()                                                             # Fond de même dimension que la fenêtre
fond = pygame.transform.scale(fond, (xmax, ymax))
fenetre.blit(fond,(0,0)) 

class Cercle:
    def __init__(self,pos,rayon):
        self.pos=pos
        self.rayon=rayon

class Rectangle:
    longueur = long_rect
    largeur = larg_rect
    def __init__(self,pos2,coordrect):
        self.pos2=pos2
        self.coordrect=coordrect


class Collision:
    def __init__(self,col):
        self.col=col

class Collision_Rectangle(Collision):
    def __init__(self,col2,rect):
        self.col=col2
        self.rect=rect
        
class Collision_Cercle(Collision):
    def __init__(self,col2,circle):
        self.col=col2
        self.circle=circle

##rayon=10
##coordrect=[10,10]
##pos=[650,406]
##pos2=[15,58]
##rouge=(255,0,0)
##vert=(0,255,0)
##pygame.draw.circle(fenetre, rouge, circle)
##pygame.draw.rect(fenetre, vert, rect)
##circle = Cercle(pos,rayon)
##rect = Rectangle(pos,coordrect)
##if Collision(col)==True and objet==circle:
##    choix=Collision_Cercle(Collision)(col2,circle)
##if Collision(col)==True and objet==rectangle:
##    choix=Collision_Rectangle(Collision)(col2,rect)
circle = Cercle(pos,rayon)
joueur = Cercle(pos,rayon)
rect = Rectangle(pos,coordrect)
coordrect=[10,10]
rayon=10
pos=[650,406]
pos2=[15,58]
situa_joueur=''
##player
##objets
##for obj in objets:
##    obj.testCollisionCercle(player)-->boolean



if (circle.pos - joueur.pos).length() < (circle.rayon + joueur.rayon):
    Collision == True

if (joueur.pos[0]+joueur.rayon)<rect.pos[0]:
    situa_joueur='gauche'
if (joueur.pos[0]-joueur.rayon)>rect.pos[0]+rect.largeur:
    situa_joueur='droite'
if (joueur.pos[1]+joueur.rayon)<rect.pos[1]:
    situa_joueur='haut'
if (joueur.pos[1]-joueur.rayon)>rect.pos[1]+rect.largeur:
    situa_joueur='bas'

if situa_joueur !='gauche' and situa_joueur !='droite' and situa_joueur !='haut' and situa_joueur !='bas': 
    Collision=True
    
    while True: # main game loop
        if Collision == True:
            pygame.draw.circle(fenetre, noir, (jx, jy),rayon)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
    pygame.display.update()
    




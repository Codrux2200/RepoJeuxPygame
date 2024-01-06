import pygame
from pygame.locals import *
import random

#Space Invaders LITE V 0.0.1


pygame.init()

ecran = pygame.display.set_mode((600,600))
ecran2= ecran.get_rect() #on va crée un rect de l'écran . sa va servir plus tard
monstre = pygame.image.load("space.png").convert_alpha()#on declare nos images et on les converties
monstre2 = pygame.image.load("space.png").convert_alpha()#on declare nos images et on les converties
monstre3 = pygame.image.load("space.png").convert_alpha()#on declare nos images et on les converties
monstre4 = pygame.image.load("space.png").convert_alpha()#on declare nos images et on les converties
image2 = pygame.image.load("k.png").convert_alpha()#on declare nos images et on les converties
rect=image2.get_rect() # pour gérer les collisions on a besoin d'une hitbox or on peut facilement verifier la collision entre 2 rect
#donc notre hitbox sera un rect noir (donc invisible) deriiere l'image et avec la meme taille.
rect3=monstre.get_rect()
rectmonstre2= monstre2.get_rect()
rectmonstre3= monstre3.get_rect()
rectmonstre4= monstre4.get_rect()
x=500 
y=400
x1=200
y1=255
x2=20
y2=250
px1=600
py1=0
rect2=(x1,y1,3,5) #On crée les rects des projectiles 
pro1=(py1,px1,3,5) #On crée les rects des projectiles 
centre=(y,x)
couleur=(0,255,0)
continuer = True
n=0
s=0
s2=0
r=0
noire=(0,2,0)
t=0
verrif=False
m1=True #mn avec 1<=n<=4 c'est un bool qui prend False quand un monstre est touché par notre projectile  
m2=True
m3=True
m4=True
y3=y2-80 # on crée les y des monstres avec 80 pixels entre 1 monstre et un autre
y4=y3-80
y5=y4-80
v=-1
compa=[y2,y3,y4,y5] #on crée une liste contenant touts les y des monstres
while continuer:
    compa=[y2,y3,y4,y5]# on le declare ici aussi car les y change tout le temps de valeur (les monstres bougent)
    
    if m1==False: # a chaque fois qu'un monstre va mourrir alors on supprime son y de la liste
        compa.remove(y2)
    
    if m2==False:
        compa.remove(y3)
        
    if m3==False:
        compa.remove(y4)
        
    if m4==False:
        compa.remove(y5)
        
    
    pygame.time.Clock().tick(120) #60 FPS
    centre=(y,x)# Tuple
    ecran.fill((0,0,0))# a chaque tour on remet l'ecran en noir (et hop on a supprimé les doublons) 
    x1=x1+5# on fait avancer le projectile rouge (ceux des mechants monstres)
    print(compa)# pour le test
    
    
    if(x1==600): # si le projectile rouge arrive tout en bas 
        x1=x2+10 # on le replace en dessous du monstre
        i=random.randint(0,int(len(compa)-1)) # on choisis un y au hassard parmi ceux encore dispo
        #dans la liste 
        y1=compa[i] # et on l'attribue au y du projectile rouge
              
        
        
    rect2=(y1,x1,3,5) # comme les images sont en mouvement alors on redeclare tout ici
    pro1=(py1,px1,3,5)
    pygame.draw.rect(ecran,(255,0,0),rect2)
    rect=image2.get_rect()
    rect3=monstre.get_rect()
    rectmonstre2= monstre2.get_rect()
    rectmonstre3= monstre3.get_rect()
    rectmonstre4= monstre4.get_rect()
    
    if(y5==0): # sa gére les mouvement des monstres je te laisse decrypter (Bonne chance)
        n=1
        x2=x2+20
        
    if(y2>500):
        n=2
        
        
    if(n==1):
        y2=y2+1
       
    else:
        y2=y2-1
        
    
    
    keyboard = pygame.key.get_pressed() # on verifie si une touche est préssé
    if keyboard[K_LEFT]: #si c'est gauche 
        y=y-10 # le vaisseaux a gauche
    if keyboard[K_RIGHT]:#tu a compris
        y=y+10# Pareil
        
    for event in pygame.event.get(): # la on verifie les appuie simple 
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:# si on appuie sur espace
                s=1
                r=1
                couleur=(0,255,0)# on met la projectile en vert
            
     
    if px1!=0 and px1!=600: #on verifie que le projectile est deja tiré si c'est le cas on bloque les tirs
        r=0
            
    if r==1: #si on autorise le tir
        py1=y 
        px1=530
        r=0 #on bloque
        
    if s==1:
        
        px1=px1-5
        if(px1==0):
            px1=600 
            s=0
                
    y3=y2-80
    y4=y3-80
    y5=y4-80
    
    #Si desous des lignes et des lignes de déclarations et d'affichage 
    rect3 = rect3.move(y2,x2).clamp(ecran2)
    ecran.blit(monstre, rect3) # on affiche le monstre dessus rect3 qui sera sa hitbox 
    
    rectmonstre2 = rectmonstre2.move(y3,x2).clamp(ecran2)
    ecran.blit(monstre2, rectmonstre2)
    
    
    
    rectmonstre3 = rectmonstre3.move(y4,x2).clamp(ecran2)
    ecran.blit(monstre3, rectmonstre3)
    
    
    rectmonstre4 = rectmonstre4.move(y5,x2).clamp(ecran2)
    ecran.blit(monstre4, rectmonstre4)
    
    rect = rect.move(y,x).clamp(ecran2)
    ecran.blit(image2, rect)
    
    pygame.draw.rect(ecran,couleur,pro1)
    
    
    
    # Ici on verifie les colisions
    
    
    if rect.colliderect(rect2) :
        pygame.quit()
        
    if rect3.colliderect(pro1) and m1: # si mon projectile touche un monstre
        m1=False
        v=v+1
        monstre.fill((0,0,0)) # on le passe en noir on ne le SUPPRIME SUUUURRTOOUUUTTT PAS sinon sa va foutre la merde
        couleur=(0,0,0) # le projectile devient en noir
        pygame.display.flip()
        


        
    if rectmonstre2.colliderect(pro1) and m2:
        m2=False
        v=v+1
        monstre2.fill((0,0,0))
        couleur=(0,0,0)

    
        
        
    if rectmonstre3.colliderect(pro1) and m3:
        m3=False
        v+=1
        monstre3.fill((0,0,0))
        couleur=(0,0,0)
        
        
       

        
    if rectmonstre4.colliderect(pro1) and m4:
        v+=1
        m4=False
        monstre4.fill((0,0,0))
        couleur=(0,0,0)
        
        
    if rect3.colliderect(rect) or rectmonstre2.colliderect(rect) or rectmonstre3.colliderect(rect) or rectmonstre4.colliderect(rect):
        # si 1 des monstres touche physiquement le vaisseaux c'est perdu
        pygame.quit()
       
    
    if m1==False and m2==False and m3==False and m4==False : # si tout le monde est mort alors on ferme
        pygame.quit()
        
        
    pygame.display.flip()

pygame.quit()

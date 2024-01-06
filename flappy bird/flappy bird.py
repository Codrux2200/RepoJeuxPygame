import pygame
import random
pygame.init()
surface= pygame.display.set_mode((600,600)) 
continuer=True
flappy=pygame.image.load("flappy.png")
surface.fill((0,0,150))
x=300
y=50
v=1
t=300
f=600
a=t-150
p=300
mur=(p, 0, 70, a)
mur2=(p, t, 70, f)
position=(x,y)
listeblock=[300]
pygame.display.set_caption("Flappy Bird speed code projets 3H")
listeblock2=[]
listeblock3=[]
pygame.display.set_icon(flappy)
listet=[200]
listepos=[200,300,400,500,600]
listepos2=[200,300,400]
calibri_font = pygame.font.SysFont("Arial",70)
space=False
compteur=0
on=True
while continuer==True:
    
    
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space=True 
                
    
    
    print(listeblock)
    
    if -50 in listeblock[1:]:
        compteur+=1
    
  
    if listeblock[0]== p-250 or on==True:
        p=500
        listeblock.insert(0,p)
        g=random.randint(0,len(listepos)-1)
        t=listepos[g]
        print(t)
        listet.insert(0,t)
        mur=(p, 0, 70, t-150)
        mur2=(p, t, 70, f)
        listeblock2.insert(0,mur)
        listeblock3.insert(0,mur2)
        on=False
        
    for i in range(len(listeblock)):
        del listeblock2[i-1]
        del listeblock3[i-1]
        listeblock[i]-=1
        mur=(listeblock[i], 0, 70, listet[i]-150)
        mur2=(listeblock[i], listet[i], 70, f)
        listeblock2.insert(i+1,mur)
        listeblock3.insert(i+1,mur2)
    
    
    for e in range(len(listeblock2)):
        pygame.draw.rect(surface,(0,255,0),listeblock2[e])
        pygame.draw.rect(surface,(0,255,0),listeblock3[e])
    
    
    if space==False: # si je n'appuis pas sur espace le flappy tombe
        y=y+3
    elif space==True:# sinon il saute
        pygame.time.Clock().tick(40)# on ralentie le jeux
        y=y-60
        space=False
        
    argent_text_surface = calibri_font.render(str(compteur),True,(255,255,255))
    surface.blit(argent_text_surface, (450,50))    
    position=(10,y)
    rect=pygame.Rect((position),(48,48))
    surface.blit(flappy,position)
    pygame.display.flip()
    surface.fill((0,0,150))
    
    if rect.collidelist(listeblock2)!= -1 or rect.collidelist(listeblock3) != -1: # si il y a contact c'est perdu
        continuer=False
    
    
        
pygame.quit()
    
    

#ceci est ma version du code v 0.0.1


import pygame #on import les librairies
import random

pygame.init() #on init pygame
screen=pygame.display.set_mode((600,600)) # fenetre en 600 par 600
continuer=True
x=300 # une variable qui va stocké les coordonées en x du serpent
y=300 # variable qui stock les coordonées en y du serpent
a=(300,300)#variable de type tuple pour plus tard ;)
x1=10*random.randint(2,59)# les coordonées en x pour la pomme en aléatoire et en multiple de 10 (2 en minima pour eviter qu'elle soit out du jeux apres les bordures)
y1=10*random.randint(2,59)# les coordonées en y pour la pomme en aléatoire et en multiple de 10 (2 en minima pour eviter qu'elle soit out du jeux apres les bordures)
direction="haut" # la meme chose que pour le code de Courbon
n=0 # un truc a la con
s=0
# trés utile tu va voir
v=2 # argghhhhh tuple != 0 donc variable a la con mais essentielle
pos1=[] # on génére des listes quand meme car sa va servir 
pos=[]
posb=[]
while continuer:# tu connais les bails :)
    time=v/2*10 # on crée une variable time pour que le temps s'accelere avec les prises de pommes et on prend v comme variable pour le calcul car il depend directement tu nombre de pommes
    pygame.time.Clock().tick(time) # on applique time au temps de base
    pygame.draw.circle(screen,(0,255,0),(x,y),5)#on dessine le cercle du serpent en vert
    pygame.draw.circle(screen,(0,0,0),a,5)# c'est notre cache misére tu verras donc en noir
    pygame.draw.circle(screen,(255,0,0),(x1,y1),5) # Les pommes en rouge
    pos1.insert(0,(x1,y1)) #pos1 stock toutes les positions des pommes
    pos.insert(0,(x,y)) # pos stock toutes les positions des cercles qui constituent le serpent 
    posb.insert(0,a)
    if(n==2): # on verifie si n=2 juste pour etre sur que le while a fait 1 tour sinon il crash   
        a=pos[s]# sa c'est super important . En gros s c'est le nombre de pomme que j'ai bouffé et donc en faite j'ai crée 2 serpent qui se superposent 1 en vert et l'autre en noir (le cache misére quoi) . Quand le serpent mange une pomme, le noir se decale de 1 cercle vers l'arriere donc la case redevient verte 
        
    if pos1[0]==pos[0]: #si la pomme touche la tete du serpent alors
        s=s+1 
        v=s+1
        screen.fill((0,0,0))# on efface l'écran (pas vraiment on le repeint en noir en faite)
        del pos[s:]# comme on ne fait que le repeindre du coup il peut y avoir des collisions temps que le jeux n'est pas terminé avec des éléments caché donc on reduit pos[] au maximum s etant le nombre de cercle que constitue le serpent a un instant T
        x1=10*random.randint(2,59) # on change les coordonées de la pomme 
        y1=10*random.randint(2,59)
   
    if x==600 or x==0 or y==600 or y== 0: # comme les coordonées c'est de simple int donc on peut facilement verifier les bordures donc quand x ou y se rapproche d'un bord on coupe le jeux
        pygame.quit()
    
    
    if pos[0] in pos[1:]: # ici on va gérer les collisions . ici je verifie que pos[0] donc la tete ne soit pas deja dans pos[1:] ou encore pos[len(pos)]-pos[0] si tu prefere   
        pygame.quit() # si c'est le cas il y a eu coollisions donc c'est fini
    else:
        del pos[v:] # sinon et comme mon serpent ne doit reagir a une collision qu'avec sa partie verte et qu'elle augmente de 1 a chaque pomme alors je supprime de pos[] le surplus et je garde l'essentielle qui accroit avec le nombre de pomme d'ou v
        # mais pq v est pas s?? car pos[v:] ne doit jamais etre = 0 sinon sa crash et donc il doit avoir un nombre de coordonées stockées n+1 par apport au nombre de pommes mangées.
        #Exemple je mange 2 pommes . J'ai alors un serpent à 3 cercles (2 des pommes + 1 du depart) et bien pour que sa marche je doit avoir stocké 4 variables car p[0] compte.  
        
    if(direction=="haut"):
        y=y-10
    elif(direction=="left"):
        x=x-10
    elif(direction=="right"):
        x=x+10 
    elif (direction=="down"):
        y=y+10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction="haut"
            if event.key == pygame.K_LEFT:
                direction="left"
            if event.key == pygame.K_RIGHT:
                direction="right"
            if event.key == pygame.K_DOWN:
                direction="down"
    n=2
    pygame.display.flip()
    
    
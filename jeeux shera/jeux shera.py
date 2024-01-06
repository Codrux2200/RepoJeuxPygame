import pygame
pygame.init()
fenetre = pygame.display.set_mode( (816,816) )
pygame.display.set_caption("Celeste")
position=(0,200)
positionp=(300,497)
save=0
x=0
arial24 = pygame.font.SysFont("arial",24)
v=True
point=(200,400)
suivi=pygame.Rect((point[0]-7,point[1]-7),(25,25))
t=1.5
seconde=0
time=0
dirrection="nul"
listeblock=[]
listenoir=[]
listeblanc=[]
niveau=["n1.txt","n2.txt"]
v=0
continuer=True
def screen(x):# note que x est ici en argument
    fenetre.fill((0,100,120))# on remet tout en noir pour evité la superposition # oublie
    
    global position,listenoir,listeblanc
    listenoir=[]# on intégre dans notre def la variable position qui est un tuple qui fixe la position des blocks en x,y
    while x<8: #pour cette exemple notre ecran de jeux est divisé en blocks de 17 donc on crée un while qui va s'executer tant que il reste des lignes a lire
        with open(niveau[v]) as f: #on ouvre notre fichier text
            for line in f.readlines()[x]:#on lit tout les caractére de la x ieme ligne du fichier

                if line=="0": #si le caractére et 0
                    position=(position[0]+48,position[1])
          
                if line=="2": #si le caractére et 0
                    rect=pygame.Rect((position),(48,48))
                    pygame.draw.rect(fenetre,(0,0,0),rect)
                    position=(position[0]+48,position[1])
                    if rect not in listeblanc:
                        listenoir.insert(0,rect)# on crée un trou car pas de block
                if line=="1":# sinon si c'est un 1
                    rect=pygame.Rect((position),(48,48))# on dessine le rect a la bonne position
                    position=(position[0]+48,position[1])# on avance ensuite position de 48px(la taille du blocks) sinon le block qui va suivre va etre au dessus de celui la
                    # et sa serait dommage
                    pygame.draw.rect(fenetre,(0,255,0),rect)# on dessine le block sur l'ecran
                    listeblock.insert(0,rect)# on le rajoute dans une liste pour pouvoir faire un rect.collidelist(listeblock) apres


        position=(0,position[1]+48)# une fois la ligne terminé on rajoute 48 px en y cette fois si pour desendre
        x+=1# on rajoute 1 a x pour passer a la ligne suivante sur le fichier
    position=(0,200)
    for r in range(len(listeblanc)):
        pygame.draw.rect(fenetre,(0,0,255),listeblanc[r])# quand tout est finit position repasse a 0 pour que sa merde pas quand je vais reappeller la def .
    pygame.draw.circle(fenetre, (255,255,255),point, 20)
    # si je fais pas sa alors position aurra garder comme position le dernier blocks et donc il va dessiner en dehors de notre écran
    return listeblock #on recuppere notre fameuse liste de rect
clock = pygame.time.Clock()
def direction():
    
    
    global dirrection,point,liste,suivi,listenoir,listeblanc,time,seconde
    pygame.draw.circle(fenetre, (255,255,255),point, 20)
    suivi=pygame.Rect((point[0]-7,point[1]-7),(25,25))
    
    if suivi.collidelist(listenoir)!=-1 and listenoir[suivi.collidelist(listenoir)] not in listeblanc  :
        listeblanc.insert(0,listenoir[suivi.collidelist(listenoir)])
        del listenoir[suivi.collidelist(listenoir)]
    

    
    if len(listenoir)==0:
        pygame.quit()

                
    
    if dirrection=="nul":
        while dirrection=="nul":
            tick()
            print("sa marche")
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        dirrection="haut"
                    elif event.key == pygame.K_LEFT:
                        dirrection="gauche"
                    elif event.key == pygame.K_RIGHT:
                        dirrection="droite"
                    elif event.key == pygame.K_DOWN:
                        dirrection="bas"
                
        
    elif dirrection=="haut":
        if suivi.collidelist(liste)==-1:
            point=(point[0],point[1]-2)
        else:
            point=(point[0],point[1]+10)
            dirrection="nul"
            
    elif dirrection=="bas":
        if suivi.collidelist(liste)==-1:
            point=(point[0],point[1]+2)
        else:
            point=(point[0],point[1]-10)
            dirrection="nul"
            
    elif dirrection=="gauche":
        if suivi.collidelist(liste)==-1:
            point=(point[0]-2,point[1])
        else:
            point=(point[0]+15,point[1])
            dirrection="nul"
            
    elif dirrection=="droite":
        if suivi.collidelist(liste)==-1:
            point=(point[0]+2,point[1])
        else:
            point=(point[0]-15,point[1])
            dirrection="nul"
            
        

def tick():
    global time,seconde,clock,v,listeblanc
    clock.tick(60)
    time=time+1
    if time==60:
        time=0
        seconde+=1
    screen(0)
    arial2 = arial24.render("il te reste :"+str(seconde)+" secondes",True,(255,255,255))
    fenetre.blit(arial2, (600,30))
    
    if seconde==30:
        seconde=0
        del listeblanc[1:]
        print("perdu")  
        v=v+1
    pygame.display.flip()
    return seconde

while continuer:
    liste=screen(0)
    secondes=tick()# on execute la def qui dessine les blocks avec comme argument 0
    direction()
    print(secondes)

    
    #pygame.draw.rect(fenetre,(255,150,0),suivi)
    
    
        

    
    
    pygame.display.flip()


pygame.quit()

#Copyright Saad Berrada
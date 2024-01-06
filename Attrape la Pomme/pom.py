# -*- coding: utf-8 -*-

import pygame
import random

pygame.init() # initialisation du module "pygame"
vitesse=8
fenetre = pygame.display.set_mode( (600,600) ) # Création d'une fenètre graphique de taille 600x600 pixels
pygame.display.set_caption("Attrape la Pomme") # Définit le titre de la fenètre
calibri_font = pygame.font.SysFont("Arial",70)
# Chargement des images:
# On définit et affecte les variables qui contiendront les images de la pomme et du panier
imagePomme = pygame.image.load("pomme.png")
imagePanier = pygame.image.load("panier.png")
imagePanier = pygame.transform.scale(imagePanier, (128, 128)) # On redimensionne l'image du panier à une taille de 64x64 pixels
imagePomme = pygame.transform.scale(imagePomme, (64, 64)) # On redimensionne l'image de la pomme à une taille de 16x16 pixels

# On définit les variables qui contiendront les positions des différents éléments (pomme, panier)
# Chaque position est un couple de valeur '(x,y)'
positionPanier = (300,460)
positionPomme = (300,10)
toucher=False
point=True
compteur=0
# Fonction en charge de dessiner tous les éléments sur notre fenêtre graphique.
# Cette fonction sera appelée depuis notre boucle infinie

def dessiner():
    global imagePanier, imagePomme, fenetre, positionPomme, positionPanier,toucher,calibri_font,compteur,point,vitesse
    # On remplit complètement notre fenêtre avec la couleur noire: (0,0,0)
    # Ceci permet de 'nettoyer' notre fenètre avant de la déssiner
    fenetre.fill( (0,0,0) ) # On dessine l'image du Panier à sa position
    rectimage=pygame.Rect(positionPanier[0]+4,positionPanier[1]+62,120,80)
    rectbut=pygame.Rect(positionPanier[0]+20,positionPanier[1]+62,85,80)
    if not positionPomme == (-1,-1):
        rectpomme=pygame.Rect(positionPomme[0]+4,positionPomme[1],62,64)
        fenetre.blit(imagePomme, positionPomme)
        
    if  toucher==True:
        positionPomme = (random.randint(64,(600-64)),-100)
        toucher=False

    
    
    
    if rectbut.colliderect(rectpomme):
        compteur+=1
        vitesse+=1
        toucher=True

        



    argent_text_surface = calibri_font.render(str(int(compteur/2)),True,(255,255,255))
    fenetre.blit(argent_text_surface, (450,50))    # On dessine l'image de la pomme à sa position
    fenetre.blit(imagePanier, positionPanier)
    
    pygame.display.flip() # Rafraichissement complet de la fenêtre avec les dernières opérations de dessin


# Fonction en charge de gérer les évènements claviers
# Cette fonction sera appelée depuis notre boucle infinie
def gererClavierEtSouris():
    global continuer, positionPanier, positionPomme,toucher,vitesse
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            continuer = False
    # Gestion du clavier: Quelle touches sont appuyées ?
    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_RIGHT] == True:
        positionPanier = ( positionPanier[0] + 10 , positionPanier[1] )
       
    if touchesPressees[pygame.K_LEFT] == True:
       
        positionPanier = ( positionPanier[0] - 10 , positionPanier[1] )
    print(positionPomme)
    
    
    if positionPanier[0]>470:
        positionPanier = (470 , positionPanier[1])
        
        
    if positionPanier[0]<0:
        positionPanier = (0 , positionPanier[1])
    
    if positionPomme[1] > 600:
        toucher=True
        

# On crée une nouvell horloge qui nous permettra de fixer la vitesse de rafraichissement de notre fenêtre
clock = pygame.time.Clock()

# La boucle infinie de pygame:
# On va continuellement dessiner sur la fenêtre, gérer les évènements et calculer certains déplacements
continuer = True
while continuer:
    # pygame permet de fixer la vitesse de notre boucle:
    # ici on déclare 50 tours par secondes soit une animation à 10 images par seconde
    clock.tick(30)

    dessiner()
    gererClavierEtSouris()

    # On fait avancer le projectile (si il existe)
    positionPomme = (positionPomme[0], positionPomme[1] + vitesse) # le projectile "tombe" du haut de la fenètre



## A la fin, lorsque l'on sortira de la boucle, on demandera à Pygame de quitter proprement
pygame.quit()

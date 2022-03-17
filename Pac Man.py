import pygame
from pygame.locals import *

#images
image_fond = "images/FOND.png"
image_mur = "images/module.png"
image_point = "images/point.png"
image_cerise = "images/cerise.png"
image_pbonus = "images/pointbonus.png"

######CLASSSS

class Joueur :
    
    def __init__(self):
        self.image = pygame.image.load('images/pacman.png')
        self.dir = ""
        self.score = 0
        self.position = 10,15
        self.etat = 0
        
    def deplacer(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if sprite == '0':
                self.position = (x,y+1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if sprite == '0':
                self.position = (x,y-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if sprite == '0':
                self.position = (x-1,y)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            print('*')
            self.position = (x+1,y)
    
    def marquer(self):
        if self.position == 0:
            self.score+=1
        return self.score

class Laby :
    def __init__(self,carte) :
        """crée un labyrinthe à partir du fichier texte carte"""
        with open(carte, "r") as fichier:
            structure_niveau = []
            #On parcourt les lignes du fichier
            for ligne in fichier:
                ligne_niveau = []
                #On parcourt les sprites (lettres) contenus dans le fichier
                for sprite in ligne:
                    #On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        #On ajoute le sprite à la liste de la ligne
                        ligne_niveau.append(sprite)
                #On ajoute la ligne à la liste du niveau
                structure_niveau.append(ligne_niveau)
        self.tableau = structure_niveau #tableau contenant le labyrinthe avec des 'd', '0', 'a' ou 'm'

        #calcul des dimensions de la fenetre graphique
        self.largeur = len(structure_niveau[0])
        self.hauteur = len(structure_niveau)

        
    def afficher(self) :
        global sprite
        """Fonction permettant d'afficher le niveau en fonction 
        de la liste de l'attirbut tableau """
        #Chargement des images (seule celle d'arrivée contient de la transparence)
        #On parcourt la liste du niveau
        fond = pygame.image.load(image_fond).convert()
        mur = pygame.image.load(image_mur).convert()
        point = pygame.image.load(image_point).convert_alpha()
        cerise = pygame.image.load(image_cerise).convert_alpha()
        pbonus = pygame.image.load(image_pbonus).convert_alpha()
        fenetre.blit(fond,(0,0))
        num_ligne = 0
        for ligne in self.tableau:
        #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
            #On calcule la position réelle en pixels
                x = num_ligne * taille_sprite
                y = num_case * taille_sprite
                if sprite == '1':   #1 = Mur
                    fenetre.blit(mur, (y,x))
                if sprite == '0':   #0 = point
                    fenetre.blit(point, (y,x))
                if sprite == 'C':   #C = Cerise
                    fenetre.blit(cerise, (y,x))
                if sprite == 'P':   # = point bonus
                    fenetre.blit(pbonus, (y,x))
                num_case += 1
            num_ligne += 1

#main
image_fond = "images/FOND.png"
image_mur = "images/module.png"
image_point = "images/point.png"
#image_depart = "images/depart.png"
#image_perso = "images/perso.png"
pygame.init()
laby = Laby("MAPv1.txt") #on envoie le fichier niveau de labyrinthe
taille_sprite = 30
fenetre = pygame.display.set_mode(size=(630, 630))
pygame.display.set_caption('PAC MAN')
programIcon = pygame.image.load('images/icon.png')
pygame.display.set_icon(programIcon)
continuer = 1
laby.afficher()
pygame.display.flip()
joueur = Joueur()

while continuer :
    laby.afficher()
    
    for event in pygame.event.get():
        #Si l'utilisateur quitte, on met la variable qui continue le jeu
        #ET la variable générale à 0 pour fermer la fenêtre
        if event.type == QUIT:
            continuer = 0
        
        joueur.deplacer(event)
    x = joueur.position[0] * taille_sprite
    y = joueur.position[1] * taille_sprite
    fenetre.blit(joueur.image, (x,y))
    pygame.display.flip()
                    
    
pygame.quit()
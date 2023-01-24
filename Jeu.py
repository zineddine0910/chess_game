import pygame
import Plateau

def main():

    grille = Plateau.Plateau()
    grille.affichage()

    # for i in range(8):
    #     for j in range(8):
    #         print(i, end=" , ")
    #         print(j, end=" : ")
    # print(grille.coups_possibles((0,1)))

    pygame.init()
    ecran = pygame.display.set_mode((640,640))
    case1 = None
    case2 = None
    joueur_actuel = "blanc"
    boucle_du_jeu = True
    while boucle_du_jeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle_du_jeu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x = x//80
                y = y//80
                # print("Coordonnées de la souris: ", y, x)
                # print(grille.coups_possibles((y,x))) 
                if case1 == None:
                    case1 = y, x
                else:
                    case2 = y, x
                print(case1)
                print(case2)
                print("----------")
                if (case1 != None and case2 != None):
                    if(joueur_actuel == grille.affiche_couleur(case1)):
                        if(case2 in grille.coups_possibles(case1)):
                            grille.coup(case1, case2)
                            grille.affichePlateau(ecran)
                            if joueur_actuel == "blanc":
                                joueur_actuel = "noir"
                            else: joueur_actuel = "blanc"
                        else: print("jamais")
                    else: print("mauvais_joueur")
                    case1 = None
                    case2 = None
        ecran.fill((205, 133, 63))
        grille.affichePlateau(ecran)
        #grille.change_couleur(ecran)
        pygame.display.update()

    pygame.quit()
    

main()

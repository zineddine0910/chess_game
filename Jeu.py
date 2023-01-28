import pygame
import Piece
import Plateau
import copy

def main():
    grille = Plateau.Plateau()
    # grille.affichage()
    # grille.inverse_plateau()
    # print("-----------------------------------------------------------")
    # grille.affichage()
    # for i in range(8):
    #     for j in range(8):
    #         print(i, end=" , ")
    #         print(j, end=" : ")
    # print(grille.coups_possibles((0,1)))

    pygame.init()
    ecran = pygame.display.set_mode((640,700))
    case1 = None
    case2 = None
    joueur_actuel = "blanc"
    choix = []
    font = pygame.font.Font(None, 30)
    button_rect = pygame.Rect(0, 650, 30, 30)
    boucle_du_jeu = True
    
    
    while boucle_du_jeu:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle_du_jeu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                # Effectuer une action lorsque le bouton est cliqué
                    grille.inverse_plateau()
                    grille.annuler_coup()
                    joueur_actuel = "noir" if joueur_actuel == "blanc" else "blanc"
                    # grille.annuler_coup()
                    choix = []
                    continue
                else:
                    x, y = event.pos
                    x = x//80
                    y = y//80
                    if(x < 0 or y < 0 or x > 7 or y > 7): 
                        continue
                    # print("Coordonnées de la souris: ", y, x)
                    # print(grille.coups_possibles((y,x))) 
                    if case1 == None:
                        case1 = (y, x)
                        if(grille.affiche_couleur(case1) != joueur_actuel):
                            print("mauvais_joueur")
                            case1 = None
                        else:                     
                            choix = grille.coups_possibles(case1)
                            if (not choix):
                                case1 = None
                            if(grille.getGrille()[y][x].getNom() == "roi"):
                                grille.getGrille()[y][x] = None
                                choix = grille.enleve_cases_roi(choix, joueur_actuel)
                                grille.getGrille()[y][x] = Piece.Piece("roi", joueur_actuel)
                    else:
                        case2 = y, x
                    # print(case1)
                    # print(case2)
                    # print("----------")
                    if (case1 != None and case2 != None):
                        if(case2 in choix):
                            grille.coup(case1, case2)
                            if(grille.roi_en_echec(joueur_actuel) == True):
                                grille.annuler_coup()
                                print("coup annulé")
                            else:
                                joueur_actuel = "noir" if joueur_actuel == "blanc" else "blanc"
                                grille.inverse_plateau()
                                # grille.coup_IA()
                                # if(grille.roi_en_echec("noir") == True):
                                #     grille.annuler_coup()
                                #     print("coup annulé")
                                # else:
                                #     joueur_actuel = "blanc"  
                                if grille.roque_blanc_a_gauche and grille.roque_blanc_a_droite:
                                    print ("roque possible blanc")
                                elif grille.roque_blanc_a_gauche == True:
                                    print ("roque possible blanc gauche")
                                elif grille.roque_blanc_a_droite == True:
                                    print ("roque possible blanc droite")
                                else:
                                    print ("roque plus possible")

                        else: print("jamais")
                        choix = []
                        case1 = None
                        case2 = None
                    
        ecran.fill((205, 133, 63))
        grille.affichePlateau(ecran, choix)
        grille.verif_echec_et_mat_noir()
        if( grille.echec_et_mat_noir == True):
            text = font.render("Les blancs ont gagné", True, (0, 0, 0))
            ecran.blit(text, (200, 650))
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        grille.verif_echec_et_mat_blanc()
        if(grille.echec_et_mat_blanc == True):
            text = font.render("Les noirs ont gagné", True, (0, 0, 0))
            ecran.blit(text, (200, 650))
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        if(grille.match_nul == True):
            text = font.render("Match nul!", True, (0, 0, 0))
            ecran.blit(text, (200, 650))
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        pygame.draw.rect(ecran, (0, 0, 0), button_rect)
        button_text = font.render("", True, (255, 255, 255))
        ecran.blit(button_text, (0, 750))
        pygame.display.update()

    pygame.quit()
    

main()

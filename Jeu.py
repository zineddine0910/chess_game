import pygame
import Plateau

def main():

    grille = Plateau.Plateau()
    grille.affichage()

    # for i in range(8):
    #     for j in range(8):
    #         print(i, end=" , ")
    #         print(j, end=" : ")
    #         print(grille.coups_possibles((i,j)))

    pygame.init()
    ecran = pygame.display.set_mode((640,640))

    boucle_du_jeu = True
    while boucle_du_jeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle_du_jeu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x = x//80
                y = y//80
                print("Coordonnées de la souris: ", y, x)
                print(grille.coups_possibles((y,x))) 
        ecran.fill((205, 133, 63))
        grille.affichePlateau(ecran)
        pygame.display.update()

    pygame.quit()
    

main()

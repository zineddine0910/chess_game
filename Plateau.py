import Piece
import pygame

class Plateau:

    grille = [[None for i in range(8)] for j in range(8)]

    def __init__(self):

        # initialisation pieces blanches

        self.grille[7][0] = Piece.Piece("tour", "blanc")
        self.grille[7][1] = Piece.Piece("cavalier", "blanc")
        self.grille[7][2] = Piece.Piece("fou", "blanc")
        self.grille[7][3] = Piece.Piece("reine", "blanc")
        self.grille[7][4] = Piece.Piece("roi", "blanc")
        self.grille[7][5] = Piece.Piece("fou", "blanc")
        self.grille[7][6] = Piece.Piece("cavalier", "blanc")
        self.grille[7][7] = Piece.Piece("tour", "blanc")

        # initialisation pieces noires

        self.grille[0][0] = Piece.Piece("tour", "noir")
        self.grille[0][1] = Piece.Piece("cavalier", "noir")
        self.grille[0][2] = Piece.Piece("fou", "noir")
        self.grille[0][3] = Piece.Piece("reine", "noir")
        self.grille[0][4] = Piece.Piece("roi", "noir")
        self.grille[0][5] = Piece.Piece("fou", "noir")
        self.grille[0][6] = Piece.Piece("cavalier", "noir")
        self.grille[0][7] = Piece.Piece("tour", "noir")

        # initialisation des pions

        for i in range(8):
            self.grille[1][i] = Piece.Piece("pion", "noir")
            self.grille[6][i] = Piece.Piece("pion", "blanc")

        # self.grille[1][1] = None
        # self.grille[6][4] = None
        # self.grille[0][1] = Piece.Piece("reine", "blanc")

    def getGrille(self):
        return self.grille

    def affichePlateau(self,ecran):
        for i in range(8):
            for j in range(8):
                if ((i%2 == 0) and (j%2 == 0)) or ((i%2 == 1) and (j%2 == 1)):
                    pygame.draw.rect(ecran, (255, 255, 255), (i*80, j*80, 80, 80))

        for i in range(8):
            for j in range(8):
                if self.grille[i][j] == None : continue
                image = pygame.image.load("src/"+self.grille[i][j].getNom()+"_"+self.grille[i][j].getCouleur()+".png")
                image = pygame.transform.scale(image, (image.get_width()/8, image.get_height()/8))
                if self.grille[i][j].getNom() == "pion" :
                    ecran.blit(image, (j*80+20, i*80+8))
                elif self.grille[i][j].getNom() == "reine" :
                    ecran.blit(image, (j*80+8, i*80+8))
                elif self.grille[i][j].getNom() == "roi" :
                    ecran.blit(image, (j*80+10, i*80+8))
                elif self.grille[i][j].getNom() == "tour" :
                    ecran.blit(image, (j*80+14, i*80+8))
                else:
                    ecran.blit(image, (j*80+20, i*80+8))
        pygame.display.flip()

    def change_couleur(self, ecran):
        pygame.draw.rect(ecran, (255, 0, 0), (80, 80, 80, 80))
        print("yoo")
        
    def affichage(self):
        for i in range(8):
            print(i, end=" : ")
            for j in range(8):
                if self.grille[i][j] == None:
                    print(" |", end="")
                else:
                    print(self.grille[i][j].getNom()+"|", end="")
            print("")
        print("")

    def coups_possibles_pion(self,case,tab_coups):
        # pions blancs
        if self.grille[case[0]][case[1]].getCouleur() == "blanc":
            try:
                if(case[0]-1 > -1 and self.grille[case[0]-1][case[1]+1] != None and self.grille[case[0]-1][case[1]+1].getCouleur() == "noir"):
                    tab_coups.append((case[0]-1,case[1]+1))
            except IndexError:
                pass
            try:
                if(case[0]-1 > -1 and case[1]-1 > -1 and self.grille[case[0]-1][case[1]-1] != None and self.grille[case[0]-1][case[1]+1].getCouleur() == "noir"):
                    tab_coups.append((case[0]-1,case[1]-1))
            except IndexError:
                pass
            if (case[0] == 6):
                if(self.grille[case[0]-1][case[1]] == None):
                    tab_coups.append((case[0]-1,case[1]))
                if(self.grille[case[0]-1][case[1]] == None and self.grille[case[0]-2][case[1]] == None):
                    tab_coups.append((case[0]-2,case[1]))
            else:
                try:
                    if(self.grille[case[0]-1][case[1]] == None):
                        tab_coups.append((case[0]-1,case[1]))
                except IndexError:
                    pass
        # pions noirs
        if self.grille[case[0]][case[1]].getCouleur() == "noir":
            try:
                if(self.grille[case[0]+1][case[1]+1] != None and self.grille[case[0]+1][case[1]+1].getCouleur() == "blanc"):
                    tab_coups.append((case[0]+1,case[1]+1))
            except IndexError:
                pass
            try:
                if(case[1]-1 > -1 and self.grille[case[0]+1][case[1]-1] != None and self.grille[case[0]+1][case[1]+1].getCouleur() == "blanc"):
                    tab_coups.append((case[0]+1,case[1]-1))
            except IndexError:
                pass
            if (case[0] == 1):
                if(self.grille[case[0]+1][case[1]] == None):
                    tab_coups.append((case[0]+1,case[1]))
                if(self.grille[case[0]+1][case[1]] == None and self.grille[case[0]+2][case[1]] == None):
                    tab_coups.append((case[0]+2,case[1]))
            else:
                try:
                    if(self.grille[case[0]+1][case[1]] == None):
                        tab_coups.append((case[0]+1,case[1]))
                except IndexError:
                    pass

    def coups_possibles_tour(self,case,tab_coups):
        # droite
        for i in range(case[1]+1,8):
            if self.grille[case[0]][i] == None :
                tab_coups.append((case[0],i))
            elif self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]][i].getCouleur():
                tab_coups.append((case[0],i))
                break
            else:
                break
        # gauche
        for i in range(case[1]-1, -1, -1):
            if self.grille[case[0]][i] == None :
                tab_coups.append((case[0],i))
            elif self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]][i].getCouleur():
                tab_coups.append((case[0],i))
                break
            else:
                break
        # haut
        for i in range(case[0]+1,8):
            if self.grille[i][case[1]] == None :
                tab_coups.append((i, case[1]))
            elif self.grille[case[0]][case[1]].getCouleur() != self.grille[i][case[1]].getCouleur():
                tab_coups.append((i, case[1]))
                break
            else:
                break  
        # bas
        for i in range(case[0]-1,-1, -1):
            if self.grille[i][case[1]] == None :
                tab_coups.append((i, case[1]))
            elif self.grille[case[0]][case[1]].getCouleur() != self.grille[i][case[1]].getCouleur():
                tab_coups.append((i, case[1]))
                break
            else:
                break 

    def coups_possibles_fou(self,case,tab_coups):
        # diag haut droite
        for i in range(1,8):
            if(case[0]+i == 8 or case[1]-i == -1): 
                break
            if self.grille[case[0]+i][case[1]-i] == None :
                tab_coups.append((case[0]+i,case[1]-i))
            elif self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]+i][case[1]-i].getCouleur():
                tab_coups.append((case[0]+i,case[1]-i))
                break
            else:
                break
        # diag haut gauche
        for i in range(1,8):
            if(case[0]-i == -1 or case[1]-i == -1): 
                break
            if self.grille[case[0]-i][case[1]-i] == None :
                tab_coups.append((case[0]-i,case[1]-i))
            elif self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]-i][case[1]-i].getCouleur():
                tab_coups.append((case[0]-i,case[1]-i))
                break
            else:
                break
        # diag bas droite
        for i in range(1,8):
            if(case[0]+i == 8 or case[1]+i == 8): 
                break
            if self.grille[case[0]+i][case[1]+i] == None :
                tab_coups.append((case[0]+i,case[1]+i))
            elif self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]+i][case[1]+i].getCouleur():
                tab_coups.append((case[0]+i,case[1]+i))
                break
            else:
                break
        # diag bas gauche
        for i in range(1,8):
            if(case[0]-i == -1 or case[1]+i == 8): 
                break
            if self.grille[case[0]-i][case[1]+i] == None :
                tab_coups.append((case[0]-i,case[1]+i))
            elif self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]-i][case[1]+i].getCouleur():
                tab_coups.append((case[0]-i,case[1]+i))
                break
            else:
                break

    def coups_possibles_cavalier(self,case,tab_coups):
    # partie gauche 
        if self.grille[case[0]-2][case[1]-1] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]-2][case[1]-1].getCouleur():
            if case[0]-2 > -1 and case[1]-1 > -1 :
                tab_coups.append((case[0]-2,case[1]-1))
        if self.grille[case[0]-1][case[1]-2] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]-1][case[1]-2].getCouleur():
            if case[0]-2 > -1 and case[1]-2 > -1 :
                tab_coups.append((case[0]-1,case[1]-2))
        try: 
            if self.grille[case[0]+1][case[1]-2] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]+1][case[1]-2].getCouleur():
                if case[1]-2 > -1 :
                    tab_coups.append((case[0]+1,case[1]-2))
        except IndexError:
            pass
        try:
            if self.grille[case[0]+2][case[1]-1] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]+2][case[1]-1].getCouleur():
                if case[1]-1 > -1 :
                    tab_coups.append((case[0]+2,case[1]-1))
        except IndexError:
            pass
        # partie droite
        try:
            if self.grille[case[0]-2][case[1]+1] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]-2][case[1]+1].getCouleur():
                if case[0]-2 > -1 :
                    tab_coups.append((case[0]-2,case[1]+1))
        except IndexError:
            pass
        try:
            if self.grille[case[0]-1][case[1]+2] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]-1][case[1]+2].getCouleur():
                if case[0]-1 > -1 :
                    tab_coups.append((case[0]-1,case[1]+2))
        except IndexError:
            pass
        try:
            if self.grille[case[0]+1][case[1]+2] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]+1][case[1]+2].getCouleur():
                tab_coups.append((case[0]+1,case[1]+2))
        except IndexError:
            pass
        try:
            if self.grille[case[0]+2][case[1]+1] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]+2][case[1]+1].getCouleur():
                tab_coups.append((case[0]+2,case[1]+1))
        except IndexError:
            pass
    
    def coups_possibles_roi(self,case,tab_coups):
        # haut
        if self.grille[case[0]-1][case[1]-1] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]-1][case[1]-1].getCouleur():
            if case[0]-1 > -1 and case[1]-1 > -1 :
                tab_coups.append((case[0]-1,case[1]-1))
        if self.grille[case[0]-1][case[1]] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]-1][case[1]].getCouleur():
            if case[0]-1 > -1 :
                tab_coups.append((case[0]-1,case[1]))
        try:
            if self.grille[case[0]-1][case[1]+1] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]-1][case[1]+1].getCouleur():
                if case[0]-1 > -1 :
                    tab_coups.append((case[0]-1,case[1]+1))
        except IndexError:
            pass
        # gauche + droite
        if self.grille[case[0]][case[1]-1] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]][case[1]-1].getCouleur():
            if case[1]-1 > -1 :
                tab_coups.append((case[0],case[1]-1))
        try:
            if self.grille[case[0]][case[1]+1] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]][case[1]+1].getCouleur():
                    tab_coups.append((case[0],case[1]+1))
        except IndexError:
            pass
        # bas
        try:
            if self.grille[case[0]+1][case[1]-1] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]+1][case[1]-1].getCouleur():
                if case[1]-1 > -1 :
                    tab_coups.append((case[0]+1,case[1]-1))
        except IndexError:
            pass
        try:
            if self.grille[case[0]+1][case[1]] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]+1][case[1]].getCouleur():
                tab_coups.append((case[0]+1,case[1]))
        except IndexError:
            pass
        try:
            if self.grille[case[0]+1][case[1]+1] == None or self.grille[case[0]][case[1]].getCouleur() != self.grille[case[0]+1][case[1]+1].getCouleur():
                tab_coups.append((case[0]+1,case[1]+1))
        except IndexError:
            pass

    def coups_possibles(self,case):

        # case vide
        if self.grille[case[0]][case[1]] == None : return []

        tab_coups = []
        
        # pion
        if self.grille[case[0]][case[1]].getNom() == "pion":
            self.coups_possibles_pion(case,tab_coups)

        # Tour
        if self.grille[case[0]][case[1]].getNom() == "tour" :
            self.coups_possibles_tour(case,tab_coups)

        # Fou
        if self.grille[case[0]][case[1]].getNom() == "fou" :
            self.coups_possibles_fou(case,tab_coups)

        # Reine
        if self.grille[case[0]][case[1]].getNom() == "reine" :
            self.coups_possibles_tour(case,tab_coups)
            self.coups_possibles_fou(case,tab_coups)

        # cavalier
        if self.grille[case[0]][case[1]].getNom() == "cavalier":
            self.coups_possibles_cavalier(case,tab_coups)
        
        # Roi
        if self.grille[case[0]][case[1]].getNom() == "roi": 
            self.coups_possibles_roi(case,tab_coups)
                
        return tab_coups  



    def coup(self,case1,case2):
        self.grille[case2[0]][case2[1]] = self.grille[case1[0]][case1[1]]
        self.grille[case1[0]][case1[1]] = None
    
    def affiche_couleur(self,case):
        if self.grille[case[0]][case[1]] == None:
            return "case vide"
        else:
            return self.grille[case[0]][case[1]].getCouleur()
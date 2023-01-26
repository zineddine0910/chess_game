import Piece
import pygame
import random

class Plateau:

    grille = [[None for i in range(8)] for j in range(8)]
    historique = []
    echec_et_mat_blanc = False
    echec_et_mat_noir = False
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

        #self.grille[5][4] = Piece.Piece("pion", "noir")
        # self.grille[1][1] = None
        # self.grille[6][4] = None
        # self.grille[0][1] = Piece.Piece("reine", "blanc")

    def getGrille(self):
        return self.grille


    def affichePlateau(self,ecran, choix):
        for i in range(8):
            for j in range(8):
                if ((i%2 == 0) and (j%2 == 0)) or ((i%2 == 1) and (j%2 == 1)):
                    pygame.draw.rect(ecran, (255, 255, 255), (i*80, j*80, 80, 80))
                if((j, i) in choix):
                    pygame.draw.circle(ecran, (0, 255, 0), (i*80+40, j*80+40), 15)
                
                    

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
        x, y = case[0], case[1]
        if self.grille[x][y].getCouleur() == "blanc":
            if x > 0:
                if (self.grille[x-1][y] == None):
                    tab_coups.append((x-1, y))
            if x == 6:
                if (self.grille[x-1][y] == None and self.grille[x-2][y] == None):
                    tab_coups.append((x-2, y))
            if (x > 0 and y > 0):
                if (self.grille[x-1][y-1] != None):
                    if (self.grille[x-1][y-1].getCouleur() == "noir"):
                        tab_coups.append((x-1, y-1))
            
            if (x > 0 and y < 7):
                if (self.grille[x-1][y+1] != None):
                    if (self.grille[x-1][y+1].getCouleur() == "noir"):
                        tab_coups.append((x-1, y+1))
                        
        else:
            if x < 7:
                if (self.grille[x+1][y] == None):
                    tab_coups.append((x+1, y))
            if x == 1:
                if (self.grille[x+1][y] == None and self.grille[x+2][y] == None):
                    tab_coups.append((x+2, y))
            if (x < 7 and y > 0):
                if (self.grille[x+1][y-1] != None):
                    if (self.grille[x+1][y-1].getCouleur() == "blanc"):
                        tab_coups.append((x+1, y-1))
                
            if (x < 7 and y < 7):
                if (self.grille[x+1][y+1] != None):
                    if (self.grille[x+1][y+1].getCouleur() == "blanc"):
                        tab_coups.append((x+1, y+1))

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
        x, y = case[0], case[1]
        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                if abs(i) != abs(j):
                    if 0 <= x + i < 8 and 0 <= y + j < 8:
                        if self.grille[x+i][y+j] == None:
                            tab_coups.append((x + i, y + j))
                        else:
                            if self.grille[x][y].getCouleur() != self.grille[x+i][y+j].getCouleur():
                                tab_coups.append((x + i, y + j))
        return tab_coups
    
    def coups_possibles_roi(self,case,tab_coups):
        x, y = case[0], case[1]
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (i != 0 or j != 0):
                    if 0 <= x + i < 8 and 0 <= y + j < 8:
                        if self.grille[x+i][y+j] == None:
                            tab_coups.append((x + i, y + j))
                        else:
                            if self.grille[x][y].getCouleur() != self.grille[x+i][y+j].getCouleur():
                                tab_coups.append((x + i, y + j))

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
        
        piece_case2 = self.grille[case2[0]][case2[1]]
        self.historique.append((case1, case2, piece_case2))
        self.grille[case2[0]][case2[1]] = self.grille[case1[0]][case1[1]]
        self.grille[case1[0]][case1[1]] = None
    
    def annuler_coup(self):
        if self.historique:
            ancienne_case, nouvelle_case, piece = self.historique.pop()
            self.grille[ancienne_case[0]][ancienne_case[1]] = self.grille[nouvelle_case[0]][nouvelle_case[1]]
            self.grille[nouvelle_case[0]][nouvelle_case[1]] = piece
    def affiche_couleur(self,case):
        if self.grille[case[0]][case[1]] == None:
            return "case vide"
        else:
            return self.grille[case[0]][case[1]].getCouleur()
    
    # def aucun_coup_dispo_IA(self, list):
        
    #     for i in range(len(list)):
    #         if self.coups_possibles(list[i]) != []:
    #             return False
    #     return True
    # def coup_IA(self):
    #     list = []
    #     list2 = []
    #     for i in range(8):
    #             for j in range(8):
    #                 if self.grille[i][j] != None:
    #                     if self.grille[i][j].getCouleur() == "noir":
    #                         list.append((i, j))
        
    #     while(not list2):
    #         case = random.choice(list)
    #         list2 = self.coups_possibles(case)
    #         if(self.grille[case[0]][case[1]].getNom() == "roi"):
    #             self.enleve_cases_roi(list2, "noir")
    #         if(self.aucun_coup_dispo_IA(list) == True):
    #             self.echec_et_mat_noir = True
    #             return
    #     case2 = random.choice(list2)
    #     self.coup(case, case2)
        
    def coup_IA(self):
        list = []
        list2 = []
        for i in range(8):
                for j in range(8):
                    if self.grille[i][j] != None:
                        if self.grille[i][j].getCouleur() == "noir":
                            list.append((i, j))
        
        while(not list2):
            for i in range(8):
                for j in range(8):
                    if self.grille[i][j] != None:
                        if self.grille[i][j].getCouleur() == "noir":
                            list.append((i, j))
            case = random.choice(list)
            list2 = self.coups_possibles(case)
        case2 = random.choice(list2)
        self.coup(case, case2)
    
    def roi_en_echec(self, couleur): #verifie si un des rois est en echec
        x,y = -1,-1
        for i in range(8):
            for j in range(8):
                if (self.grille[i][j] != None and self.grille[i][j].getNom() == "roi" and self.grille[i][j].getCouleur() == couleur):
                    x, y = i, j
        for i in range(8):
            for j in range(8):
                if (self.grille[i][j] != None and self.grille[i][j].getCouleur() != couleur):
                    if((x,y) in self.coups_possibles((i,j))):
                        return True
        return False
    
    def enleve_cases_roi(self, tab_coups, couleur): #nleve les cases qui representeraient un echec et mat pour le roi
        cpt = 0
        arret = False
        while not arret:
            if self.case_vide_en_echec(tab_coups[cpt], couleur):
                tab_coups.remove(tab_coups[cpt])
            else: cpt = cpt+1
            if cpt == len(tab_coups):
                arret = True
                    
    def case_vide_en_echec(self, case, couleur): #verifie si une case vide sera en echecs si elle reçoit une piece de couleur couleur
        x,y = case[0], case[1]
        for i in range(8):
            for j in range(8):
                if (self.grille[i][j] != None and self.grille[i][j].getNom() != "pion" and self.grille[i][j].getCouleur() != couleur):
                    if((x,y) in self.coups_possibles((i,j))):
                        return True
        if(couleur == "blanc"):
            if(self.grille[x-1][y-1] != None and self.grille[x-1][y-1].getNom() == "pion" and self.grille[x-1][y-1].getCouleur() == "noir"):
                return True
            if(self.grille[x-1][y+1] != None and self.grille[x-1][y+1].getNom() == "pion" and self.grille[x-1][y+1].getCouleur() == "noir"):
                return True
        else:
            if(self.grille[x+1][y-1] != None and self.grille[x+1][y-1].getNom() == "pion" and self.grille[x+1][y-1].getCouleur() == "blanc"):
                return True
            if(self.grille[x+1][y+1] != None and self.grille[x+1][y+1].getNom() == "pion" and self.grille[x+1][y+1].getCouleur() == "blanc"):
                return True
        return False
                    
    def verif_echec_et_mat_blanc(self): #verifie si les blanc ont perdu
        for i in range(8):
            for j in range(8):
                if (self.grille[i][j] != None and self.grille[i][j].getNom() == "roi" and self.grille[i][j].getCouleur() == "blanc"):
                    return
        self.echec_et_mat_blanc = True
    
    def verif_echec_et_mat_noir(self): #verifie si les noirs ont perdu
        for i in range(8):
            for j in range(8):
                 if (self.grille[i][j] != None and self.grille[i][j].getNom() == "roi" and self.grille[i][j].getCouleur() == "noir"):
                    return
        self.echec_et_mat_noir = True
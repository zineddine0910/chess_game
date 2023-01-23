class Piece:

    nom = ""
    couleur = ""

    def __init__(self,nom,couleur):
        self.nom = nom
        self.couleur = couleur

    def getNom(self):
        return self.nom

    def getCouleur(self):        
        return self.couleur
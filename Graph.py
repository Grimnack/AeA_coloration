import random as r
from Sommet import Sommet
from Arete import Arete
from collections import deque

class GraphValue(object):
    """docstring for GraphValue"""
    def __init__(self, matrix):
        super(GraphValue, self).__init__()
        self.lesAretes = []            
        lesSommets = []
        for i in range(len(matrix)) :
            sommet = Sommet([],i)
            lesSommets.append(sommet)
        for i in range(len(matrix)) :
            for j in range(i) :
                if matrix[i][j] != -1 :
                    lesSommets[i].ajouteVoisin(lesSommets[j],matrix[i][j],self)
        self.lesSommets = lesSommets


    def __str__(self) :
        chaine = ""
        for sommet in self.lesSommets :
            chaine +=  "sommet num = " + str(sommet) + ", couleur = " + str(sommet.couleur) + "\n"
        for arete in self.lesAretes :
            chaine += str(arete.sommet1) + " --- "+ str(arete.sommet2) + "\n" 
        return chaine



    def algoWelshPowel(self) :
        lesSommets = self.lesSommets[:]
        lesSommets.sort()
        for sommet in lesSommets :
            lesVoisinsColores = sommet.getVoisinsColores()
            couleurTrouve = False
            i = 0
            while not couleurTrouve :
                contientI = sommetsContientCouleur(lesVoisinsColores,i)
                if not contientI :
                    couleurTrouve = True
                    sommet.couleur = i
                    sommet.tag = True
                else :
                    i += 1

    def algoDSATUR(self):
        lesSommets = self.lesSommets[:]
        lesSommets.sort(key=lambda sommet: sommet.getDSAT(), reverse=True)
        lesSommets[0].colorierDSAT(lesSommets, 0)
        while lesSommets :
            couleur = lesSommets[0].getSmallestColor()
            lesSommets[0].colorierDSAT(lesSommets, couleur)

    def algoNaif(self) :
        lesSommets=self.lesSommets[:]
        r.shuffle(lesSommets)
        for sommet in lesSommets :
            couleur = sommet.getSmallestColor()
            sommet.couleur = couleur
            sommet.tag = True

    def totalColor(self) :
        nbcol = 0
        for sommet in self.lesSommets :
            if nbcol<sommet.couleur :
                nbcol = sommet.couleur
        return nbcol




def sommetsContientCouleur(listeSommets,icouleur) :
    for sommet in listeSommets :
        if sommet.couleur == icouleur :
            return True
    return False

def comp (sommet1,sommet2) :
    deg1 = len(sommet1.aretes)
    deg2 = len(sommet2.aretes)
    if deg1 < deg2 :
        return -1
    elif deg1 > deg2 :
        return 1
    else :
        return 0

def graphAlea(nbSommets, poidsMax, p) :
    matrix = []
    for i in range(nbSommets) :
        matrix.append([-1] * nbSommets)
    for i in range(nbSommets) :
        for j in range(i) :
            if p >= r.random() :
                poidsAlea = r.randint(1,poidsMax)
                matrix[i][j] = poidsAlea
                matrix[j][i] = poidsAlea
    return GraphValue(matrix)
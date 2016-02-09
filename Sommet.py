from Arete import Arete
import Graph as g

class Sommet(object):
    """docstring for Sommet"""
    def __init__(self, listeArete, num):
        super(Sommet, self).__init__()
        self.aretes = listeArete[:]
        self.couleur = -1 # -1 veut dire qu'il n'a pas encore de coloriage
        self.num = num
        self.tag = False

    def __str__(self) :
        return str(self.num)

    def __eq__(self,other) :
        return self.num == other.num

    def __lt__(self,other) :
        return len(self.aretes) < len(other.aretes)

    def __gt__(self,other) :
        return len(self.aretes) > len(other.aretes)
    

    def __cmp__(self,sommet2) :
        deg1 = len(self.aretes)
        deg2 = len(sommet2.aretes)
        if deg1 < deg2 :
            return -1
        elif deg1 > deg2 :
            return 1
        else :
            return 0

    def getDSAT(self) :
        lesColores = self.getVoisinsColores()
        if lesColores == [] :
            return len(self.aretes)
        else :
            return len(lesColores)

    def colorierDSAT(self, lesSommets, couleur) :
        self.couleur = couleur
        self.tag = True
        lesSommets.remove(self)
        lesSommets.sort(key=lambda sommet: sommet.getDSAT(), reverse=True)

    def getSmallestColor(self) :
        voisinsColores = self.getVoisinsColores()
        i = 0
        while True :
            contientI = g.sommetsContientCouleur(voisinsColores,i)
            if not contientI :
                return i
            else :
                i += 1
        
    def getVoisins(self) :
        voisins = []
        for arete in self.arete :
            voisins.append(arete.renvoieVoisin(self))
        return voisins

    def getVoisinsColores(self) :
        '''
        fonction utile pour l algo de prim
        renvoie une liste de couples (sommet,arete)

        '''
        voisins = []
        for arete in self.aretes :
            voisin = arete.renvoieVoisin(self)
            if voisin.tag :
                voisins.append(voisin)
        return voisins

    def ajouteVoisin(self,sommet2,poids,graph) :
        lien = Arete(self,sommet2,poids)
        graph.lesAretes.append(lien)
        self.aretes.append(lien)
        sommet2.aretes.append(lien)

    def renvoiePoidsMin(self) :
        '''
        a tester
        '''
        return min(self.aretes, key=lambda arete: arete.poids)    


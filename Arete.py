class Arete(object):
    """docstring for Arete"""
    def __init__(self, sommet1, sommet2, poids):
        super(Arete, self).__init__()
        self.sommet1 = sommet1
        self.sommet2 = sommet2
        self.poids = poids

    def __str__(self) :
        return str(self.sommet1) + " - " + str(self.sommet2) + " (" + str(self.poids) + ')'

    def renvoieVoisin(self,sommet) :
        if self.sommet1.num == sommet.num :
            return self.sommet2
        else :
            return self.sommet1
        
from Compte import *
class CompteCourant(Compte):
    def __nint__(self,num,propri,solde,date,motant):
        super().__init__(num,propri,solde,date)
        self.__motantDecouvertAutorise = motant
    
    @property
    def motentDecou(self):
        return self.__motantDecouvertAutorise
    @motentDecou.setter
    def setmoteDecou(self,motent):
        self.__motantDecouvertAutorise = motent 
    
    def __str__(self):
        super().__str__()
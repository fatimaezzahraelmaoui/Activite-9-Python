from Compte import *
class CompteEparge(Compte):
    def __nint__(self,num,propri,solde,date,inte):
        super().__init__(num,propri,solde,date)
        self.__interet = inte 
        
    @property
    def interet(self):
        return self.__interet
    @interet.setter
    def setinteret(self,inte):
        self.__interet = inte
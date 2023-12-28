class Compte:
    def __nint__(self,num,propri,solde,date):
        self.__numero= num 
        self.__proprietaire = propri 
        self.__solde =solde
        self.__dateOverture = date
        
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def setnumero(self,num):
        self.__numero = num 
    
    @property
    def proprietaire(self):
        return self.__proprietaire
    @proprietaire.setter
    def setpreprietaire(self,prpori):
        self.__proprietaire = prpori 
    
    @property
    def solde(self):
        return self.__solde
    @solde.setter
    def setsolde(self,solde):
        self.__solde = solde
    
    @property
    def dateOverture(self):
        return self.__dateOverture
    @dateOverture.setter
    def setdateOverture(self,date):
        self.__dateOverture = date
    
    def __str__(self):
        return (f"-{self.__numero}-{self.__proprietaire}-{self.__solde}-{self.__dateOverture}")
    
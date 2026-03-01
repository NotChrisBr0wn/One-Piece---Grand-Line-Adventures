# Vamos ver se sai daqui o melhor jogo de one piece (via texto :P)

class Tripulante:
    def __init__ (self, nome:str,classe:str,fruta:str,poder:int,energia:int = 100,recompensa:float = 0):
        self.nome = nome
        self.classe = classe
        self.fruta = fruta
        self.poder = poder
        self.energia = energia
        self.recompensa = recompensa

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, valor: str):
        self.nome = valor

    @property
    def classe(self):
        return self.classe
    
    @classe.setter
    def classe(self, valor: str):
        self.classe = valor

    @property
    def fruta(self):
        return self.fruta
    
    @fruta.setter
    def fruta(self, valor: str):
        self.fruta = valor

    @property
    def poder(self):
        return self.poder
    
    @poder.setter
    def poder(self, valor: int):
        if 0 <= poder <= 100:
            self.poder = valor
        else:
            raise ValueError(f"O poder de {self.nome} deve ser um valor entre 0 e 100.")
        
    @property
    def energia(self):
        return self.energia
    
    @energia.setter
    def energia(self, valor: int):
        if 0 <= energia <= 100:
            self.energia = valor
        else:
            raise ValueError(f"A energia de {self.nome} deve ser um valor entre 0 e 100.") 
    
    @property
    def recompensa(self):
        return self.recompensa
    
    @recompensa.setter
    def recompensa(self, valor: float):
        if valor >= 0:
            self.recompensa = valor
        else:
            raise ValueError(f"A recompensa de {self.nome} não pode ser menor que 0.")
        
  

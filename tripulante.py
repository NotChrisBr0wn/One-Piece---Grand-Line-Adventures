# Vamos ver se sai daqui o melhor jogo de one piece (via texto :P)

class Tripulante:
    def __init__ (self, nome:str,classe:str,fruta:str,recompensa:float,poder:int,energia:int = 100):
        self.nome = nome
        self.classe = classe
        self.fruta = fruta
        self.poder = poder
        self.energia = energia
        self.recompensa = recompensa

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor: str):
        self._nome = valor

    @property
    def classe(self):
        return self._classe
    
    @classe.setter
    def classe(self, valor: str):
        self._classe = valor

    @property
    def fruta(self):
        return self._fruta
    
    @fruta.setter
    def fruta(self, valor: str):
        self._fruta = valor

    @property
    def poder(self):
        return self._poder
    
    @poder.setter
    def poder(self, valor: int):
        if 0 <= valor <= 100:
            self._poder = valor
        else:
            raise ValueError(f"O poder de {self.nome} deve ser um valor entre 0 e 100.")
        
    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, valor: int):
        if 0 <= valor <= 100:
            self._energia = valor
        else:
            raise ValueError(f"A energia de {self.nome} deve ser um valor entre 0 e 100.") 
    
    @property
    def recompensa(self):
        return self._recompensa
    
    @recompensa.setter
    def recompensa(self, valor: float):
        if valor >= 0:
            self._recompensa = valor
        else:
            raise ValueError(f"A recompensa de {self.nome} não pode ser menor que 0.")
        
    # Métodos

    def trabalhar(self, tempo: int):
        # Reduz a energia de acordo com o tempo
        energia_gasta = tempo * 5
        nova_energia = max(0, self.energia - energia_gasta)
        self.energia = nova_energia
        print(f"{self.nome} trabalhou por {tempo} horas e gastou {energia_gasta} de energia.")

    def descansar(self):
        self.energia = 100
        print(f"{self.nome} descansou e recuperou toda a energia.")

    def __str__(self):
        return f"Nome: {self.nome} Classe: [{self.classe}] Fruta: {self.fruta} - Recompensa: {self.recompensa} Poder: {self.poder} Energia: {self.energia}"


if __name__ == "__main__":
    zoro = Tripulante("Zoro", "Espadachim", "N/A", 32000000, 95, 100)
    print(zoro) # Testa o __str__
    
    zoro.trabalhar(5) # Perde 25 de energia
    print(f"Energia após trabalho: {zoro.energia}")
    
    zoro.trabalhar(20) # Tentaria perder 100, mas o max(0) prende no zero!
    print(f"Energia após muito trabalho: {zoro.energia}")
    
    zoro.descansar()
    print(f"Energia após descanso: {zoro.energia}")
from tripulante import Tripulante

class Navegador(Tripulante):
    def __init__(self, nome: str, fruta: str, recompensa: float, poder: int, energia: int = 100, status: str = "Ok", milhas_navegadas: int = 0):
        super().__init__(nome, fruta, recompensa, poder, energia, status)
        self.milhas_navegadas = milhas_navegadas

    @property
    def milhas_navegadas(self):
        return self._milhas_navegadas
    
    @milhas_navegadas.setter
    def milhas_navegadas(self, valor: int):
        if valor >= 0:
            self._milhas_navegadas = valor
        else:
            raise ValueError("As milhas navegadas não podem ser negativas.")

    def __str__(self):
        return f"{super().__str__()} | Milhas: {self.milhas_navegadas}"
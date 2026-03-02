from tripulante import Tripulante

class Musico(Tripulante):
    def __init__(self, nome: str, fruta: str, recompensa: float, poder: int, energia: int = 100, status: str = "Ok", instrumento: str = "Violino"):
        super().__init__(nome, fruta, recompensa, poder, energia, status)
        self.instrumento = instrumento

    @property
    def instrumento(self):
        return self._instrumento
    
    @instrumento.setter
    def instrumento(self, valor: str):
        self._instrumento = valor

    def __str__(self):
        return f"{super().__str__()} | Instrumento: {self.instrumento}"
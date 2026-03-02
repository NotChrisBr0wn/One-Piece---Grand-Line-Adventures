from tripulante import Tripulante

class Carpinteiro(Tripulante):
    def __init__(self, nome: str, fruta: str, recompensa: float, poder: int, energia: int = 100, status: str = "Ok", litros_cola: int = 0):
        super().__init__(nome, fruta, recompensa, poder, energia, status)
        self.litros_cola = litros_cola

    @property
    def litros_cola(self):
        return self._litros_cola
    
    @litros_cola.setter
    def litros_cola(self, valor: int):
        if valor >= 0:
            self._litros_cola = valor
        else:
            raise ValueError("Os litros de cola não podem ser negativos. SUUUUPEEEEERRRR erro!")

    def __str__(self):
        return f"{super().__str__()} | Reserva de Cola: {self.litros_cola}L"
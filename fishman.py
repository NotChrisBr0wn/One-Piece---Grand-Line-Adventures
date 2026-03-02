from tripulante import Tripulante

class Timoneiro(Tripulante):
    def __init__(self, nome: str, fruta: str, recompensa: float, poder: int, energia: int = 100, status: str = "Ok", tsunamis_surfados: int = 0):
        super().__init__(nome, fruta, recompensa, poder, energia, status)
        self.tsunamis_surfados = tsunamis_surfados

    @property
    def tsunamis_surfados(self):
        return self._tsunamis_surfados
    
    @tsunamis_surfados.setter
    def tsunamis_surfados(self, valor: int):
        if valor >= 0:
            self._tsunamis_surfados = valor
        else:
            raise ValueError("O número de tsunamis não pode ser negativo.")

    def __str__(self):
        return f"{super().__str__()} | Tsunamis Surfados: {self.tsunamis_surfados}"
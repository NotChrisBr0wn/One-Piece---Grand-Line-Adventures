from tripulante import Tripulante

class Atirador(Tripulante):
    def __init__(self, nome: str, fruta: str, recompensa: float, poder: int, energia: int = 100, status: str = "Ok", precisao: int = 0):
        super().__init__(nome, fruta, recompensa, poder, energia, status)
        self.precisao = precisao

    @property
    def precisao(self):
        return self._precisao
    
    @precisao.setter
    def precisao(self, valor: int):
        if 0 <= valor <= 100:
            self._precisao = valor
        else:
            raise ValueError("A precisão tem de estar entre 0 e 100.")

    def __str__(self):
        return f"{super().__str__()} | Precisão: {self.precisao}%"
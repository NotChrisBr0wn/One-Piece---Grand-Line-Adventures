from tripulante import Tripulante

class Arqueologo(Tripulante):
    def __init__(self, nome: str, fruta: str, recompensa: float, poder: int, energia: int = 100, status: str = "Ok", poneglyphs_lidos: int = 0):
        super().__init__(nome, fruta, recompensa, poder, energia, status)
        self.poneglyphs_lidos = poneglyphs_lidos

    @property
    def poneglyphs_lidos(self):
        return self._poneglyphs_lidos
    
    @poneglyphs_lidos.setter
    def poneglyphs_lidos(self, valor: int):
        if valor >= 0:
            self._poneglyphs_lidos = valor
        else:
            raise ValueError("O número de Poneglyphs lidos não pode ser negativo.")

    def __str__(self):
        return f"{super().__str__()} | Poneglyphs Lidos: {self.poneglyphs_lidos}"
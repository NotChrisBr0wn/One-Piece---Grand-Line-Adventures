from tripulante import Tripulante

class Capitao(Tripulante):
    def __init__(self, nome: str, recompensa:float = 0.0, poder:int = 0, fruta: str = "Nenhuma",  energia: int = 100, status: str = "Ok", haki_lvl: int = 0):
        super().__init__(nome, recompensa, poder, fruta, energia, status)
        self.haki_lvl = haki_lvl

    @property
    def haki_lvl(self):
        return self._haki_lvl
    
    @haki_lvl.setter
    def haki_lvl(self, valor: int):
        if 0 <= valor <= 100:
            self._haki_lvl = valor
        else:
            raise ValueError("O nível de Haki deve estar entre 0 e 100.")

    def __str__(self):
        return f"{super().__str__()} | Nível de Haki: {self.haki_lvl}"
    
    def executar_acao(self, navio):
        if self.haki_lvl > 50:
            print(f"👑 {self.nome} usou Haki do Rei Supremo! Metade dos inimigos desmaiaram.")
        else:
            print(f"🍖 {self.nome} está a roubar a comida do armazém...")
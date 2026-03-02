from tripulante import Tripulante

class Cozinheiro(Tripulante):
    def __init__(self, nome: str, fruta: str, recompensa: float, poder: int, energia: int = 100, status: str = "Ok", refeicoes_preparadas: int = 0):
        super().__init__(nome, fruta, recompensa, poder, energia, status)
        self.refeicoes_preparadas = refeicoes_preparadas

    @property
    def refeicoes_preparadas(self):
        return self._refeicoes_preparadas
    
    @refeicoes_preparadas.setter
    def refeicoes_preparadas(self, valor: int):
        if valor >= 0:
            self._refeicoes_preparadas = valor
        else:
            raise ValueError("As refeições preparadas não podem ser negativas.")

    def __str__(self):
        return f"{super().__str__()} | Refeições Preparadas: {self.refeicoes_preparadas}"
    
    def executar_acao(self, navio):
        self.refeicoes_preparadas += 1
        if self.refeicoes_preparadas == 1:
            print(f"🍳 {self.nome} preparou a primeira refeição! Que delícia!")
        else:
            print(f"🍳 {self.nome} preparou um banquete! Já cozinhou {self.refeicoes_preparadas} refeições divinais")
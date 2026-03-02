from tripulante import Tripulante

class Cozinheiro(Tripulante):
    def __init__(self, nome: str, recompensa: float, poder: int, fruta: str = "Nenhuma",  energia: int = 100, status: str = "Ok", refeicoes_preparadas: int = 0):
        super().__init__(nome, recompensa, poder, fruta, energia, status)
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
        if not navio._tripulacao:
            print(f"🍳 {self.nome} fez um banquete épico, mas não há ninguém para comer!")
            return
            
        for pirata in navio._tripulacao:
            nova_energia = pirata.energia + 20
            pirata.energia = min(100, nova_energia)
            
        self.refeicoes_preparadas += 1
        print(f"🍖 {self.nome} preparou o seu famoso curry especial!")
        print(f"✨ Toda a tripulação do {navio.nome} recuperou 20% de energia. (Refeições divinas servidas: {self.refeicoes_preparadas})")
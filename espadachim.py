from tripulante import Tripulante

class Espadachim(Tripulante):
    def __init__(self, nome: str, fruta: str, recompensa: float, poder: int, energia: int = 100, status: str = "Ok", espadas: list = None):
        super().__init__(nome, fruta, recompensa, poder, energia, status)
        self.espadas = espadas if espadas is not None else []

    @property
    def espadas(self):
        return self._espadas
    
    @espadas.setter
    def espadas(self, valor: list):
        if isinstance(valor, list):
            self._espadas = valor
        else:
            raise ValueError("O atributo espadas tem de ser uma lista (list).")

    def __str__(self):
        base = super().__str__()
        nomes_espadas = ", ".join(self.espadas) if self.espadas else "Nenhuma"
        return f"{base} | Espadas: {nomes_espadas}"
    
    def executar_acao(self, navio):
        print(f"⚔️ {self.nome} está a treinar intensamente com as suas espadas.")
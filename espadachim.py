from tripulante import Tripulante

class Espadachim(Tripulante):
    def __init__(self, nome: str, recompensa:float = 0.0, poder:int = 0, fruta: str = "Nenhuma",  energia: int = 100, status: str = "Ok", espadas: list = None):
        super().__init__(nome, recompensa, poder, fruta, energia, status)
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
        bonus = 10 * len(self.espadas)
        
        novo_poder = self.poder + bonus
        self.poder = min(100, novo_poder) 
        
        print(f"⚔️ {self.nome} executa um ataque devastador com as suas {len(self.espadas)} espadas!")
        print(f"💪 O poder de combate de {self.nome} subiu para {self.poder}.")
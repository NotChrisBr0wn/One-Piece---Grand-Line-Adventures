from tripulante import Tripulante

class Navio:
    def __init__(self, nome: str):
        self._nome = nome
        self._tripulacao: list[Tripulante] = []
   
    # Getters e propriedades    
    @property
    def nome(self):
        return self._nome
    
    @property
    def recompensa_total(self):
        total = 0
        for pirata in self._tripulacao:
            total += pirata.recompensa
        return total
    
    # Métodos de gestão de tripulação
    def recrutar(self, novo_tripulante: Tripulante):
        # Adiciona um tripulante á lista de tripulação
        self._tripulacao.append(novo_tripulante)
        print(f"☠️ {novo_tripulante.nome} juntou-se á tripulação de {self.nome}.")
    
    def expulsar(self, nome_tripulante: str):
        # Remove um tripulante da tripulação pelo nome
        for pirata in self._tripulacao:
            if pirata.nome.lower() == nome_tripulante.lower() or pirata.nome == nome_tripulante: # verifica o nome em maiusculas e minusculas
                self._tripulacao.remove(pirata) # remove o pirata da crew
                print(f"🦈 {pirata.nome} foi dado aos tubarões do {self.nome}.")
                return True # indica remoção sucedida
        
        # se não houver ninguém com o nome
        print(f"❓ Não há nenhum tripulante chamado {nome_tripulante} neste navio.")
        return False # indica remoção falhada
    
    def calcular_poder_total(self): # calcula o poder total
        poder_total = 0
        for pirata in self._tripulacao:
            poder_total += pirata.poder
        return poder_total
    
    def mostrar_manifesto(self):
        print(f"\n{'=' * 65}")
        print(f"📜 Manifesto do Navio {self.nome.upper()}:")
        print(f"💰 Recompensa Total: {self.recompensa_total()}B")
        print(f"⚔️ Poder Total: {self.calcular_poder_total()}")
        print(f"={'=' * 65}")

        if not self._tripulacao:
            print("🚫 A tripulação está vazia.")
        else:
            for pirata in self._tripulacao:
                print(f"- {pirata}")
        print(f"{'=' * 65}\n")        
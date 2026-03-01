from tripulante import Tripulante
from colorama import init, Fore, Style

init(autoreset=True)

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
        print(Fore.GREEN + f"☠️ {novo_tripulante.nome} juntou-se á tripulação de {self.nome}.")
    
    def expulsar(self, nome_tripulante: str):
        # Remove um tripulante da tripulação pelo nome
        for pirata in self._tripulacao:
            if pirata.nome.lower() == nome_tripulante.lower() or pirata.nome == nome_tripulante: # verifica o nome em maiusculas e minusculas
                self._tripulacao.remove(pirata) # remove o pirata da crew
                print(Fore.RED + f"🦈 {pirata.nome} foi dado aos tubarões do {self.nome}.")
                return True # indica remoção sucedida
        
        # se não houver ninguém com o nome
        print(Fore.YELLOW + f"❓ Não há nenhum tripulante chamado {nome_tripulante} neste navio.")
        return False # indica remoção falhada
    
    def calcular_poder_total(self): # calcula o poder total
        poder_total = 0
        for pirata in self._tripulacao:
            poder_total += pirata.poder
        return poder_total
    
    def mostrar_manifesto(self):
        print(Fore.WHITE + Style.BRIGHT + f"\n{'=' * 65}")
        print(Fore.CYAN + Style.BRIGHT + f"📜 Manifesto do Navio {self.nome.upper()}:")
        print(Fore.YELLOW + f"💰 Recompensa Total: {self.recompensa_total()}B")
        print(Fore.RED + f"⚔️ Poder Total: {self.calcular_poder_total()}")
        print(Fore.WHITE + Style.BRIGHT +f"={'=' * 65}")

        if not self._tripulacao:
            print(Fore.YELLOW + "🚫 A tripulação está vazia.")
        else:
            for pirata in self._tripulacao:
                cor = Fore.WHITE
                classe_lower = pirata.classe.lower()

                if "capitão" in classe_lower or "capitao" in classe_lower:
                    cor = Fore.RED + Style.BRIGHT
                elif "espadachim" in classe_lower:
                    cor = Fore.GREEN + Style.BRIGHT
                elif "atirador" in classe_lower:
                    cor = Fore.BLUE + Style.BRIGHT
                elif "navegador" in classe_lower:
                    cor = Fore.CYAN + Style.BRIGHT
                elif "cozinheiro" in classe_lower:
                    cor = Fore.YELLOW + Style.BRIGHT
                elif "médico" in classe_lower or "medico" in classe_lower:
                    cor = Fore.MAGENTA + Style.BRIGHT
                print(f"- {pirata}")


            blocos_cheios = int(pirata.energia / 10)
            blocos_vazios = 10 - blocos_cheios
        print(f"{'=' * 65}\n")        
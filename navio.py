import json
from tripulante import Tripulante
from colorama import init, Fore, Style 

init(autoreset=True)

class Navio:
    def __init__(self, nome: str, vida:int, ouro: int):
        self._nome = nome
        self._tripulacao: list[Tripulante] = []
        self.vida = 100
        self.ouro = 0
   
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
    
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor: int):
        # Clamping
        if valor > 100:
            self._vida = 100
        elif valor < 0:
            self._vida = 0
        else:
            self._vida = valor

    @property
    def ouro(self):
        return self._ouro

    @ouro.setter
    def ouro(self, valor: int):
        if valor >= 0:
            self._ouro = valor
        else:
            self._ouro = 0
    
    # Métodos de gestão de tripulação
    def recrutar(self, novo_tripulante: Tripulante):
        # Adiciona um tripulante á lista de tripulação
        self._tripulacao.append(novo_tripulante)
        print(Fore.GREEN + f"☠️   {novo_tripulante.nome} juntou-se á tripulação de {self.nome}.")
    
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
    
    def reparar(self, quantidade: int):
        # Recupera a vida do navio
        self.vida += quantidade 
        print(Fore.GREEN + f"🛠️ O {self.nome} foi reparado em {quantidade}! Vida atual: {self.vida}/100")

    def danificar(self, quantidade: int):
        # DISPARAR CANHOESSSSS!!!
        self.vida -= quantidade 
        print(Fore.RED + f"💥 BOOM! O navio sofreu {quantidade} de dano! Vida atual: {self.vida}/100")
        
        if self.vida == 0:
            print(Fore.RED + Style.BRIGHT + f"\n☠️ GAME OVER! O {self.nome} afundou-se nas profundezas do oceano! ☠️")
            # Aqui depois podes meter um código para terminar o jogo se quiseres!

    def ganhar_ouro(self, quantidade: int):
        # Adiciona o money do navio
        self.ouro += quantidade
        print(Fore.YELLOW + f"🪙 BINGO! Ganhaste {quantidade} B Tesouro total: {self.ouro}B")
    
    def calcular_poder_total(self): # calcula o poder total
        poder_total = 0
        for pirata in self._tripulacao:
            poder_total += pirata.poder
        return poder_total
    
    def ordenar_tripulacao(self):
        if not self._tripulacao:
            print(Fore.YELLOW + "🚫 A tripulação está vazia. Nada para ordenar.")
            return
        
        self._tripulacao.sort(reverse=True)
        print(Fore.GREEN + "🔝 A tripulação foi ordenada por poder e recompensa com sucesso!")
    
    def mostrar_manifesto(self):
        print(Fore.WHITE + Style.BRIGHT + f"\n{'=' * 65}")
        print(Fore.CYAN + Style.BRIGHT + f"📜 Manifesto do Navio {self.nome.upper()}:")
        print(Fore.YELLOW + f"💰 Recompensa Total: {self.recompensa_total:,.2f}B")
        print(Fore.RED + f"⚔️ Poder Total: {self.calcular_poder_total()}")
        print(Fore.WHITE + Style.BRIGHT +f"={'=' * 65}")

        if not self._tripulacao:
            print(Fore.YELLOW + "🚫 A tripulação está vazia.")
        else:
            for pirata in self._tripulacao:
                cor = Fore.WHITE

                if "capitão" in pirata.classe.lower() or "capitao" in pirata.classe.lower():
                    cor = Fore.RED + Style.BRIGHT
                elif "espadachim" in pirata.classe.lower():
                    cor = Fore.GREEN + Style.BRIGHT
                elif "atirador" in pirata.classe.lower():
                    cor = Fore.BLUE + Style.BRIGHT
                elif "navegador" in pirata.classe.lower():
                    cor = Fore.CYAN + Style.BRIGHT
                elif "cozinheiro" in pirata.classe.lower():
                    cor = Fore.YELLOW + Style.BRIGHT
                elif "médico" in pirata.classe.lower() or "medico" in pirata.classe.lower():
                    cor = Fore.MAGENTA + Style.BRIGHT


                blocos_cheios = int(pirata.energia / 10)
                blocos_vazios = 10 - blocos_cheios
                barra = (Fore.GREEN + "█" * blocos_cheios) + (Fore.LIGHTBLACK_EX + "░" * blocos_vazios)
                print(f"🗡️   {cor}{pirata.nome} {Fore.WHITE} | Classe: {pirata.classe} | Fruta: {pirata.fruta} | Recompensa: {pirata.recompensa:,.2f}B | Energia: [{barra}{Fore.WHITE}] {pirata.energia:3}% | Poder: {pirata.poder}")
    
    def guardar_jogo(self, ficheiro="save_navio.json"):
        # Guarda a trip num ficheiro JSON
        dados = [pirata.to_dict() for pirata in self._tripulacao]
        
        with open(ficheiro, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
            
        print(Fore.BLUE + Style.BRIGHT + f"💾 Jogo guardado com sucesso em '{ficheiro}'!")

    def carregar_jogo(self, ficheiro="save_navio.json"):
        # Carrega a trip
        try:
            with open(ficheiro, "r", encoding="utf-8") as f:
                dados = json.load(f)
                
            self._tripulacao.clear() # Da clear do navio atual
            for d in dados:
                self._tripulacao.append(Tripulante.from_dict(d))
                
            print(Fore.BLUE + Style.BRIGHT + f"📂 Jogo carregado com sucesso! Bem-vindo de volta.")
        except FileNotFoundError:
            print(Fore.RED + f"❌ Ficheiro '{ficheiro}' não encontrado. O oceano engoliu o teu save!")
                
    print(Fore.CYAN + Style.BRIGHT + f"{'='*65}\n")        
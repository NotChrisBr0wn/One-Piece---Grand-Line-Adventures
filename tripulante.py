# Vamos ver se sai daqui o melhor jogo de one piece (via texto :P)

class Tripulante:
    def __init__ (self, nome:str, recompensa:float = 0.0, poder:int = 0, fruta:str = "Nenhuma", energia:int = 100, status:str = "Ok"):
        self.nome = nome
        self.recompensa = recompensa
        self.poder = poder
        self.fruta = fruta
        self.energia = energia
        self.status = status

    # Getters e Setters

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor: str):
        self._nome = valor

    @property
    def fruta(self):
        return self._fruta
    
    @fruta.setter
    def fruta(self, valor: str):
        self._fruta = valor

    @property
    def poder(self):
        return self._poder
    
    @poder.setter
    def poder(self, valor: int):
        if 0 <= valor <= 100:
            self._poder = valor
        else:
            raise ValueError(f"O poder de {self.nome} deve ser um valor entre 0 e 100.")
        
    @property
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, valor: int):
        if 0 <= valor <= 100:
            self._energia = valor
        else:
            raise ValueError(f"A energia de {self.nome} deve ser um valor entre 0 e 100.") 
    
    @property
    def recompensa(self):
        return self._recompensa
    
    @recompensa.setter
    def recompensa(self, valor: float):
        if valor >= 0:
            self._recompensa = valor
        else:
            raise ValueError(f"A recompensa de {self.nome} não pode ser menor que 0.")
        
    # Métodos

    def trabalhar(self, tempo: int):
        # se está sem energia, não pode trabalhar
        if self.energia == 0:
            print(f"{self.nome} está muito cansado para trabalhar. Descanse primeiro.")
            return
        
        # 1 hora de trabalho gasta 5 de energia
        energia_necessaria = tempo * 5 # energia necessaria para trabalhar
        energia_gasta = min(self.energia, energia_necessaria) # a energia gasta vai ser o mínimo entre a atual e a necessaria
        self.energia -= energia_gasta

        if energia_gasta < energia_necessaria:
            print(f"{self.nome} trabalhou mais do que devia e acabou por desmaiar!")
        else:
            print(f"{self.nome} trabalhou por {tempo} horas e gastou {energia_gasta} de energia.")

    def descansar(self): # Recupera toda a energia
        self.energia = 100
        print(f"{self.nome} descansou e recuperou toda a energia.")
    
    def executar_acao(self, navio):
        print(f"{self.nome} olha para os lados e não sabe o que fazer...")

    # Ordenação Personalizada
    def __lt__(self, outro):
        
        if self.poder == outro.poder:
            return self.recompensa < outro.recompensa
        
        return self.poder < outro.poder
    
    # Retorna o objeto
    def __str__(self):
        return f"Nome: {self.nome} Classe: [{type(self).__name__}] Recompensa: {self.recompensa} Poder: {self.poder} Fruta: {self.fruta} Energia: {self.energia} Status: {self.status}"
    
    def to_dict(self):
        # Converter o objeto num dicionário
        return {
            "nome": self.nome,
            "recompensa": self.recompensa,
            "poder": self.poder,
            "fruta": self.fruta,
            "energia": self.energia,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, dados: dict):
        # criar tripulante a partir de um dicionário
        return cls(
            nome=dados["nome"],
            recompensa=dados["recompensa"],
            poder=dados["poder"],
            fruta=dados["fruta"],
            energia=dados["energia"],
            status=dados.get("status", "Ok"), 
        )



    
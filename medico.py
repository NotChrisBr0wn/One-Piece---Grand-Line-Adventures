from tripulante import Tripulante

class Medico(Tripulante):
    def __init__(self, nome: str, recompensa: float, poder: int, fruta: str = "Nenhuma",  energia: int = 100, status: str = "Ok", pacientes_curados: int = 0):
        super().__init__(nome, recompensa, poder, fruta, energia, status)
        self.pacientes_curados = pacientes_curados

    @property
    def pacientes_curados(self):
        return self._pacientes_curados
    
    @pacientes_curados.setter
    def pacientes_curados(self, valor: int):
        if valor >= 0:
            self._pacientes_curados = valor
        else:
            raise ValueError("Os pacientes curados não podem ser negativos.")

    def __str__(self):
        return f"{super().__str__()} | Pacientes Curados: {self.pacientes_curados}"
    
    def executar_acao(self, navio):
        if not navio._tripulacao:
            print(f"🩺 {self.nome} tem as ligaduras prontas, mas não há ninguém no navio para curar!")
            return

        # 
        paciente = min(navio._tripulacao, key=lambda p: p.energia)
        
        nova_energia = paciente.energia + 40
        paciente.energia = min(100, nova_energia)
        
        self.pacientes_curados += 1
        print(f"💉 {self.nome} encontrou {paciente.nome} ferido e tratou-o!")
        print(f"❤️ A energia de {paciente.nome} subiu para {paciente.energia}%. (Pacientes curados: {self.pacientes_curados})")
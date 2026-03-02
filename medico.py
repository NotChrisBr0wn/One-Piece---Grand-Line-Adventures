from tripulante import Tripulante

class Medico(Tripulante):
    def __init__(self, nome: str, fruta: str, recompensa: float, poder: int, energia: int = 100, status: str = "Ok", pacientes_curados: int = 0):
        super().__init__(nome, fruta, recompensa, poder, energia, status)
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
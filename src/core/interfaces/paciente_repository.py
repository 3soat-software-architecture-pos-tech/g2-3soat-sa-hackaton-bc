from abc import ABC, abstractmethod
from typing import List
from src.core.entities.paciente import Paciente

class PacienteRepository(ABC): 
		@abstractmethod
		def add_paciente(self, paciente: Paciente) -> None:
				pass
		
		@abstractmethod
		def get_pacientes(self) -> List[Paciente]:
				pass
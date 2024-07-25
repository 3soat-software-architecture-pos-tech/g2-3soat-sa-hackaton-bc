from abc import ABC, abstractmethod
from typing import List
from src.core.entities.prontuario import Prontuario

class ProntuarioRepository(ABC): 
		@abstractmethod
		def get_prontuario(self, prontuario_id: str) -> Prontuario:
				pass
		
		@abstractmethod
		def get_prontuarios_by_paciente(self, paciente_id: str) -> List[Prontuario]:
				pass
		
		@abstractmethod
		def get_prontuarios_by_medico(self, paciente_id: str, medico_id: str) -> List[Prontuario]:
				pass

		# @abstractmethod
		# def get_prontuarios(self, medico_id: str, paciente_id: str) -> List[Prontuario]:
		# 		pass

		@abstractmethod
		def add_prontuario(self, prontuario: Prontuario) -> None:
				pass

		@abstractmethod
		def update_prontuario(self, prontuario_id: str, prontuario: Prontuario) -> None:
				pass

		@abstractmethod
		def delete_prontuario(self, prontuario_id: str) -> None:
				pass
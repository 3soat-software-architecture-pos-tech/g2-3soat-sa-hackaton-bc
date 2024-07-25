from src.core.entities.prontuario import Prontuario
from src.core.interfaces.prontuario_repository import ProntuarioRepository

class AddProntuarioUseCase:
	def __init__(self, prontuario_repo: ProntuarioRepository):
		self.prontuario_repo = prontuario_repo

	def execute(self, prontuario: Prontuario):
		return self.prontuario_repo.add_prontuario(prontuario)
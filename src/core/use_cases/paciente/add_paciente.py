from src.core.entities.paciente import Paciente
from src.core.interfaces.paciente_repository import PacienteRepository

class AddPacienteUseCase:
		def __init__(self, paciente_repo: PacienteRepository):
				self.paciente_repo = paciente_repo

		def execute(self, paciente: Paciente):
				return self.paciente_repo.add_paciente(paciente)
from src.core.interfaces.paciente_repository import PacienteRepository

class GetPacientesUseCase:
		def __init__(self, paciente_repo: PacienteRepository):
				self.paciente_repo = paciente_repo

		def execute(self):
				return self.paciente_repo.get_pacientes()
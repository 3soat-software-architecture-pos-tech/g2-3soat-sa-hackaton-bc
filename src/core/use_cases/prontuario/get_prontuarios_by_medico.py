from src.core.interfaces.prontuario_repository import ProntuarioRepository

class GetProntuariosByMedicoUseCase:
		def __init__(self, prontuario_repo: ProntuarioRepository):
				self.prontuario_repo = prontuario_repo

		def execute(self, id_paciente: str, id_medico: str):
				return self.prontuario_repo.get_prontuarios_by_medico(id_paciente, id_medico)
from typing import Optional
from src.core.entities.doctor import Doctor
from src.core.interfaces.doctor_repository import DoctorRepository

class GetDoctorsUseCase:
		def __init__(self, doctor_repo: DoctorRepository):
				self.doctor_repo = doctor_repo

		def execute(self, avaliacao: Optional[str] = None, distancia: Optional[str] = None, especialidade: Optional[str] = None):
				return self.doctor_repo.get_doctors(avaliacao, distancia, especialidade)
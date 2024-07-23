from core.entities.doctor import Doctor
from core.interfaces.doctor_repository import DoctorRepository

class GetDoctorsUseCase:
		def __init__(self, doctor_repo: DoctorRepository):
				self.doctor_repo = doctor_repo

		def execute(self):
				return self.doctor_repo.get_doctors()
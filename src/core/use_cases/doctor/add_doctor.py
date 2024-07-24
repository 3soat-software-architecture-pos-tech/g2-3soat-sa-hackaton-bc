from src.core.entities.doctor import Doctor
from src.core.interfaces.doctor_repository import DoctorRepository

class AddDoctorUseCase:
		def __init__(self, doctor_repo: DoctorRepository):
				self.doctor_repo = doctor_repo

		def execute(self, doctor: Doctor):
				return self.doctor_repo.add_doctor(doctor)
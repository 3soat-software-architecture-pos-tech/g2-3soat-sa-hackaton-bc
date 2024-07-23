from abc import ABC, abstractmethod
from typing import List
from src.core.entities.doctor import Doctor

class DoctorRepository(ABC): 
		@abstractmethod
		def get_doctor(self, doctor_id: str) -> Doctor:
				pass

		@abstractmethod
		def get_doctors(self) -> List[Doctor]:
				pass

		@abstractmethod
		def add_doctor(self, doctor: Doctor) -> None:
				pass

		@abstractmethod
		def update_doctor(self, doctor_id: str, doctor: Doctor) -> None:
				pass

		@abstractmethod
		def delete_doctor(self, doctor_id: str) -> None:
				pass
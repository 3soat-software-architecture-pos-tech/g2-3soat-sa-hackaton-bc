from pydantic import BaseModel

class Doctor(BaseModel):
		id: int
		name: str
		cpf: str
		crm: str
		email: str
		phone: str
		specialty: str

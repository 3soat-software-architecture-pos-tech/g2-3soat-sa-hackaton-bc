from pydantic import BaseModel

class Especialidade(BaseModel):
		id: str
		especialidade: str

class Doctor(BaseModel):
		id: str
		nome: str
		cpf: str
		crm: str
		email: str
		telefone: str
		especialidade: Especialidade
		distancia: int
		avaliacao: int


# {
# 	"id": "1",
# 	"nome": "Dr. House",
# 	"cpf": "123.456.789-00",
# 	"crm": "123456",
# 	"email": "",
# 	"telefone": "(11) 99999-9999",
# 	"especialidade": {
# 		"id": "1",
# 		"especialidade": "Cardiologista"
# 	},
# 	"distancia": "5",
# 	"avaliacao": "4.5"
# }

# {
# 	"id": "2",
# 	"nome": "Dr. Murilo",
# 	"cpf": "123.456.789-00",
# 	"crm": "2345678",
# 	"email": "",
# 	"telefone": "(11) 99999-9999",
# 	"especialidade": {
# 		"id": "2",
# 		"especialidade": "Clinico Geral"
# 	},
# 	"distancia": "2 km",
# 	"avaliacao": "5"
# }
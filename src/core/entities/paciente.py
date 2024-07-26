from pydantic import BaseModel

class Paciente(BaseModel):
	id: str
	nome: str
	cpf: str
	email: str
	telefone: str
	data_nascimento: str
	endereco: str
	cep: str
	cidade: str
	estado: str


# def to_dict(self):
# 		data = self.dict()
# 		data['peso'] = Decimal(str(data['peso']))
# 		data['altura'] = Decimal(str(data['altura']))
# 		return data

# {
# 	"id": "1",
# 	"nome": "Rafael Silva",
# 	"cpf": "123.456.789-00",
# 	"email": "rafaelsilva@gmail.com",
# 	"telefone": "(11) 99999-9999",
# 	"data_nascimento": "01/01/1990",
# 	"endereco": "Rua dos Bobos",
# 	"cep": "12345-678",
# 	"cidade": "São Paulo",
# 	"estado": "SP"
# }
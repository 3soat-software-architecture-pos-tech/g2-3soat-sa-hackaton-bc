from pydantic import BaseModel
from typing import List

class MedicosAutorizados(BaseModel):
	id: str
	validade: str

class Prontuario(BaseModel):
	id: str
	id_paciente: str
	id_medico: str
	consulta_data: str
	sintomas: str
	diagnostico: str
	tratamento: str
	remedios_receitados: str
	observacoes: str
	tipoArquivo: str
	arquivo: str
	medicos_autorizados: List[MedicosAutorizados]


# {
# 	"id": "234",
# 	"id_paciente": "1",
# 	"id_medico": "1",
# 	"consulta_data": "2021-05-01",
# 	"sintomas": "Dor de cabeça",
# 	"diagnostico": "Enxaqueca",
# 	"tratamento": "Repouso",
# 	"remedios_receitados": "Dipirona",
# 	"observacoes": "Paciente precisa de repouso",
# 	"tipoArquivo": "pdf",
# 	"arquivo": "https://www.s3.com/arquivo.pdf",
# 	"medicos_autorizados": [
# 		{
# 			"id": "1",
# 			"validade": "2021-05-01"
# 		}
# 	]
# }
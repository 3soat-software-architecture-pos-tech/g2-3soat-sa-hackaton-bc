from typing import List
import boto3
from boto3.dynamodb.conditions import Key
from src.core.entities.paciente import Paciente
from src.core.interfaces.paciente_repository import PacienteRepository

class DynamoDBPacienteRepository(PacienteRepository):
	def __init__(self):
		self.dynamodb = boto3.resource('dynamodb')
		self.table = self.dynamodb.Table('Pacientes')
	
	def get_pacientes(self) -> List[Paciente]:
		response = self.table.scan()
		return [Paciente(**paciente) for paciente in response['Items']]
	
	def add_paciente(self, paciente: Paciente) -> None:
		self.table.put_item(Item=paciente.dict())
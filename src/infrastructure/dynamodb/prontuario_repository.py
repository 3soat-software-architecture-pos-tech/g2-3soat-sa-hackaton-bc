from typing import List
import boto3
from boto3.dynamodb.conditions import Key, Attr
from src.core.entities.prontuario import Prontuario
from src.core.entities.prontuario import MedicosAutorizados
from src.core.interfaces.prontuario_repository import ProntuarioRepository

class DynamoDBProntuarioRepository(ProntuarioRepository):
	def __init__(self):
		self.dynamodb = boto3.resource('dynamodb')
		self.table = self.dynamodb.Table('Prontuarios')

	def get_prontuario(self, prontuario_id: str) -> Prontuario:
		response = self.table.query(
			KeyConditionExpression=Key('id').eq(prontuario_id)
		)
		return Prontuario(**response['Items'][0])

	def get_prontuarios_by_paciente(self, id_paciente: str) -> List[Prontuario]:
		response = self.table.query(
			IndexName='PacienteIndex',
			KeyConditionExpression=Key('id_paciente').eq(id_paciente)
		)
		return [Prontuario(**prontuario) for prontuario in response['Items']]
	
	def get_prontuarios_by_medico(self, id_paciente: str, id_medico: str) -> List[Prontuario]:
		response = self.table.query(
			IndexName='PacienteIndex',
			KeyConditionExpression=Key('id_paciente').eq(id_paciente),
			FilterExpression=Attr('id_medico').eq(id_medico)
		)
		return [Prontuario(**prontuario) for prontuario in response['Items']]
	
	def add_prontuario(self, prontuario: Prontuario) -> None:
		self.table.put_item(Item=prontuario.dict())

	def update_prontuario(self, prontuario_id: str, id_medico: str, validade: str) -> None:
		novo_medico_auth = MedicosAutorizados(id=id_medico, validade=validade)
		self.table.update_item(
			Key={'id': prontuario_id},
			UpdateExpression='SET medicos_autorizados = list_append(medicos_autorizados, :medicos_autorizados)',
			ExpressionAttributeValues={':medicos_autorizados': novo_medico_auth.dict()},
			ReturnValues="UPDATED_NEW"
		)

	def delete_prontuario(self, prontuario_id: str) -> None:
		self.table.delete_item(Key={'id': prontuario_id})
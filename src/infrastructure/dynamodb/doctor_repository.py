from typing import List, Optional
import boto3
from boto3.dynamodb.conditions import Key, Attr
from src.core.entities.doctor import Doctor
from src.core.interfaces.doctor_repository import DoctorRepository

class DynamoDBDoctorRepository(DoctorRepository):
	def __init__(self):
		self.dynamodb = boto3.resource('dynamodb')
		self.table = self.dynamodb.Table('Doctors')

	def get_doctor(self, doctor_id: str) -> Doctor:
		response = self.table.query(
			KeyConditionExpression=Key('id').eq(doctor_id)
		)
		return Doctor(**response['Items'][0])
	
	def get_doctors(self, avaliacao: Optional[str] = None, distancia: Optional[str] = None, especialidade: Optional[str] = None) -> List[Doctor]:
		filter_conditions = []
		if avaliacao is not None:
				filter_conditions.append(Attr('avaliacao').gte(int(avaliacao)))
		if distancia is not None:
				filter_conditions.append(Attr('distancia').lte(int(distancia)))
		if especialidade is not None:
				filter_conditions.append(Attr('especialidade.id').eq(especialidade))

		filter_expression = None
		if filter_conditions:
			filter_expression = filter_conditions[0]
			for condition in filter_conditions[1:]:
					filter_expression &= condition
			
			response = self.table.scan(
					FilterExpression=filter_expression
			)
		else:
				response = self.table.scan()
		# return response.get('Items', [])
		return [Doctor(**doctor) for doctor in response['Items']]
	
	def add_doctor(self, doctor: Doctor) -> None:
		self.table.put_item(Item=doctor.dict())

	def update_doctor(self, doctor_id: str, doctor: Doctor) -> None:
		self.table.update_item(
			Key={'id': doctor_id},
			UpdateExpression='SET nome = :nome, cpf = :cpf, crm = :crm, email = :email, telefone = :telefone, especialidade = :especialidade',
			ExpressionAttributeValues={
				':nome': doctor.nome,
				':cpf': doctor.cpf,
				':crm': doctor.crm,
				':email': doctor.email,
				':telefone': doctor.telefone,
				':especialidade': doctor.especialidade
			}
		)

	def delete_doctor(self, doctor_id: str) -> None:
		self.table.delete_item(Key={'id': doctor_id})
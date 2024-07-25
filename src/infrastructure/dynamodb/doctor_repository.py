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
		if avaliacao:
				filter_conditions.append(Attr('avaliacao').eq(avaliacao))
		if distancia:
				filter_conditions.append(Attr('distancia').eq(distancia))
		if especialidade:
				filter_conditions.append(Attr('especialidade.id').eq(especialidade))

		if filter_conditions:
				print(filter_conditions)
				filter_expression = filter_conditions[0]
				for condition in filter_conditions[1:]:
						filter_expression = filter_expression & condition
		else:
				filter_expression = None

		response = self.table.scan(FilterExpression=filter_expression) if filter_expression else self.table.scan()
		# response = self.table.scan()
		return [Doctor(**doctor) for doctor in response['Items']]
	
	def add_doctor(self, doctor: Doctor) -> None:
		self.table.put_item(Item=doctor.dict())

	def update_doctor(self, doctor_id: str, doctor: Doctor) -> None:
		self.table.update_item(
			Key={'id': doctor_id},
			UpdateExpression='SET name = :name, cpf = :cpf, crm = :crm, email = :email, phone = :phone, specialty = :specialty',
			ExpressionAttributeValues={
				':name': doctor.name,
				':cpf': doctor.cpf,
				':crm': doctor.crm,
				':email': doctor.email,
				':phone': doctor.phone,
				':specialty': doctor.specialty
			}
		)

	def delete_doctor(self, doctor_id: str) -> None:
		self.table.delete_item(Key={'id': doctor_id})
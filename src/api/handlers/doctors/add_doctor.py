import json
from src.core.entities.doctor import Doctor
from src.core.use_cases.doctor.add_doctor import AddDoctorUseCase
from src.infrastructure.dynamodb.doctor_repository import DynamoDBDoctorRepository

def add_doctor_handler(event, context):
		doctor = Doctor(**json.loads(event['body']))
		repository = DynamoDBDoctorRepository()
		use_case = AddDoctorUseCase(repository)
		use_case.execute(doctor)

		return {
				'statusCode': 200,
				'body': json.dumps(doctor.model_dump())
		}
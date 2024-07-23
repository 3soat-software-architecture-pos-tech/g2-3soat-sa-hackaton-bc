
import json
from core.entities.doctor import Doctor
from core.use_cases.doctor.add_doctor import AddDoctorUseCase
from infrastructure.dynamodb.doctor_repository import DynamoDBDoctorRepository

def main(event, context):
		doctor = Doctor(**json.loads(event['body']))
		repository = DynamoDBDoctorRepository()
		use_case = AddDoctorUseCase(repository)
		use_case.execute(doctor)

		return {
				'statusCode': 200,
				'body': json.dumps(doctor.model_dump())
		}
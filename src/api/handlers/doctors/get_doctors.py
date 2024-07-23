import json
from core.use_cases.doctor.get_doctors import GetDoctorsUseCase
from infrastructure.dynamodb.doctor_repository import DynamoDBDoctorRepository


def main(event, context):
	repository = DynamoDBDoctorRepository()
	use_case = GetDoctorsUseCase(repository)
	doctors = use_case.execute()

	return {
		'statusCode': 200,
		'body': json.dumps([doctor.model_dump() for doctor in doctors])
	}
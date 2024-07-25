import json
from src.core.use_cases.doctor.get_doctors import GetDoctorsUseCase
from src.infrastructure.dynamodb.doctor_repository import DynamoDBDoctorRepository


def get_doctors_handler(event, context):
	query_params = event.get('queryStringParameters', {})  
	if query_params is None:
			query_params = {}
	avaliacao = query_params.get('avaliacao', None)
	distancia = query_params.get('distancia', None)
	especialidade = query_params.get('especialidade', None)

	repository = DynamoDBDoctorRepository()
	use_case = GetDoctorsUseCase(repository)
	doctors = use_case.execute(avaliacao, distancia, especialidade)

	return {
		'statusCode': 200,
		'body': json.dumps([doctor.model_dump() for doctor in doctors])
	}
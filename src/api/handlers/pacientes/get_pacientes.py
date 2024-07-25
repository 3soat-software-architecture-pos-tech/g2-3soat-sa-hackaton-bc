import json
from src.core.use_cases.paciente.get_pacientes import GetPacientesUseCase
from src.infrastructure.dynamodb.paciente_repository import DynamoDBPacienteRepository


def get_pacientes_handler(event, context):
	repository = DynamoDBPacienteRepository()
	use_case = GetPacientesUseCase(repository)
	pacientes = use_case.execute()

	return {
		'statusCode': 200,
		'body': json.dumps([paciente.model_dump() for paciente in pacientes])
	}
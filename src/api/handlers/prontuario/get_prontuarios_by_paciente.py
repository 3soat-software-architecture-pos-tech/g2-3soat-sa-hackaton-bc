import json
from src.core.use_cases.prontuario.get_prontuarios_by_paciente import GetProntuariosByPacienteUseCase
from src.infrastructure.dynamodb.prontuario_repository import DynamoDBProntuarioRepository


def get_prontuarios_by_paciente_handler(event, context):
	id_paciente = event['pathParameters']['idPaciente']

	repository = DynamoDBProntuarioRepository()
	use_case = GetProntuariosByPacienteUseCase(repository)
	prontuarios = use_case.execute(id_paciente)

	return {
		'statusCode': 200,
		'body': json.dumps([prontuario.model_dump() for prontuario in prontuarios])
	}
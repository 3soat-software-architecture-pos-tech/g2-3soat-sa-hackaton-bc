import json
from src.core.use_cases.prontuario.get_prontuarios_by_medico import GetProntuariosByMedicoUseCase
from src.infrastructure.dynamodb.prontuario_repository import DynamoDBProntuarioRepository


def get_prontuarios_by_medico_handler(event, context):
		id_paciente = event['pathParameters']['idPaciente']
		id_medico = event['pathParameters']['idMedico']

		repository = DynamoDBProntuarioRepository()
		use_case = GetProntuariosByMedicoUseCase(repository)
		prontuarios = use_case.execute(id_paciente, id_medico)

		return {
				'statusCode': 200,
				'body': json.dumps([prontuario.model_dump() for prontuario in prontuarios])
		}
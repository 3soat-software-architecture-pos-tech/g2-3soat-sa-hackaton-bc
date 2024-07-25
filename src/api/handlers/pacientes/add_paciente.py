import json
from src.core.entities.paciente import Paciente
from src.core.use_cases.paciente.add_paciente import AddPacienteUseCase
from src.infrastructure.dynamodb.paciente_repository import DynamoDBPacienteRepository

def add_paciente_handler(event, context):
		paciente = Paciente(**json.loads(event['body']))
		repository = DynamoDBPacienteRepository()
		use_case = AddPacienteUseCase(repository)
		use_case.execute(paciente)

		return {
			'statusCode': 200,
			'body': json.dumps(paciente.model_dump())
		}
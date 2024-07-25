import json
from src.core.entities.prontuario import Prontuario
from src.core.use_cases.prontuario.add_prontuario import AddProntuarioUseCase
from src.infrastructure.dynamodb.prontuario_repository import DynamoDBProntuarioRepository

def add_prontuario_handler(event, context):
		prontuario = Prontuario(**json.loads(event['body']))
		repository = DynamoDBProntuarioRepository()
		use_case = AddProntuarioUseCase(repository)
		use_case.execute(prontuario)

		return {
				'statusCode': 200,
				'body': json.dumps(prontuario.model_dump())
		}
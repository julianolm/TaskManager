import json

class SearchTaskController():
    def __init__(self, searchTaskUseCase):
        self.searchTaskUseCase = searchTaskUseCase

    def handle(self, request):
        try:
            text_to_search = request['body']['text_to_search']
            tasks = self.searchTaskUseCase.execute(text_to_search)
            serialized_tasks = [task.serialize() for task in tasks]
            return {
                'statusCode': 200,
                'body': json.dumps({"tasks": serialized_tasks}),
            }
        except KeyError as e:
            return {
                'statusCode': 400,
                'body': json.dumps({"message": f'Request body missing on field: {str(e)}'}),
            }
        except Exception as e:
            return {
                'statusCode': 400,
                'body': json.dumps({"message": str(e)}),
            }
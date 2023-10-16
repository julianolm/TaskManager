import json

from . SearchTaskUseCase import SearchTaskUseCase

class SearchTaskController():
    def __init__(self, searchTaskUseCase: SearchTaskUseCase):
        self.searchTaskUseCase = searchTaskUseCase

    def handle(self, request):
        try:
            text_to_search = request['body']['text_to_search']
            tasks = self.searchTaskUseCase.execute(text_to_search)
            return {
                'statusCode': 200,
                'body': json.dumps({"tasks": tasks}),
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
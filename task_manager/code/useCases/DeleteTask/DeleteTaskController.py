import json

class DeleteTaskController():
    def __init__(self, deleteTaskUseCase):
        self.deleteTaskUseCase = deleteTaskUseCase

    def handle(self, request):
        # get data from request

        # validate request data

        try:
            tasks = self.deleteTaskUseCase.execute(request)
            return {
                'statusCode': 200,
                'body': json.dumps({"tasks": tasks}),
            }
        except Exception as e:
            return {
                'statusCode': 400,
                'body': json.dumps({"message": str(e)}),
            }
        # Verificar como essa exception esta sendo retornada no JSON ----------------------------------
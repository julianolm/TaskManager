import json

class MapTaskController():
    def __init__(self, mapTaskUseCase):
        self.mapTaskUseCase = mapTaskUseCase

    def handle(self, request):
        # get data from request

        # validate request data

        try:
            tasks = self.mapTaskUseCase.execute(request)
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
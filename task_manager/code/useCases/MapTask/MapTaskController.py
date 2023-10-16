import json

from . MapTaskUseCase import MapTaskUseCase

class MapTaskController():
    def __init__(self, mapTaskUseCase: MapTaskUseCase):
        self.mapTaskUseCase = mapTaskUseCase

    def handle(self, request):
        try:
            task_id = request['body']['task_id']
            mapped_task = self.mapTaskUseCase.execute(task_id)
            return {
                'statusCode': 200,
                'body': json.dumps({"task": mapped_task}),
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
import json

from . DeleteTaskUseCase import DeleteTaskUseCase

class DeleteTaskController():
    def __init__(self, deleteTaskUseCase: DeleteTaskUseCase):
        self.deleteTaskUseCase = deleteTaskUseCase

    def handle(self, request):
        try:
            task_id = request['body']['task_id']
            new_dataset = self.deleteTaskUseCase.execute(task_id)
            return {
                'statusCode': 200,
                'body': json.dumps({"dataset": new_dataset}),
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
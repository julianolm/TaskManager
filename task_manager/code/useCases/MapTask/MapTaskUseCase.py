from repositories.TaskBoardRepository import TaskBoardRepository

class MapTaskUseCase():
    def __init__(self, task_board_repository: TaskBoardRepository):
        self.task_board_repository = task_board_repository

    def execute(self, task_id):
        task = self.task_board_repository.get_task_by_id(task_id)
        serialized_task = task.serialize_cascading()

        return serialized_task
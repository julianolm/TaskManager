from repositories.TaskBoardRepository import TaskBoardRepository

class DeleteTaskUseCase():
    def __init__(self, task_board_repository: TaskBoardRepository):
        self.task_board_repository = task_board_repository

    def execute(self, task_id):
        task = self.task_board_repository.get_task_by_id(task_id)
        self.task_board_repository.delete(task)
        new_dataset = self.task_board_repository.export_dataset()
        return new_dataset
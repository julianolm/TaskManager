class DeleteTaskUseCase():
    def __init__(self, task_board_repository):
        self.task_board_repository = task_board_repository

    def execute(self, task_id):
        return self.task_board_repository.delete(task_id)
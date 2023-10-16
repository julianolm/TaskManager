class MapTaskUseCase():
    def __init__(self, task_board_repository):
        self.task_board_repository = task_board_repository

    def execute(self, task_id):
        return self.task_board_repository.map(task_id)
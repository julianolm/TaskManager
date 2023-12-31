from repositories.TaskBoardRepository import TaskBoardRepository

class SearchTaskUseCase():
    def __init__(self, task_board_repository: TaskBoardRepository):
        self.task_board_repository = task_board_repository

    def execute(self, text_to_search: str):
        ids = self.task_board_repository.get_ids_by_text(text_to_search)
        tasks = self.task_board_repository.get_tasks_by_ids(ids)
        serialized_tasks = [task.serialize() for task in tasks]

        return serialized_tasks
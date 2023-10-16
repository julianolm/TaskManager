class SearchTaskUseCase():
    def __init__(self, task_board_repository):
        self.task_board_repository = task_board_repository

    def execute(self, text_to_search):
        return self.task_board_repository.search(text_to_search)
from repositories.TaskBoardRepository import TaskBoardRepository
from . SearchTaskUseCase import SearchTaskUseCase
from .SearchTaskController import SearchTaskController

def SearchTask():
    task_board_repository = TaskBoardRepository()
    search_task_use_case = SearchTaskUseCase(task_board_repository)
    search_task_controller = SearchTaskController(search_task_use_case)

    return search_task_controller

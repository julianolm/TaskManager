from repositories.TaskBoardRepository import TaskBoardRepository
from . DeleteTaskUseCase import DeleteTaskUseCase
from .DeleteTaskController import DeleteTaskController

def DeleteTask():
    task_board_repository = TaskBoardRepository()
    delete_task_use_case = DeleteTaskUseCase(task_board_repository)
    delete_task_controller = DeleteTaskController(delete_task_use_case)

    return delete_task_controller

from repositories.TaskBoardRepository import TaskBoardRepository
from . MapTaskUseCase import MapTaskUseCase
from .MapTaskController import MapTaskController

def MapTask():
    task_board_repository = TaskBoardRepository()
    map_task_use_case = MapTaskUseCase(task_board_repository)
    map_task_controller = MapTaskController(map_task_use_case)

    return map_task_controller

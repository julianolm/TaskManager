from typing import List, Dict
from io import StringIO
import csv

from .Task import Task

class TaskBoard:
    expected_header = ["Parent", "ID", "Status", "Title", "Description"]

    def __init__(self, data: str):
        # encontrar uma forma de nao acessar diretamente as root_tasks
        # pq listas sao mutaveis e entao poderiam editar a lista
        # sem passar pela funcao de add/delete
        self.data = data
        self.root_tasks: List[Task] = self.__build_task_board()

    def __check_csv_header(self, csv_string):
        # Use StringIO to treat the CSV string as a file-like object
        with StringIO(csv_string) as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
        if header != self.expected_header:
            raise Exception(f"Error: CSV header does not match the expected format. Expected: {self.expected_header}, Found: {header}", 400)
        return None

    def __build_task_board(self):
        csv_string = self.data
        header_check_result = self.__check_csv_header(csv_string)

        if header_check_result:
            return header_check_result

        task_dict: Dict[str, 'Task'] = {}  # Use a dictionary to store tasks temporarily based on their IDs
        
        # Use StringIO to treat the CSV string as a file-like object
        with StringIO(csv_string) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row

            for row in csv_reader:
                parent_id, task_id, status, title, description = row
                task = Task(task_id, status, title, description)
                task_dict[task_id] = task

        root_tasks: List['Task'] = []
        # Now that we have all the tasks in a dictionary, we can build the tree
        with StringIO(csv_string) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row

            for row in csv_reader:
                parent_id, task_id, _, _, _ = row
                task = task_dict[task_id]
                parent_id = parent_id
                if parent_id in task_dict:
                    parent_task = task_dict[parent_id]
                    parent_task.children.append(task)
                    task.parent = parent_task
                else:
                    root_tasks.append(task)
        
        return root_tasks

    def __str__(self):
        return "\n".join([str(task) for task in self.root_tasks])
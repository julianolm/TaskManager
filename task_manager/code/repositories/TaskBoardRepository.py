from typing import List, Dict, Literal, Optional
from io import StringIO
import csv

from utils.patterns import Singleton

class Task:
    StatusType = Literal["Not Started", "In Progress", "Under Review", "On Hold", "Deployed", "Testing"]

    def __init__(self, id: str, status: StatusType, title: str, description: str):
        self.parent: Optional['Task'] = None
        self.children: List['Task'] = []
        self.id = id
        self.status = status
        self.title = title
        self.description = description

    def add_child(self, child: 'Task'):
        self.children.append(child)

    def set_parent(self, parent: 'Task'):
        self.parent = parent

    def __str__(self):
        return (
            f"  Parent: {self.parent.id if self.parent else 'root'}\n"
            f"  ID: {self.id}\n"
            f"  Status: {self.status}\n"
            f"  Title: {self.title}\n"
            f"  Description: {self.description}\n"
            f"  Children: {[child.id for child in self.children]}"
        )

"""
Here I got to a very interesting point. I dont know how to make a division between the model and the repository.
I mean, I think I should have a class to represent a task board, just reflecting its state and with very basic methods and attributes.

On the other hand, I think I should have a repository class that would be responsible for the CRUD operations and for the
persistence of the data. This class would have a reference to the task board class and would be responsible for
manipulating it.

I'm still trying to figure out a clear frontier between those two, but still dont know how to do it.
"""
class TaskBoardRepository(metaclass=Singleton):
    expected_header = ["Parent", "ID", "Status", "Title", "Description"]

    def __init__(self, data: str):
        self.data = data
        self.root_tasks: List['Task'] = self.__build_task_forest()

    def __check_csv_header(self, csv_string):
        # Use StringIO to treat the CSV string as a file-like object
        with StringIO(csv_string) as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
        if header != self.expected_header:
            raise Exception(f"Error: CSV header does not match the expected format. Expected: {self.expected_header}, Found: {header}", 400)
        return None

    def __build_task_forest(self):
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

    """Below are the functions that will be part of the repository (and not of the model/class)"""

    # rename to export_dataset
    def csv(self):
        # Helper function to recursively build the CSV string starting from a task
        def task_csv(task: Task):
            csv_string = ""
            title = task.title if ',' not in task.title else f'"{task.title}"'
            description = task.description if ',' not in task.description else f'"{task.description}"'
            fields = [task.parent.id if task.parent else "root", task.id, task.status, title, description]
            csv_string += ",".join(fields)
            for child in task.children:
                csv_string += "\n" + task_csv(child)
            return csv_string
        # Build the CSV string starting from each root task
        csv_string = ",".join(self.expected_header) + "\n"
        for task in self.root_tasks:
            csv_string += task_csv(task)
        return csv_string

    def search(self, text_to_search):
        return "Busca realizada com sucesso do texto: " + text_to_search
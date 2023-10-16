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
            f"ID: {self.id}\n"
            f"Status: {self.status}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Parent: {self.parent.id if self.parent else 'root'}\n"
            f"Children: {[child.id for child in self.children]}"
        )

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "title": self.title,
            "description": self.description,
            "children": [child.id for child in self.children]
        }

    def serialize_cascading(self):
        return {
            "id": self.id,
            "status": self.status,
            "title": self.title,
            "description": self.description,
            "children": [child.serialize_cascading() for child in self.children]
        }

"""
Here I got to a very interesting point. I dont know how to make a division between the model and the repository.
I mean, I think I should have a class to represent a task board, just reflecting its state and with very basic methods and attributes, 
and another class that would be responsible for the CRUD operations and for the persistence of the data. Threrfore a class to represent the
board 'TaskBoard' and other to provide the repository 'TaskBoardRepository'.

I'm still trying to figure out a clear frontier between those two, but still dont know how to do it.

On the other hand, I just can't see how the two would fit together in this project. Since the repository has to be initialized with the data
incoming from the request it ends up doing everything the model would do. Therefore it seems that TaskBoard is just unncecessary.
"""
class TaskBoardRepository(metaclass=Singleton):
    expected_header = ["Parent", "ID", "Status", "Title", "Description"]

    def __init__(self, data: str):
        self.__check_csv_header(data)
        self.data = data
        self.task_dict: Dict[str, 'Task'] = self.__build_task_dict()
        self.root_tasks: List['Task'] = self.__build_task_forest()

    def __check_csv_header(self, csv_string):
        # Use StringIO to treat the CSV string as a file-like object
        with StringIO(csv_string) as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
        if header != self.expected_header:
            raise Exception(f"Error: CSV header does not match the expected format. Expected: {self.expected_header}, Found: {header}", 400)
        return None

    def __build_task_dict(self):
        csv_string = self.data
        task_dict: Dict[str, 'Task'] = {}  # Use a dictionary to store tasks temporarily based on their IDs
        # Use StringIO to treat the CSV string as a file-like object
        with StringIO(csv_string) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                parent_id, task_id, status, title, description = row
                task = Task(task_id, status, title, description)
                task_dict[task_id] = task
        return task_dict

    def __build_task_forest(self):
        csv_string = self.data
        root_tasks: List['Task'] = []
        with StringIO(csv_string) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                parent_id, task_id, _, _, _ = row
                task = self.task_dict[task_id]
                parent_id = parent_id
                if parent_id in self.task_dict:
                    parent_task = self.task_dict[parent_id]
                    parent_task.children.append(task)
                    task.parent = parent_task
                else:
                    root_tasks.append(task)
        return root_tasks

    def __str__(self):
        return "\n".join([str(task) for task in self.root_tasks])

    """Below are the functions that will be part of the repository (and not of the model/class)"""

    def get_task_by_id(self, id: str) -> Task:
        """Returns a task given its id"""
        return self.task_dict[id]
    
    def get_tasks_by_ids(self, ids: List[str]) -> list[Task]:
        """Returns a list of tasks given its ids"""
        tasks: List[Task] = []
        for id in ids:
            task = self.get_task_by_id(id)
            tasks.append(task)
        return tasks

    def get_ids_by_text(self, text_to_search: str) -> List[str]:
        """Searches for tasks that match the given text in the title or description and return a list of ids"""
    
        def match_task(task: Task):
            """Helper function to tell if a task matches the search text"""
            return text_to_search.lower() in task.title.lower() or text_to_search.lower() in task.description.lower()

        def find_tasks_by_text(tasks: List['Task'], text_to_search: str) -> List[str]:
            """Helper function to recursively find tasks that match the search text"""
            matching_tasks: List[str] = []
            for task in tasks:
                if match_task(task):
                    matching_tasks.append(task.id)

                # Recursively search in children tasks
                matching_tasks += find_tasks_by_text(task.children, text_to_search)
            return matching_tasks

        matching_tasks: List[str] = find_tasks_by_text(self.root_tasks, text_to_search)
        return matching_tasks
    
    def delete(self, task: Task):
        """Deletes a task given its id"""
        for child in task.children:
            self.delete(child)
        if task.parent:
            task.parent.children.remove(task)
        else:
            self.root_tasks.remove(task)
        del self.task_dict[task.id]

    def export_dataset(self):
        """Helper function to recursively build the CSV string starting from a task"""
        def task_csv(task: Task) -> str:
            csv_string = ""
            title = task.title if ',' not in task.title else f'"{task.title}"'
            description = task.description if ',' not in task.description else f'"{task.description}"'
            fields = [task.parent.id if task.parent else "root", task.id, task.status, title, description]
            csv_string += ",".join(fields)
            for child in task.children:
                csv_string += "\n" + task_csv(child)
            return csv_string
        """Build the CSV string starting from each root task"""
        csv_string = ",".join(self.expected_header) + "\n"
        for task in self.root_tasks:
            csv_string += task_csv(task)
        return csv_string

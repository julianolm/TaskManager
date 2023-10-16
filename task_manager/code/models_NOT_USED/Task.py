from typing import Literal, List, Optional

StatusType = Literal["Not Started", "In Progress", "Under Review", "On Hold", "Deployed", "Testing"]

class Task:
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
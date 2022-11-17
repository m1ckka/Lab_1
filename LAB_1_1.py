from typing import List, Any
from datetime import datetime


class Developer:
    def int(self, id: int,
                name: str,
                address: str,
                phone_number: str,
                email: str,
                position: int,
                rank: int,
                salary: float) -> None:
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = salary
        self.assignments = []
        self.projects: List[Any] = []

    def assign_projects(self) -> List[Any]:
        return self.projects

    def assigned(self, project):
        self.projects.append(project)

    def unassigned(self, project):
        self.projects.remove(project)


class Assignment:
    def int(self, received_tasks: dict,
                is_done: bool,
                description: str,
                status: str) -> None:
        self.received_tasks = received_tasks
        self.is_done = is_done
        self.description = description
        self.status = status

    def get_tasks_to_date(self, date: datetime):
        return [v for k, v
                in self.received_tasks.items()
                if k <= date]



class Project:
    def init(self, title: str,
                ):

        self.developers = []

    def add_developer(self, developer: Developer):
        class ProjectManager:
            def init(self, developer1):
                self.developer1 = developer1
                print("developer added")

        def remove_developer(self, developer: Developer):
            class ProjectManager:
                def del(self, developer):
                    print("developer deleted")




class QAEngineer:
    def int(self, id:int,
            name: str,
            address: str,
            phone_number: str,
            email: str,
            salary: float,
            rank: str,
            position: str
            ) -> None:
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.rank = rank
        self.position = position

    def test_feature(self, assignment) -> str:
        print(f"{assignment.title} has been tested")


class ProjectManager:
    def int(self, id:int,
            name: str,
            address: str,
            phone_number: str,
            email: str,
            salary: float,
            project: Project
            ) -> None:
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.project = Project

    def discuss_progress(self, developer):
        self.developer
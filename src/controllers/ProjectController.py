from fastapi import UploadFile

from .BaseController import BaseController
import os

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str):
        self.project_path = os.path.join(
            self.files_path, 
            project_id   
        )

        if not os.path.exists(self.project_path):
            os.makedirs(self.project_path)

        return self.project_path
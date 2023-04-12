from suds.client import Client
from suds import WebFault

from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = self.app.soap_url
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = Client(self.app.soap_url)
        projects = client.service.mc_projects_get_user_accessible(
            self.app.config['soap']['username'], self.app.config['soap']['password'])
        project_list = []
        for project in projects:
            name = project.name
            description = project.description
            status = project.status
            project_list.append(Project(name=name, description=description, status=status))
        return project_list


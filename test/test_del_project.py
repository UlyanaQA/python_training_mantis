import random

from model.project import Project


def test_delete_random_contact(app):
    app.session.ensure_login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="ProjectName", status="obsolete", description="desc"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.key_name) == sorted(new_projects, key=Project.key_name)

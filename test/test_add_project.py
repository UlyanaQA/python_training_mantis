from model.project import Project

def test_add_project(app, json_projects):
    app.session.ensure_login("administrator", "root")
    project = json_projects
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert len(old_projects) == len(new_projects)
    assert sorted(old_projects, key=Project.key_name) == sorted(new_projects, key=Project.key_name)
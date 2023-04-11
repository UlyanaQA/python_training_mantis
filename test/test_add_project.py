from model.project import Project


def test_add_new_project(app, json_projects):
    project = json_projects
    old_projects = app.soap.get_project_list(
        username=app.config["webadmin"]["username"], password=app.config["webadmin"]["password"])
    app.project.create_project(project)
    new_projects = app.soap.get_project_list(
        username=app.config["webadmin"]["username"], password=app.config["webadmin"]["password"])
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.key_name) == sorted(new_projects, key=Project.key_name)

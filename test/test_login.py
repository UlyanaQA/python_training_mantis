
def test_login(app):
    app.session.ensure_login(app.config["webadmin"]["username"], password=app.config["webadmin"]["password"])
    assert app.session.is_logged_in_as("administrator")

from model.group import Group


def test_group_change(app):
    app.session.login(login="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test_del"))
    app.group.first_group_change(Group(name="HW7_", header="HW7", footer="test"))
    app.session.logout()
def test_group_change_name(app):
    app.session.login(login="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test_del"))
    app.group.first_group_change(Group(name="New group"))
    app.session.logout()


def test_group_change_header(app):
    app.session.login(login="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test_del"))
    app.group.first_group_change(Group(header="New header"))
    app.session.logout()
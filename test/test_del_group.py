#задание 7
from model.group import Group
def test_delete_first_group(app):
    app.session.login(login="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test_del"))
    app.group.delete_first_group()
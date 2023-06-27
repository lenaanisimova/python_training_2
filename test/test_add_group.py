#задание 7
from model.group import Group

def test_add_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(Group(name="grouplena", header="grouplena1", footer="grouplena2"))

def test_add_empty_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))

  #  app.session.logout()

#задание 20
import random
from model.group import Group
from random import randrange


def test_group_change(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="grouptest"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_group_change_name(app):
#    app.session.login(login="admin", password="secret")
#    if app.group.count() == 0:
#        app.group.create(Group(name="test_del"))
#    app.group.first_group_change(Group(name="New group"))
#    app.session.logout()


#def test_group_change_header(app):
#    app.session.login(login="admin", password="secret")
#    if app.group.count() == 0:
#        app.group.create(Group(name="test_del"))
#    app.group.first_group_change(Group(header="New header"))
#    app.session.logout()
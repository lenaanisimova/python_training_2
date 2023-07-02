
#задание 13
from model.group import Group
from random import randrange


def test_group_change(app):
    if app.group.count() == 0:
        app.group.create(Group(name="grouptest"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="HW13", header="HW13", footer="test")
    group.id = old_groups[index].id
    app.group.group_change_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

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
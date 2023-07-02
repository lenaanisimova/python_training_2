#задание 13
from random import randrange
from model.contact import Contact

def test_delete_some_contact(app):
    #app.session.login(login="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Lena", last_name="Anisimova", address="Санкт-Петербург", mobile_phone="79110975564", email="elena@mail.ru", day_of_birth="02", month_of_birth="October",
                            year_of_birth="1992"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
#задание 13
from model.contact import Contact
from random import randrange

def test_first_contact_change(app):
    #app.session.login(login="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Lena", last_name="Anisimova", address="Санкт-Петербург", mobile_phone="79110975563", email="elena@mail.ru", day_of_birth="10", month_of_birth="October",
                            year_of_birth="1992"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact=Contact(first_name="Lena12", last_name="Anisimova12", address="St. Petersburg", mobile_phone="+79110975565", email="elena12@mail.ru", day_of_birth="12", month_of_birth="November",
                            year_of_birth="1983")
    app.contact.contact_change_by_index(index, contact)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

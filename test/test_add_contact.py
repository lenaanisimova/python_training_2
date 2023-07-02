#задание 7
from model.contact import Contact
def test_add_contact(app):
    #app.session.login(login="admin", password="secret")
    old_contacts = app.contact.get_contact_list()
    contact=Contact(first_name="Lena", last_name="Anisimova", address="Санкт-Петербург", mobile_phone="79110975562", email="elena@mail.ru", day_of_birth="10", month_of_birth="October",
                            year_of_birth="1992")

    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


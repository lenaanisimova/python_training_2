
from model.contact import Contact
from random import randrange

def test_first_contact_change(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.add(Contact(first_name="Lena", last_name="Anisimova", address="Санкт-Петербург",
                                mobile_phone="79110975563", work_phone="79110975566",
                                home_phone="79110975569", secondary_phone="79110975560",
                                email="elena@mail.ru", day_of_birth="10", month_of_birth="October",
                            year_of_birth="1992"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact=Contact(first_name="Lena12", last_name="Anisimova12", address="St. Petersburg",
                    mobile_phone="+79110975565", work_phone="79110975566",
                    home_phone="79110975569", secondary_phone="79110975560",
                    email="elena12@mail.ru", day_of_birth="12", month_of_birth="November",
                            year_of_birth="1983")
    contact.id = int(old_contacts[index].id)
    app.contact.contact_change_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

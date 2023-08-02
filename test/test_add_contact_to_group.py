from model.contact import Contact
from model.group import Group
import random
def test_add_contact_to_group(app, db, orm):
    # проверяем наличие хотя бы одного контакта. Если его нет - создаем
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="Elena", last_name="Anisimova", address="Санкт-Петербург", mobile_phone="7911095563", home_phone="89110975565",
            work_phone="89110975567", secondary_phone="89110975568", email="email@email.ru",
            email_2="email2@email.ru", email_3="email3@email.ru", day_of_birth="02",
            month_of_birth="November", year_of_birth="1987"))
    # выбираем случайный контакт
  #  contacts = db.get_contact_list()
   # contact = random.choice(contacts)
    # проверяем наличие хотя бы одной группы. Если её нет - создаем
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_del"))
    # выбираем случайную группу
    groups = db.get_group_list()
    group = random.choice(groups)
    # добавляем контакт в группу
    contacts_for_add_in_group = orm.get_contacts_not_in_group(group)
    if contacts_for_add_in_group == []:
        app.contact.add(Contact(first_name="Elena", last_name="Anisimova", address="Санкт-Петербург", mobile_phone="7911095563",
                    home_phone="89110975565",
                    work_phone="89110975567", secondary_phone="89110975568", email="email@email.ru",
                    email_2="email2@email.ru", email_3="email3@email.ru", day_of_birth="02",
                    month_of_birth="November", year_of_birth="1987"))
        contact_for_add_in_group = orm.get_contacts_not_in_group(group)[0]
    else:
        contact_for_add_in_group = random.choice(contacts_for_add_in_group)
    app.contact.add_contact_to_group(contact_for_add_in_group, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact_for_add_in_group in contacts_in_group
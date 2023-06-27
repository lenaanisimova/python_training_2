#задание 7
from model.contact import Contact

def test_delete_first_contact(app):
    app.session.login(login="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Lena", last_name="Anisimova", address="Санкт-Петербург", mobile_phone="79110975564", email="elena@mail.ru", day_of_birth="02", month_of_birth="October",
                            year_of_birth="1992"))
    app.contact.delete_first_contact()
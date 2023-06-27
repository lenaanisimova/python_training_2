#задание 7
from model.contact import Contact
def test_add_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.add(Contact(first_name="Lena", last_name="Anisimova", address="Санкт-Петербург", mobile_phone="79110975562", email="elena@mail.ru", day_of_birth="10", month_of_birth="October",
                            year_of_birth="1992"))


def test_add_contact_2(app):
    app.session.login(login="admin", password="secret")
    app.contact.add(Contact(first_name="Vika", last_name="Frolova", address="123", mobile_phone="123456789", email="123456@mail.ru", day_of_birth="13", month_of_birth="November",
                            year_of_birth="1987"))

    app.session.logout()
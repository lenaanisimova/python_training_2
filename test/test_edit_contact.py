from model.contact import Contact
def test_first_contact_change(app):
    app.session.login(login="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Lena", last_name="Anisimova", address="Санкт-Петербург", mobile_phone="79110975563", email="elena@mail.ru", day_of_birth="10", month_of_birth="October",
                            year_of_birth="1992"))
    app.contact.first_contact_change(Contact(first_name="Lena12", last_name="Anisimova12", address="St. Petersburg", mobile_phone="+79110975565", email="elena12@mail.ru", day_of_birth="12", month_of_birth="November",
                            year_of_birth="1983"))
    app.session.logout()
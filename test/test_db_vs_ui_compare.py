
from model.contact import Contact

def test_data_on_home_page_and_db(app, db):
    contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

    # проверяем, что длина списков совпадает (чтобы не проводить лишние проверки, если вдруг ошибка уже здесь)
    assert len(contacts_db) == len(contacts_from_home_page)

    # проверяем каждое отдельное поле
    for index in range(len(contacts_db)):
        assert contacts_from_home_page[index].first_name == contacts_db[index].first_name
        assert contacts_from_home_page[index].last_name == contacts_db[index].last_name
        assert contacts_from_home_page[index].address == contacts_db[index].address
        assert contacts_from_home_page[index].all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contacts_db[index])
        assert contacts_from_home_page[index].all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contacts_db[index])
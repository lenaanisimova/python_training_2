import re


def test_contacts_on_home_and_edit_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)


#def clear(s):
 #   return re.sub("[() -]", "", s)



#def merge_phones_like_on_home_page(contact):
#    return "\n".join(filter(lambda x: x != "",
#                            map(lambda x: clear(x),
#                                filter(lambda x: x is not None,
 #                                   [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))

#def merge_emails_like_on_home_page(contact):
 #   return "\n".join(filter(lambda x: x != "",
 #                               filter(lambda x: x is not None,
 #                                   [contact.email, contact.email_2, contact.email_3])))
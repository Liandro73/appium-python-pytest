import allure

from faker import Faker
from src.pages.contacts_page import ContactsPage as contactsPage
from src.pages.create_contact_page import CreateContactPage as createContactPage
from src.pages.contact_page import ContactPage as contactPage
from src.tests.conftest import driver, os, wait

fk = Faker()

FIRST_NAME = fk.first_name()
LAST_NAME = fk.last_name()
COMPANY = fk.company()
PHONE = fk.basic_phone_number()
ADDRESS = fk.address()
FULL_NAME = f'{FIRST_NAME} {LAST_NAME}'

@allure.suite("Contact")
@allure.title("Add Contact successfully")
@allure.description("This is a test about adding new Contacts in Android and iOS Applications")
def test_create_contact_successfully(driver, os, wait):
    allure.dynamic.tag("Contact", os, wait)
    contactsPage.verify_if_button_add_contact_is_visible(driver, os, wait)
    contactsPage.click_on_button_add_contact(driver, os, wait)
    createContactPage.fill_input_first_name(driver, os, FIRST_NAME, wait)
    createContactPage.fill_input_last_name(driver, os, LAST_NAME, wait)
    createContactPage.fill_input_company(driver, os, COMPANY, wait)
    createContactPage.fill_input_phone(driver, os, PHONE, wait)
    createContactPage.click_on_button_save_contact(driver, os, wait)
    contactPage.verify_if_new_contact_exists(driver, os, FULL_NAME, wait)
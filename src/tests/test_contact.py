import allure

from faker import Faker
from src.pages.contacts_page import ContactsPage as contactsPage
from src.pages.create_contact_page import CreateContactPage as createContactPage
from src.pages.contact_page import ContactPage as contactPage
from src.tests.conftest import driver, os

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
def test_create_contact_successfully(driver, os):
    allure.dynamic.tag("Contact", os)
    contactsPage.verify_if_button_add_contact_is_visible(driver, os)
    contactsPage.click_on_button_add_contact(driver, os)
    createContactPage.fill_input_first_name(driver, os, FIRST_NAME)
    createContactPage.fill_input_last_name(driver, os, LAST_NAME)
    createContactPage.fill_input_company(driver, os, COMPANY)
    createContactPage.fill_input_phone(driver, os, PHONE)
    createContactPage.click_on_button_save_contact(driver, os)
    contactPage.verify_if_new_contact_exists(driver, os, FULL_NAME)
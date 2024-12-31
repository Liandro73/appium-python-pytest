import allure

from src.pages.contacts_page import ContactsPage as contactsPage
from src.tests.conftest import driver, os

@allure.suite("Contact")
@allure.title("Add Contact successfully")
@allure.description("This is a test about adding new Contacts in Android and iOS Applications")
def test_login_successfully(driver, os):
    allure.dynamic.tag("Contact", os)
    contactsPage.verify_if_is_contact_page(driver, os)
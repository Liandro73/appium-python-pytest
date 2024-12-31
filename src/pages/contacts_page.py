import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webelement import WebElement

from src.pages.helper.pages_helper import PageObjectHelper

class ContactsPage(PageObjectHelper):

    # Android Locators
    btn_add_contact_android = AppiumBy.ACCESSIBILITY_ID, "Create contact"

    # iOS Locators
    btn_add_contact_ios = AppiumBy.ACCESSIBILITY_ID, "Add"

    @classmethod
    @allure.step("Verify if is Contacts Page")
    def verify_if_is_contact_page(cls, driver, os):
        if os == 'ios':
            btn_add_contact: WebElement = driver.find_element(*cls.btn_add_contact_ios)
            cls.wait_until_element_is_visible(driver, btn_add_contact)
            btn_add_contact.click()
        else:
            btn_add_contact: WebElement = driver.find_element(*cls.btn_add_contact_android)
            cls.wait_until_element_is_visible(driver, btn_add_contact)
            btn_add_contact.click()

        allure.attach(
            driver.get_screenshot_as_png(),
            name="contacts-page",
            attachment_type=allure.attachment_type.PNG
        )
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webelement import WebElement

from src.pages.helper.pages_helper import PageObjectHelper

class ContactsPage(PageObjectHelper):

    # Android Locators
    btn_skip_backup_android = AppiumBy.ID, "android:id/button2"
    input_search_contact_android = AppiumBy.XPATH, "//android.widget.EditText[@text='Search contacts']"
    btn_add_contact_android = AppiumBy.ACCESSIBILITY_ID, "Create contact"
    toast_contact_deleted_android = AppiumBy.XPATH, "//android.widget.Toast[@text='1 contact deleted']"

    # iOS Locators
    input_search_contact_ios = AppiumBy.ACCESSIBILITY_ID, "Search"
    btn_add_contact_ios = AppiumBy.ACCESSIBILITY_ID, "Add"

    @classmethod
    @allure.step("Verify if button Backup is visible and click on it")
    def verify_if_button_backup_is_visible(cls, driver, os):
        if os == 'android':
            btn_skip_backup: WebElement = driver.find_element(*cls.btn_skip_backup_android)
            cls.wait_until_element_is_visible(driver, btn_skip_backup)

            allure.attach(
                driver.get_screenshot_as_png(),
                name="contacts-page",
                attachment_type=allure.attachment_type.PNG
            )

            cls.click_on_element(driver, btn_skip_backup)

    @classmethod
    @allure.step("Verify if search bar is visible")
    def verify_if_search_bar_is_visible(cls, driver, os):
        if os == 'ios':
            input_search_contact: WebElement = driver.find_element(*cls.input_search_contact_ios)
            cls.wait_until_element_is_visible(driver, input_search_contact)
        else:
            input_search_contact: WebElement = driver.find_element(*cls.input_search_contact_android)
            cls.wait_until_element_is_visible(driver, input_search_contact)

        allure.attach(
            driver.get_screenshot_as_png(),
            name="contacts-page",
            attachment_type=allure.attachment_type.PNG
        )

    @classmethod
    @allure.step("Click on search bar")
    def click_on_search_bar(cls, driver, os):
        if os == 'ios':
            input_search_contact: WebElement = driver.find_element(*cls.input_search_contact_ios)
            cls.click_on_element(driver, input_search_contact)
        else:
            input_search_contact: WebElement = driver.find_element(*cls.input_search_contact_android)
            cls.click_on_element(driver, input_search_contact)

    @classmethod
    @allure.step("Verify if button Add Contact is visible")
    def verify_if_button_add_contact_is_visible(cls, driver, os):
        if os == 'ios':
            btn_add_contact: WebElement = driver.find_element(*cls.btn_add_contact_ios)
            cls.wait_until_element_is_visible(driver, btn_add_contact)
        else:
            btn_add_contact: WebElement = driver.find_element(*cls.btn_add_contact_android)
            cls.wait_until_element_is_visible(driver, btn_add_contact)

        allure.attach(
            driver.get_screenshot_as_png(),
            name="contacts-page",
            attachment_type=allure.attachment_type.PNG
        )

    @classmethod
    @allure.step("Click on button Add Contact")
    def click_on_button_add_contact(cls, driver, os):
        if os == 'ios':
            btn_add_contact: WebElement = driver.find_element(*cls.btn_add_contact_ios)
            cls.click_on_element(driver, btn_add_contact)
        else:
            btn_add_contact: WebElement = driver.find_element(*cls.btn_add_contact_android)
            cls.click_on_element(driver, btn_add_contact)

    @classmethod
    @allure.step("Verify if the new Contact is on the list")
    def verify_if_new_contact_in_on_the_list(cls, driver, os, fullname: str):
        if os == 'ios':
            input_search_contact: WebElement = driver.find_element(*cls.input_search_contact_ios)
            cls.clear_and_type_in_element(driver, input_search_contact, fullname)
            cls.wait_until_element_is_visible(driver, driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeCell[@name='" + fullname + "']"))
        else:
            input_search_contact: WebElement = driver.find_element(*cls.input_search_contact_android)
            cls.clear_and_type_in_element(driver, input_search_contact, fullname)
            cls.wait_until_element_is_visible(driver, driver.find_element(AppiumBy.ACCESSIBILITY_ID, fullname))
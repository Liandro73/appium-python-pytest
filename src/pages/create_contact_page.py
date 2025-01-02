import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webelement import WebElement

from src.pages.helper.pages_helper import PageObjectHelper

class CreateContactPage(PageObjectHelper):

    # Android Locators
    input_first_name_android = AppiumBy.XPATH, "//android.widget.EditText[@text='First name']"
    input_last_name_android = AppiumBy.XPATH, "//android.widget.EditText[@text='Last name']"
    input_company_android = AppiumBy.XPATH, "//android.widget.EditText[@text='Company']"
    input_phone_android = AppiumBy.XPATH, "//android.widget.EditText[@text='Phone']"
    input_email_android = AppiumBy.XPATH, "//android.widget.EditText[@text='Email']"
    input_address_android = AppiumBy.XPATH, "//android.widget.AutoCompleteTextView[@text='Address']"
    #
    btn_phone_type_android = AppiumBy.ACCESSIBILITY_ID, "Mobile Phone"
    btn_email_type_android = AppiumBy.ACCESSIBILITY_ID, "Home Email"
    btn_address_type_android = AppiumBy.ACCESSIBILITY_ID, "Home Address"
    btn_more_fields_android = AppiumBy.XPATH, "//android.widget.TextView[@text='More fields']"
    btn_save_contact_android = AppiumBy.ID, "com.google.android.contacts:id/toolbar_button"

    # iOS Locators
    input_first_name_ios = AppiumBy.ACCESSIBILITY_ID, "First name"
    input_last_name_ios = AppiumBy.ACCESSIBILITY_ID, "Last name"
    input_company_ios = AppiumBy.ACCESSIBILITY_ID, "Company"
    input_phone_ios = AppiumBy.XPATH, "//XCUIElementTypeTextField[@value='Phone']"
    input_email_ios = AppiumBy.XPATH, "//XCUIElementTypeTextField[@value='Email']"
    input_address_ios = AppiumBy.XPATH, "(//XCUIElementTypeTextField[@name='Street'])[2]"
    input_city_ios = AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='City']"
    input_state_ios = AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='State']"
    input_postal_code_ios = AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='Postal Code']"

    btn_add_phone_ios = AppiumBy.XPATH, "//XCUIElementTypeCell[@name='add phone']"
    btn_phone_type_ios = AppiumBy.XPATH, "(//XCUIElementTypeImage[@name='Forward'])[1]"
    btn_add_email_ios = AppiumBy.XPATH, "//XCUIElementTypeCell[@name='add email']"
    btn_email_type_ios = AppiumBy.XPATH, "(//XCUIElementTypeImage[@name='Forward'])[2]"
    btn_add_address_ios = AppiumBy.XPATH, "//XCUIElementTypeCell[@name='add address']"
    btn_address_type_ios = AppiumBy.XPATH, "(//XCUIElementTypeImage[@name='Forward'])[5]"
    btn_save_contact_ios = AppiumBy.ACCESSIBILITY_ID, "Done"

    @classmethod
    @allure.step("Fill input first name")
    def fill_input_first_name(cls, driver, os, firstname: str):
        if os == 'ios':
            input_first_name: WebElement = driver.find_element(*cls.input_first_name_ios)
            cls.clear_and_type_in_element(driver, input_first_name, firstname)
        else:
            input_first_name: WebElement = driver.find_element(*cls.input_first_name_android)
            cls.clear_and_type_in_element(driver, input_first_name, firstname)

    @classmethod
    @allure.step("Fill input last name")
    def fill_input_last_name(cls, driver, os, firstname: str):
        if os == 'ios':
            input_last_name: WebElement = driver.find_element(*cls.input_last_name_ios)
            cls.clear_and_type_in_element(driver, input_last_name, firstname)
        else:
            input_last_name: WebElement = driver.find_element(*cls.input_last_name_android)
            cls.clear_and_type_in_element(driver, input_last_name, firstname)

    @classmethod
    @allure.step("Fill input company")
    def fill_input_company(cls, driver, os, company: str):
        if os == 'ios':
            input_company: WebElement = driver.find_element(*cls.input_company_ios)
            cls.clear_and_type_in_element(driver, input_company, company)
        else:
            input_company: WebElement = driver.find_element(*cls.input_company_android)
            cls.clear_and_type_in_element(driver, input_company, company)

    @classmethod
    @allure.step("Click on button add phone")
    def click_on_button_add_phone(cls, driver, os):
        if os == 'ios':
            input_company: WebElement = driver.find_element(*cls.btn_add_phone_ios)
            cls.click_on_element(driver, input_company)

    @classmethod
    @allure.step("Click on button add phone")
    def click_on_button_select_phone_type(cls, driver, os):
        if os == 'ios':
            btn_phone_type: WebElement = driver.find_element(*cls.btn_phone_type_ios)
            cls.click_on_element(driver, btn_phone_type)
        else:
            btn_phone_type: WebElement = driver.find_element(*cls.btn_phone_type_android)
            cls.click_on_element(driver, btn_phone_type)

    @classmethod
    @allure.step("Fill input phone")
    def fill_input_phone(cls, driver, os, phone: str):
        cls.click_on_button_add_phone(driver, os)
        if os == 'ios':
            input_phone: WebElement = driver.find_element(*cls.input_phone_ios)
            cls.clear_and_type_in_element(driver, input_phone, phone)
        else:
            input_phone: WebElement = driver.find_element(*cls.input_phone_android)
            cls.clear_and_type_in_element(driver, input_phone, phone)

    @classmethod
    @allure.step("Click on button save contact")
    def click_on_button_save_contact(cls, driver, os):
        if os == 'ios':
            btn_save_contact: WebElement = driver.find_element(*cls.btn_save_contact_ios)
            cls.click_on_element(driver, btn_save_contact)
        else:
            btn_save_contact: WebElement = driver.find_element(*cls.btn_save_contact_android)
            cls.click_on_element(driver, btn_save_contact)
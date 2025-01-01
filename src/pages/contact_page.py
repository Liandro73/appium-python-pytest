from time import sleep

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from src.pages.helper.pages_helper import PageObjectHelper

class ContactPage(PageObjectHelper):

    # Android Locators
    btn_back_contact_android = AppiumBy.ACCESSIBILITY_ID, 'Navigate up'
    btn_close_popup_android = AppiumBy.ACCESSIBILITY_ID, 'Close Popup Window'

    # iOS Locators

    @classmethod
    @allure.step("Click on button Back")
    def click_on_button_back_contact(cls, driver, os, wait):
        if os == 'android':
            btn_back_contact: WebElement = driver.find_element(*cls.btn_back_contact_android)
            cls.click_on_element(wait, btn_back_contact)

    @classmethod
    @allure.step("Verify if the new Contact exists")
    def verify_if_new_contact_exists(cls, driver, os, full_name: str, wait):
        sleep(3)
        if os == 'ios':
            cls.wait_until_element_is_visible(wait, driver.find_element(AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{full_name}"]'))
        else:
            try:
                btn_close_popup: WebElement = driver.find_element(*cls.btn_close_popup_android)
                cls.click_on_element(wait, btn_close_popup)
            except NoSuchElementException:
                print(f'element {cls.btn_close_popup_android} not showed')
            cls.wait_until_element_is_visible(wait, driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text="{full_name}"]'))
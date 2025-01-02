from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class PageObjectHelper:
    TIMEOUT = 30
    wait: WebDriverWait

    @classmethod
    def wait_until_element_is_visible(cls, driver, element):
        cls.wait = WebDriverWait(driver, cls.TIMEOUT)
        cls.wait.until(ec.visibility_of(element))

    @classmethod
    def clear_and_type_in_element(cls, driver, element, text):
        cls.wait_until_element_is_visible(driver, element)
        element.click()
        element.clear()
        element.send_keys(text)

    @classmethod
    def click_on_element(cls, driver, element):
        cls.wait_until_element_is_visible(driver, element)
        element.click()

    @classmethod
    def get_text_from_element_and_compare(cls, driver, element, text):
        cls.wait_until_element_is_visible(driver, element)
        text_element = element.text
        assert(text_element == element.text)
        print("")
        print("-----------------------------------------")
        print("Text obtained: " + text_element.upper())
        print("Text expected: " + text.upper())
        print("-----------------------------------------")
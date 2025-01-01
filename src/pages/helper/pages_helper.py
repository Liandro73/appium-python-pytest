from selenium.webdriver.support import expected_conditions as ec

class PageObjectHelper:

    @classmethod
    def wait_until_element_is_visible(cls, wait, element):
        wait.until(ec.visibility_of(element))

    @classmethod
    def clear_and_type_in_element(cls, wait, element, text):
        cls.wait_until_element_is_visible(wait, element)
        element.click()
        element.clear()
        element.send_keys(text)

    @classmethod
    def click_on_element(cls, wait, element):
        cls.wait_until_element_is_visible(wait, element)
        element.click()

    @classmethod
    def get_text_from_element_and_compare(cls, wait, element, text):
        cls.wait_until_element_is_visible(wait, element)
        text_element = element.text
        assert(text_element == element.text)
        print("")
        print("-----------------------------------------")
        print("Text obtained: " + text_element.upper())
        print("Text expected: " + text.upper())
        print("-----------------------------------------")
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_connection import AppiumConnection
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 30

def pytest_addoption(parser):
    parser.addoption(
        "--os", action="store", default="android", help="System to use in the mobile tests"
    )
    parser.addoption(
        "--host", action="store", default="127.0.0.1", help="Appium server host"
    )
    parser.addoption(
        "--port", action="store", default="4723", help="Appium server port"
    )

@pytest.fixture
def os(request):
    yield request.config.getoption("--os")

@pytest.fixture
def host(request):
    yield request.config.getoption("--host")

@pytest.fixture
def port(request):
    yield request.config.getoption("--port")

@pytest.fixture(scope='function')
def driver(request, os, host, port):

    client_config = ClientConfig(
        remote_server_addr=f'http://{host}:{port}',
        ignore_certificates=True
    )

    appium_executor = AppiumConnection(
        client_config=client_config
    )

    if os == "ios":
        options = XCUITestOptions()
        options.platformVersion = '18.2'
        options.udid = '9AFF57CC-41D0-416A-A1F6-ABEA6EFE55E8'
        options.app = 'com.apple.MobileAddressBook'
        driver = webdriver.Remote(command_executor=appium_executor, options=options)
    else:
        options = UiAutomator2Options()
        options.platformVersion = '15'
        options.udid = 'emulator-5554'
        options.app_package = 'com.google.android.contacts'
        options.app_activity = 'com.android.contacts.activities.PeopleActivity'
        driver = webdriver.Remote(command_executor=appium_executor, options=options)

    yield driver

    driver.quit()

@pytest.fixture(scope='function')
def wait(driver):
    wait = WebDriverWait(driver, TIMEOUT)

    yield wait
"""Module"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.firefox.service import Service as firefoxservice
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture()
def setup(request,get_arguments):
    """Method """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    # AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument("--log-level=1")
    browser = get_arguments
    if browser == 'chrome':
        driver = webdriver.Chrome(service= chromeservice(ChromeDriverManager().install()),options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=firefoxservice(GeckoDriverManager().install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get('http://127.0.0.1:61673')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    """Method"""
    parser.addoption("--browser",action="store",default="chrome")

@pytest.fixture(scope="session")
def get_arguments(request):
    """Method"""
    browser_ = request.config.getoption("--browser")
    return browser_


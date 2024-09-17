"""Module"""

from selenium.webdriver.common.by import By


MESSAGE = '//h1'

class GREETPAGE():
    """Class """

    def __init__(self,driver) -> None:
        self.driver = driver

    def get_greet_message(self):
        """Method """
        return self.driver.find_element(By.XPATH,MESSAGE).text

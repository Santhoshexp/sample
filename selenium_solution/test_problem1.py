"""Module to test greeting message"""

import pytest
from greet_page import GREETPAGE





@pytest.mark.usefixtures('setup')
class Testgreet:
    """Class"""

    def test_greeting_message(self):
        """Method"""
        greet_obj = GREETPAGE(self.driver)
        msg = greet_obj.get_greet_message()
        assert 'Hello from the Backend!' == msg

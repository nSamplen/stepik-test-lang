import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

pytest.result_str = ""

def test_there_is_add_to_card_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    time.sleep(10)

    button = browser.find_element_by_css_selector(".btn-add-to-basket")

    assert button, "There is no button" 





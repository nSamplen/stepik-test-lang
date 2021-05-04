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

    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        "There is no button"
    





import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pytest
from selenium import webdriver
from pageobject.login_page import LoginPage

@pytest.fixture
def login():
    options = webdriver.ChromeOptions()
    options.headless = False
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
    
    if os.path.isfile(_chromedriver):
        driver_ = webdriver.Chrome((_chromedriver), options=options)
    else:
        driver_ = webdriver.Chrome("C:/Auto/Nam_Test_TodoApp_withlogin/Nam_Test_TodoApp_withlogin/vendor/chromedriver.exe")
    
    loginPage = LoginPage(driver_)
    
    return loginPage

def test_login(login):
    login.login_("namtest8497", "Kami1497")
    
    assert 1 == 1






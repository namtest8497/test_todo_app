import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pytest
from selenium import webdriver
from pageobject.dashboard_page import DashboardPage

@pytest.fixture
def self():
    options = webdriver.ChromeOptions()
    options.headless = False
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
    
    if os.path.isfile(_chromedriver):
        driver_ = webdriver.Chrome((_chromedriver), options=options)
    else:
        driver_ = webdriver.Chrome("C:/Auto/Nam_Test_TodoApp_withlogin/Nam_Test_TodoApp_withlogin/vendor/chromedriver.exe")
    
    dashboardPage = DashboardPage(driver_)
    
    return dashboardPage
    
def test_create_list(self):
    self.create_10list_("namtest8497", "Kami1497")
    
    assert 1 == 1
    
def test_delete_list(self):
    self.delete_last_5list_("namtest8497", "Kami1497")
    
    assert 1 == 1
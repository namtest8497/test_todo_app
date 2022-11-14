from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pageobject.basepage import BasePage
import random, string
import time

class DashboardPage(BasePage):
    BUTTON_GITHUB = {"by": By.CSS_SELECTOR, "value":".btn-github"}
    INPUT_EMAIL = {"by": By.ID, "value": "login_field"}
    INPUT_PASSWORD = {"by": By.ID, "value":"password"}
    BUTTON_SIGNIN = {"by": By.CSS_SELECTOR, "value":".btn"}
    INPUT_LIST = {"by": By.XPATH, "value": "//input[@ng-model='home.list']"}
    BUTTON_ADD = {"by": By.CSS_SELECTOR, "value":".btn-success"}
    BUTTON_SIGNOUT = {"by": By.XPATH, "value":"//button[contains(.,'Sign out')]"}
    BUTTON_DELETE5 = {"by": By.CSS_SELECTOR, "value":".disney1:nth-child(5) .btn"} 
    
    def __init__(self, driver):
        self.driver = driver
        self._visit("https://todo-list-login.firebaseapp.com/#!/")
    
    def create_10list_(self, gmail, password):
        try:
            btn_github = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (self.BUTTON_GITHUB["by"], self.BUTTON_GITHUB["value"]))
            )
            
            if(btn_github.is_displayed()):
                self._click(self.BUTTON_GITHUB)
            else:
                print(" - Submit button is invisible")
                exit(1)

        except TimeoutException:
            print("Loading Submit button took too much time!")
        
        handles = self.driver.window_handles
        for i in handles:
            self.driver.switch_to.window(i)
        
        try:
            input_email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (self.INPUT_EMAIL["by"], self.INPUT_EMAIL["value"]))
            )
            
            if(input_email.is_displayed()):
                self._type(self.INPUT_EMAIL, gmail)
                self._type(self.INPUT_PASSWORD, password)
            else:
                print(" - Submit button is invisible")
                exit(1)
        
        except TimeoutException:
            print("Loading Submit button took too much time!")
        
        self._click(self.BUTTON_SIGNIN)

        window_before = self.driver.window_handles[0]
        self.driver.switch_to.window(window_before)

        valid_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #create list with 10 item
        for i in range(10):
            #create random string from valid_letters
            randomstring = ''.join((random.choice(valid_letters) for i in range(5)))
            
            try:
                input_list = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (self.INPUT_LIST["by"], self.INPUT_LIST["value"]))
                )
                
                if(input_list.is_displayed()):
                    self._type(self.INPUT_LIST, randomstring)
                    self._click(self.BUTTON_ADD)
                else:
                    print(" - Submit button is invisible")
                    exit(1)
            except TimeoutException:
                print("Loading Submit button took too much time!")

        #logout
        self._click(self.BUTTON_SIGNOUT)

        return 1
    
    def delete_last_5list_(self, gmail, password):
        try:
            btn_github = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (self.BUTTON_GITHUB["by"], self.BUTTON_GITHUB["value"]))
            )
            
            if(btn_github.is_displayed()):
                self._click(self.BUTTON_GITHUB)
            else:
                print(" - Submit button is invisible")
                exit(1)

        except TimeoutException:
            print("Loading Submit button took too much time!")
        
        handles = self.driver.window_handles
        for i in handles:
            self.driver.switch_to.window(i)
        
        try:
            input_email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (self.INPUT_EMAIL["by"], self.INPUT_EMAIL["value"]))
            )
            
            if(input_email.is_displayed()):
                self._type(self.INPUT_EMAIL, gmail)
                self._type(self.INPUT_PASSWORD, password)
            else:
                print(" - Add button is invisible")
                exit(1)
        
        except TimeoutException:
            print("Loading Add button took too much time!")
        
        self._click(self.BUTTON_SIGNIN)

        window_before = self.driver.window_handles[0]
        self.driver.switch_to.window(window_before)
        #delete from item 5 to 10
        for i in range(6):
            try:
                btn_delete = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (self.BUTTON_DELETE5["by"], self.BUTTON_DELETE5["value"]))
                )
                
                if(btn_delete.is_displayed()):
                    self._click(self.BUTTON_DELETE5)
                else:
                    print(" - Delete button is invisible")
                    exit(1)
            except TimeoutException:
                print("Loading Delete button took too much time!")

        #Logout
        self._click(self.BUTTON_SIGNOUT)

        return 1
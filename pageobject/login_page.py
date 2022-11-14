from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import smtplib
import time
import imaplib
import email
import string
import traceback
from pageobject.basepage import BasePage
# imap_url = 'imap.gmail.com'
# imap_user = 'namtest8497@gmail.com'
# imap_pass = 'zidtaflxmtepjyxe'


def get_text(msg):
    if msg.is_multipart():
        return get_text(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

class LoginPage(BasePage):
    BUTTON_GITHUB = {"by": By.CSS_SELECTOR, "value":".btn-github"}
    INPUT_EMAIL = {"by": By.ID, "value": "login_field"}
    INPUT_PASSWORD = {"by": By.ID, "value":"password"}
    BUTTON_SIGNIN = {"by": By.CSS_SELECTOR, "value":".btn"}
    BUTTON_SIGNOUT = {"by": By.CSS_SELECTOR, "value":".btn-default"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("https://todo-list-login.firebaseapp.com/#!/")

    def login_(self, gmail, password):
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
        
        # email OTP verify
        # # connect to host using SSL
        # mail = imaplib.IMAP4_SSL(imap_url)
        # subject = '[GitHub] Please verify your device   '
        # # login to server
        # mail.login(imap_user, imap_pass)
        # mail.select('Inbox')
        # result, data = mail.search(None,'(UNSEEN SUBJECT "%s")' % subject)
    
        # for num in data[0].split():
        #     result, data = mail.fetch(num,'(RFC822)')
        #     if result == 'OK':
        #         raw = email.message_from_bytes(data[0][1])
        #         string1 = str(get_text(raw))
        #         cut_string = string1[230:236]
        #         print(" OTP to verify code is: ",cut_string)
        # try:
        #     verify_code_input = WebDriverWait(self.driver, 10).until(
        #         EC.visibility_of_element_located(
        #             (By.ID, "otp"))
        #     )
        #     if(verify_code_input.is_displayed()):
        #         verify_code_input.send_keys(cut_string)
        #     else:
        #         print(" - Input Verify Code is invisible")
        # except TimeoutException:
        #     print("Loading Input Verify Code took too much time!")

        # btn_submit = WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//*[@id='login']/div[3]/div[2]/div[2]/form/button"))
        # )
        # btn_submit.click()
        
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.window(window_before)
        
        try:
            btn_signout = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (self.BUTTON_SIGNOUT["by"], self.BUTTON_SIGNOUT["value"]))
            )
            
            if(btn_signout.is_displayed()):
                self._click(self.BUTTON_SIGNOUT)
            else:
                print(" - Signout button is invisible")
                exit(1)
        
        except TimeoutException:
            print("Loading Signout button took too much time!")

        return 1

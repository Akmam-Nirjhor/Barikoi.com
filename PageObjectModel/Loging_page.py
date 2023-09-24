from selenium.webdriver.common.by import By
class Loging_page:
    def __init__(self,driver):
        self.driver = driver

    User_name_or_Email_Address = (By.XPATH,"//input[@id='user_login'] ")
    Password = (By.NAME,'pwd')
    Loging_Button = (By.XPATH," //input[@type='submit'] ")


    def get_User_name_or_Email_Address(self):
        return self.driver.find_element(*Loging_page.User_name_or_Email_Address)

    def get_Password(self):
        return self.driver.find_element(*Loging_page.Password)

    def get_Logging_Button(self):
        return self.driver.find_element(*Loging_page.Loging_Button)







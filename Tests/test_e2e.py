import time
from selenium.webdriver.common.by import By
from Utilites.BaseClass import BassClass
from PageObjectModel.Loging_page import Loging_page
from PageObjectModel.Hone_page import Homepage

class TestOne(BassClass):

    def test_e2e(self):
        logingpage = Loging_page(self.driver)
        homepage = Homepage(self.driver)



        logingpage.get_User_name_or_Email_Address().send_keys("akmamnirjhor")
        logingpage.get_Password().send_keys("2030514.js@1ABC")
        time.sleep(2)
        logingpage.get_Logging_Button().click()
        homepage.get_WP_Dark_mode().click()
        homepage.get_Enable_Backend_Darkmode_button().click()
        time.sleep(2)
        homepage.get_general_setting().click()
        time.sleep(2)
        homepage.get_save_button().click()
        time.sleep(2)
        homepage.get_darkmode_button().click()
        time.sleep(2)
        homepage.get_white_mode_Button().click()
        time.sleep(1)
        homepage.get_WP_Dark_mode().click()
        time.sleep(1)
        homepage.get_switch_button().click()
        time.sleep(2)
        homepage.get_floating_switch().click()
        homepage.get_Switch_size().click()
        homepage.switch_Custom_scale().click()
        homepage.get_float_switch_button().click()
        time.sleep(1)
        homepage.get_save_Button_1().click()
        time.sleep(2)
        homepage.get_accessibility().click()
        time.sleep(1)
        homepage.get_Keyboard_Shortcut().click()
        homepage.get_save_button3().click()
        homepage.get_animation().click()
        time.sleep(2)
        homepage.get_darkmode_Toggle_Animation().click()
        homepage.get_Annimation_Effect().click()
        time.sleep(2)
        homepage.get_flip_buton().click()
        time.sleep(1)
        homepage.get_SaveandSettings().click()
        time.sleep(2)
        homepage.get_darkmode_button().click()

        print("Darkmode is working Successfull")













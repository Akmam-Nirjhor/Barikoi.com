import time
from selenium.webdriver.common.by import By
from Utilites.BaseClass import BassClass
from PageObjectModel.Search_button_page import Loging_page


class TestOne(BassClass):

    def test_e2e(self):
        logingpage = Loging_page(self.driver)
        time.sleep(2)

        logingpage.get_name().send_keys("Independent University Bangladesh ")
        time.sleep(2)
        logingpage.get_iub().click()
        time.sleep(4)
        logingpage.get_cross().click()
        logingpage.get_name().send_keys("Barikoi")
        time.sleep(1)
        logingpage.get_barikoi().click()
        time.sleep(3)
        logingpage.get_cross().click()
        logingpage.get_name().send_keys("Jamuna Future Park")
        time.sleep(2)
        logingpage.get_jamuna().click()
        time.sleep(2)
        logingpage.get_cross().click()
        logingpage.get_name().send_keys("Banani")
        time.sleep(2)
        logingpage.get_banani().click()
        time.sleep(3)
        logingpage.get_cross().click()
        logingpage.get_name().send_keys("Badda")
        time.sleep(3)
        logingpage.get_badda().click()
        time.sleep(2)
        logingpage.get_cross().click()
        time.sleep(2)
        logingpage.get_name().send_keys("Dhanmondi")
        time.sleep(2)
        logingpage.get_dhanmondi().click()
        time.sleep(2)
        logingpage.get_cross().click()
        time.sleep(2)
        logingpage.get_name().send_keys("Lalmatiya")
        time.sleep(3)
        logingpage.get_Lalmatiya().click()
        time.sleep(2)
        logingpage.get_cross().click()
        time.sleep(2)
        logingpage.get_name().send_keys("Khilgaon ")
        time.sleep(2)
        logingpage.get_khilgoan().click()
        time.sleep(2)
        logingpage.get_cross().click()
        time.sleep(2)
        logingpage.get_name().send_keys("Motijheel")
        time.sleep(3)
        logingpage.get_motijheel().click()
        time.sleep(2)
        logingpage.get_cross().click()
        time.sleep(2)
        logingpage.get_name().send_keys("Gulshan")
        time.sleep(2)
        logingpage.get_Gulshna().click()
        time.sleep(2)
        logingpage.get_cross().click()
        time.sleep(3)

        print('Execute all Location Successfully')



        




















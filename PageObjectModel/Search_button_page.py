from selenium.webdriver.common.by import By
class Loging_page:
    def __init__(self,driver):
        self.driver = driver

    search_button = (By.CSS_SELECTOR,' .ant-select-selection-search-input')
    IUB = (By.XPATH,' /html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div/div')
    cross_button = (By.CSS_SELECTOR,'.ant-btn.css-18iikkb.ant-btn-default.ant-btn-lg.autoCompleteSearchbarButton ')
    barikoi = (By.XPATH,'//*[@id="3354"]/div/div/b[2] ')
    jamuna = (By.XPATH,' /html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/b[1] ')
    Banani = (By.XPATH,' /html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/div  ')
    Badda = (By.XPATH,'//*[@id="633"]/div/div ')
    Dhanmondi = (By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/div   ')
    Lalmatiya = (By.XPATH,'//*[@id="992371"]/div/div ')
    Khilgaon = (By.XPATH, '//*[@id="634080"]/div/div ')
    motijheel = (By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/div')
    Gulshnan2 = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/b[1]')



    def get_name(self):
        return self.driver.find_element(*Loging_page.search_button)

    def get_iub(self):
        return self.driver.find_element(*Loging_page.IUB)

    def get_cross(self):
        return self.driver.find_element(*Loging_page.cross_button)

    def get_barikoi(self):
        return self.driver.find_element(*Loging_page.barikoi)

    def get_jamuna(self):
        return self.driver.find_element(*Loging_page.jamuna)

    def get_banani(self):
        return self.driver.find_element(*Loging_page.Banani)

    def get_badda(self):
        return self.driver.find_element(*Loging_page.Badda)

    def get_dhanmondi(self):
        return self.driver.find_element(*Loging_page.Dhanmondi)

    def get_Lalmatiya(self):
        return self.driver.find_element(*Loging_page.Lalmatiya)

    def get_khilgoan(self):
        return self.driver.find_element(*Loging_page.Khilgaon)

    def get_motijheel(self):
        return self.driver.find_element(*Loging_page.motijheel)

    def get_Gulshna(self):
        return self.driver.find_element(*Loging_page.Gulshnan2)


from selenium.webdriver.common.by import By
class Homepage:
    def __init__(self,driver):
        self.driver = driver


    WP_Dark_Mode =(By.XPATH,'//*[@id="toplevel_page_wp-dark-mode-settings"]/a/div[3] ')
    General_Settinga = (By.XPATH,'//*[@id="wp_dark_mode_general-tab"]/span ')
    Enable_Backend_Darkmood = (By.XPATH,'//*[@id="wp_dark_mode_general"]/form/table/tbody/tr[2]/td/fieldset/label/div/div')
    save_button = (By.XPATH,' //*[@id="save_settings"]')
    Dark_moode_Button = (By.XPATH,' //*[@id="wp-admin-bar-wp-dark-mode"]/a/div/label/div[2]/p[2]')
    White_mode_Button = (By.XPATH,'//*[@id="wp-admin-bar-wp-dark-mode"]/a/div/label/div[2]/p[1]')
    Switch_setting = (By.XPATH,'//*[@id="wp_dark_mode_switch-tab"]/span')
    floating_switch_style = (By.XPATH,'//*[@id="wp_dark_mode_switch"]/form/table/tbody/tr[2]/td/fieldset/label[3]/img')
    Switch_size = (By.XPATH,"//*[@id='wp_dark_mode_switch']/form/table/tbody/tr[3]/td/div/span[6] ")
    Switch_customer_scale = (By.XPATH,'//*[@id="wp_dark_mode_switch[switcher_position]"]/option[1]  ')
    floating_Switch_position = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/div[4]/form/div/p ")
    save_Button_1= (By.XPATH,' /html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/div[4]/form/div/p/input')
    Accessbility_settings = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/ul/li[8]/a/span ')
    Keyboard_Shortcut = (By.XPATH,'//*[@id="wp_dark_mode_accessibility"]/form/table/tbody/tr[5]/td/fieldset/label/div/div ')
    Save_Button3 = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/div[8]/form/div/p/input ')
    Animation_button = (By.XPATH,'//*[@id="wp_dark_mode_animation-tab"]/span  ')
    Darkmode_Toggle_Animation =(By.XPATH,'//*[@id="wp_dark_mode_animation"]/form/table/tbody/tr[1]/td/fieldset/label/div/div  ')
    Animation_Effect = (By.XPATH,' //*[@id="wp_dark_mode_animation[animation]"]')
    Save_Setting_4 = (By.XPATH,' //*[@id="wp_dark_mode_animation[animation]"]/option[3] ')
    flip_Button = (By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/div[13]/form/div/p/input ')



    def get_WP_Dark_mode(self):
        return self.driver.find_element(*Homepage.WP_Dark_Mode)

    def get_general_setting(self):
        return self.driver.find_element(*Homepage.General_Settinga)

    def get_Enable_Backend_Darkmode_button(self):
        return self.driver.find_element(*Homepage.Enable_Backend_Darkmood)

    def get_save_button(self):
        return self.driver.find_element(*Homepage.save_button)

    def get_darkmode_button(self):
        return self.driver.find_element(*Homepage.Dark_moode_Button)

    def get_white_mode_Button(self):
        return self.driver.find_element(*Homepage.White_mode_Button)

    def get_switch_button(self):
        return self.driver.find_element(*Homepage.Switch_setting)

    def get_floating_switch(self):
        return self.driver.find_element(*Homepage.floating_switch_style)

    def get_Switch_size(self):
        return self.driver.find_element(*Homepage.Switch_size)

    def switch_Custom_scale(self):
        return self.driver.find_element(*Homepage.floating_Switch_position)

    def get_float_switch_button(self):
        return self.driver.find_element(*Homepage.floating_Switch_position)

    def get_save_Button_1(self):
        return self.driver.find_element(*Homepage.save_Button_1)

    def get_accessibility(self):
        return self.driver.find_element(*Homepage.Accessbility_settings)

    def get_Keyboard_Shortcut(self):
        return self.driver.find_element(*Homepage.Keyboard_Shortcut)

    def get_save_button3(self):
        return self.driver.find_element(*Homepage.Save_Button3)

    def get_animation(self):
        return self.driver.find_element(*Homepage.Animation_button)

    def get_darkmode_Toggle_Animation(self):
        return self.driver.find_element(*Homepage.Darkmode_Toggle_Animation)

    def get_Annimation_Effect(self):
        return self.driver.find_element(*Homepage.Animation_Effect)

    def get_flip_buton(self):
        return self.driver.find_element(*Homepage.flip_Button)

    def get_SaveandSettings(self):
        return self.driver.find_element(*Homepage.Save_Setting_4)


import allure
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction():
    def __init__(self,driver):
        self.driver =driver

    def base_find(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x :x.find_element(*loc))
    def base_click(self,loc):
        self.base_find(loc).click()
    def base_input(self,loc,value):
        self.base_find(loc).send_keys(value)
    def base_clear(self,loc):
        self.base_find(loc).clear()
    #返回
    @allure.step(title="点击返回")
    def base_back(self):
        self.driver.press_keycode(4)
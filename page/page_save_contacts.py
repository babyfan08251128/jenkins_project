import allure
import pytest

from base.base_action import BaseAction
import page


class PageSaveContacts(BaseAction):
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title ="输入联系人姓名")
    def input_name(self,name):
        allure.attach("输入",name)
        self.base_input(page.name_input,name)
    @allure.step(title = "输入电话号码")
    def input_num(self,num):

        allure.attach(num,"输入")
        self.base_input(page.num_input,num)
        #allure.attach("截图",self.driver.get_screenshot_as_png(),allure.attachment_type.PNG)

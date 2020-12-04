from time import sleep

import pytest

from base.get_dirver import get_driver
from base.read_yaml import read_yaml
from page.page import Page


class TestContacts:
    pass
    def setup(self):

        self.driver = get_driver()
        self.page = Page(self.driver)
    def teardown(self):
        sleep(2)
        self.driver.quit()


    @pytest.mark.parametrize("contacts",read_yaml("contacts_data.yaml","test_contacts"))
    def test_contacts(self,contacts):
        name = contacts["name"]
        num = contacts["num"]
        #print(number)
        #点击新建联系人
        self.page.page_new_contacts.click_new_contacts()
        #输入姓名
        self.page.page_save_contacts.input_name(name)
        #输入电话号
        self.page.page_save_contacts.input_num(num)
        #点击返回
        self.page.page_save_contacts.base_back()
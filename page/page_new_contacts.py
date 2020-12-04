import allure

from base.base_action import BaseAction
import page


class PageNewContacts(BaseAction):
    @allure.step(title="点击新建联系人")
    def click_new_contacts(self):

        self.base_click(page.new_contacts)

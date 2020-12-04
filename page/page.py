from page.page_new_contacts import PageNewContacts
from page.page_save_contacts import PageSaveContacts


class Page:
    def __init__(self,driver):
        self.driver = driver
    @property
    def page_new_contacts(self):
        return PageNewContacts(self.driver)
    @property
    def page_save_contacts(self):
        return PageSaveContacts(self.driver)

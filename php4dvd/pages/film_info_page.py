from php4dvd.pages.page import Page
from selenium.webdriver.common.by import By


class FilmInfoPage(Page):

    @property
    def remove_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Remove\"]")

    def edit_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Edit\"]")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "img[alt=\"Seen\"]"))

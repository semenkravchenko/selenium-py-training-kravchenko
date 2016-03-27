from php4dvd.pages.page import Page
from selenium.webdriver.common.by import By


class ImdbSearchResultPage(Page):

    @property
    def is_this_page(self):
        return self.is_element_visible((By.ID, "imdbsearchform"))

    @property
    def home_link(self):
        # return self.driver.find_element((By.LINK_TEXT, "Home"))
        return self.driver.find_element_by_link_text("Home")
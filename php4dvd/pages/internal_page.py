from php4dvd.pages.page import Page
from selenium.webdriver.common.by import By


class InternalPage(Page):

    @property
    def logout_button(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?logout']")

    @property
    def user_profile_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=profile']")

    @property
    def user_management_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=users']")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "nav"))

    @property
    def movies_searcher(self):
        return self.driver.find_elements_by_class_name("title")

    @property
    def add_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Add movie\"]")

    @property
    def home_link(self):
        # return self.driver.find_element((By.LINK_TEXT, "Home"))
        return self.driver.find_element_by_link_text("Home")

    @property
    def search_field(self):
        return self.driver.find_element_by_css_selector("input[type=\"text\"]")

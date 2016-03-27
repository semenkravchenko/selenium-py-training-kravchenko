from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By
from selenium import webdriver

class Page(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def is_element_visible(self, locator):
        try:
            self.wait.until(visibility_of_element_located(locator))
            return True
        except WebDriverException:
            return False

    def accept_to_the_next_alert(self):
        self.driver.switch_to.alert.accept()

    # def click_at_the_element(self, locator):
    #     self.driver.find_element(locator).click()

    def click_at_the_link_text_element(self, input_string):
        self.driver.find_element_by_link_text(input_string).click()

    def click_at_the_class_name_element(self, input_class):
        self.driver.find_element_by_class_name(input_class).click()

    def home_return(self):
        self.home_link.click()
        self.is_element_visible((By.CLASS_NAME, "title"))

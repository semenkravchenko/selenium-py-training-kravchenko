# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Removing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_removing_film_description(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")

        #login
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        driver.find_element_by_class_name("movie_box").click()
        driver.find_element_by_css_selector("img[alt=\"Edit\"]").click()

        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("rating").clear()
        driver.find_element_by_id("formats").clear()
        driver.find_element_by_id("text_languages_0").clear()

        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_name("name").send_keys("Title")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_name("year").send_keys("not a number")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("-1")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("0")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys("-10")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys("13")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_name("rating").clear()
        driver.find_element_by_name("rating").send_keys("-1")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("formats").clear()
        driver.find_element_by_id("formats").send_keys("VHS")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_link_text("Home").click()

    def test_film_removing(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")

        #login
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        driver.find_element_by_class_name("movie_box").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        driver.switch_to.alert.accept()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

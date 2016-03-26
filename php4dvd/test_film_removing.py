# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
import unittest, time, re

class Removing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_film_removing(self):

        class SmthWentWrongException(Exception):pass

        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")

        wait = WebDriverWait(self.driver, 3)

        #login
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        films_before_remove = driver.find_elements_by_class_name("title")

        driver.find_element_by_class_name("movie_box").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        driver.switch_to.alert.accept()

        wait.until(visibility_of_element_located((By.CLASS_NAME, "movie_box")))

        films_after_remove = driver.find_elements_by_class_name("title")

        if len(films_before_remove) == len(films_after_remove):
            raise SmthWentWrongException("films_before_remove list == films_after_remove list")

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

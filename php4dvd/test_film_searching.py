# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
import unittest, time, re

class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_existed_film_local_searching(self):

        class NotExistedFilmException(Exception): pass

        search_target = u"Криминальное чтиво"
        wait = WebDriverWait(self.driver, 3)

        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.implicitly_wait(3)

        #login
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        random_film = driver.find_element_by_class_name("title")

        searchbox = driver.find_element_by_class_name("inputDefault")
        searchbox.clear()
        searchbox.send_keys(search_target)
        searchbox.send_keys(Keys.ENTER)

        wait.until(invisibility_of_element_located((By.NAME, random_film)))

        time.sleep(1)

        films_after_search = driver.find_elements_by_class_name("title")

        if len(films_after_search) == 0:
            raise NotExistedFilmException("Film was not found")

        for film in films_after_search:

            if film.get_attribute("textContent") == search_target:
                print "We have found film with title: ", film.get_attribute("textContent")
                break

        driver.find_element_by_link_text("Home").click()

    def test_not_existed_film_local_searching(self):

        class NotExistedFilmException(Exception): pass

        search_target = u"Красная шапочка"
        wait = WebDriverWait(self.driver, 3)

        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.implicitly_wait(3)

        #login
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        random_film = driver.find_element_by_class_name("title")

        searchbox = driver.find_element_by_class_name("inputDefault")
        searchbox.clear()
        searchbox.send_keys(search_target)
        searchbox.send_keys(Keys.ENTER)

        wait.until(invisibility_of_element_located((By.NAME, random_film)))

        time.sleep(1)

        films_after_search = driver.find_elements_by_class_name("title")

        if len(films_after_search) > 0:
            for film in films_after_search:

                if film.get_attribute("textContent") == search_target:
                    print "We have found film with title: ", film.get_attribute("textContent")
                    raise NotExistedFilmException("We have found not existed film")

        driver.find_element_by_link_text("Home").click()

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

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Adding(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        self.verificationErrors = []
        self.accept_next_alert = True

    def EXCLUDED_test_film_adding_imdb_search(self):

        search_target_string = u"Криминальное чтиво"

        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")

        #login
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        #film adding
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_id("imdbsearch").clear()
        driver.find_element_by_id("imdbsearch").send_keys(search_target_string)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

        time.sleep(1)

        driver.find_element_by_link_text(search_target_string).click()
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_link_text("Home").click()

        time.sleep(1)

    def test_film_adding_full_data(self):

        class BadRequiredFieldException(Exception):pass

        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.implicitly_wait(3)

        #login
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        #film adding
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()

        imbdid = driver.find_element_by_name("imdbid")
        imbdid.clear()
        imbdid.send_keys("666")
        imbdid.send_keys(Keys.TAB)

        if str(imbdid.get_attribute("class")) != "digits":
            raise BadRequiredFieldException("Required field \"imbdid\" was filled bad")

        name = driver.find_element_by_name("name")
        name.clear()
        name.send_keys("Test Film Full Data")

        aka = driver.find_element_by_name("aka")
        aka.clear()
        aka.send_keys("Scary Test Film Full Data")

        year = driver.find_element_by_name("year")
        year.clear()
        year.send_keys("1937")
        year.send_keys(Keys.TAB)

        if str(year.get_attribute("class")) != "required digits":
            raise BadRequiredFieldException("Required field \"year\" was filled bad")

        duration = driver.find_element_by_name("duration")
        duration.clear()
        duration.send_keys("13")
        duration.send_keys(Keys.TAB)

        if str(duration.get_attribute("class")) != "digits":
            raise BadRequiredFieldException("Required field \"duration\" was filled bad")

        rating = driver.find_element_by_name("rating")
        rating.clear()
        rating.send_keys("777")
        rating.send_keys(Keys.TAB)

        if str(rating.get_attribute("class")) != "number":
            raise BadRequiredFieldException("Required field \"rating\" was filled bad")

        format = driver.find_element_by_name("format")
        format.clear()
        format.send_keys("VHS")
        format.send_keys(Keys.TAB)

        if str(format.get_attribute("class")) != "required ui-autocomplete-input":
            raise BadRequiredFieldException("Required field \"format\" was filled bad")

        trailer = driver.find_element_by_name("trailer")
        trailer.clear()
        trailer.send_keys("http://www.ru")
        trailer.send_keys(Keys.TAB)

        if str(trailer.get_attribute("class")) != "url":
            raise BadRequiredFieldException("Required field \"trailer\" was filled bad")

        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("Personal notes")
        driver.find_element_by_name("taglines").clear()
        driver.find_element_by_name("taglines").send_keys("Taglines")
        driver.find_element_by_name("plotoutline").clear()
        driver.find_element_by_name("plotoutline").send_keys("Plot outline")
        driver.find_element_by_name("plots").clear()
        driver.find_element_by_name("plots").send_keys("Plots")
        driver.find_element_by_id("text_languages_0").clear()
        driver.find_element_by_id("text_languages_0").send_keys("Russian")
        driver.find_element_by_name("subtitles").clear()
        driver.find_element_by_name("subtitles").send_keys("Subtitles")
        driver.find_element_by_name("audio").clear()
        driver.find_element_by_name("audio").send_keys("Audio")
        driver.find_element_by_name("video").clear()
        driver.find_element_by_name("video").send_keys("Video")
        driver.find_element_by_name("country").clear()
        driver.find_element_by_name("country").send_keys("Country")
        driver.find_element_by_name("genres").clear()
        driver.find_element_by_name("genres").send_keys("Genres")
        driver.find_element_by_name("director").clear()
        driver.find_element_by_name("director").send_keys("Director")
        driver.find_element_by_name("writer").clear()
        driver.find_element_by_name("writer").send_keys("Writer")
        driver.find_element_by_name("producer").clear()
        driver.find_element_by_name("producer").send_keys("Producer")
        driver.find_element_by_name("music").clear()
        driver.find_element_by_name("music").send_keys("Music")
        driver.find_element_by_name("cast").clear()
        driver.find_element_by_name("cast").send_keys("Cast")

        # driver.find_element_by_name("imdbid").clear()
        # film_id = driver.find_element_by_name("imdbid")
        # film_id.send_keys("aaa")
        # film_id.send_keys(Keys.TAB)

        # color = film_id.value_of_css_property("background-color")
        # print "Background color is: ", color
        #
        # color = film_id.value_of_css_property("border-color")
        # print "Border color is: ", color
        #
        # color = film_id.value_of_css_property("font-color")
        # print "Font color is: ", color
        #
        # all_input_elements = driver.find_elements_by_css_selector("input[type=\"text\"]")
        #
        # if all_input_elements > 0:
        #     for element in all_input_elements:
        #         #color = element.get_css_value("background-color")
        #         #color = element.get_attribute("background-color")
        #         color = element.value_of_css_property("background-color")
        #         #if color == None: print "Color is None. It is OK"
        #         #print color
        # else:
        #     print "We have not found input elements on page"
        #     self.fail

        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_link_text("Home").click()

        time.sleep(1)

    def EXCLUDED_test_film_adding_corrupted_data(self):

        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")

        #login
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()


        #trying to add film with corrupted data
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("imdbid").send_keys("not a number")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("imdbid").send_keys("777")
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("Test Film Currupted Data")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_name("aka").clear()
        driver.find_element_by_name("aka").send_keys("Scary Test Film Corrupted Data")
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("not a number")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_name("year").clear()
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("-1")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("999999999999999999999999999999999999")
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys("not a number")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys("13")
        driver.find_element_by_id("formats").clear()
        driver.find_element_by_id("formats").send_keys("")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("formats").clear()
        driver.find_element_by_id("formats").send_keys("VHS")
        driver.find_element_by_id("loaned_yes").click()
        driver.find_element_by_name("loandate").clear()
        driver.find_element_by_name("loandate").send_keys("")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
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

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

    def sender(self, element, keys):
        element.clear()
        element.send_keys(keys)
        element.send_keys(Keys.TAB)

    def test_film_adding_imbdid_field(self):

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

        #case 1
        self.sender(imbdid, "666")

        if str(imbdid.get_attribute("class")) != "digits":
            raise BadRequiredFieldException("Required field \"imbdid\" was filled bad")

        #case 2
        self.sender(imbdid, "-1")

        if str(imbdid.get_attribute("class")) == "digits":
            raise BadRequiredFieldException("Required field \"imbdid\" was filled bad")

        #case 3
        self.sender(imbdid, "not a number")

        if str(imbdid.get_attribute("class")) == "digits":
            raise BadRequiredFieldException("Required field \"imbdid\" was filled bad")

        #case 4
        self.sender(imbdid, "")

        if str(imbdid.get_attribute("class")) != "digits":
            raise BadRequiredFieldException("Required field \"imbdid\" was filled bad")

    def test_film_adding_year_field(self):

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

        year = driver.find_element_by_name("year")

        #case 1
        self.sender(year, "666")

        if str(year.get_attribute("class")) != "required digits":
            raise BadRequiredFieldException("Required field \"year\" was filled bad")

        #case 2
        self.sender(year, "-1")

        if str(year.get_attribute("class")) == "required digits":
            raise BadRequiredFieldException("Required field \"year\" was filled bad")

        #case 3
        self.sender(year, "not a number")

        if str(year.get_attribute("class")) == "required digits":
            raise BadRequiredFieldException("Required field \"year\" was filled bad")

        #case 4
        self.sender(year, "")

        if str(year.get_attribute("class")) != "required digits error":
            raise BadRequiredFieldException("Required field \"year\" was filled bad")

    def test_film_adding_duration_field(self):

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

        duration = driver.find_element_by_name("duration")

        #case 1
        self.sender(duration, "666")

        if str(duration.get_attribute("class")) != "digits":
            raise BadRequiredFieldException("Required field \"duration\" was filled bad")

        #case 2
        self.sender(duration, "-1")

        if str(duration.get_attribute("class")) == "digits":
            raise BadRequiredFieldException("Required field \"duration\" was filled bad")

        #case 3
        self.sender(duration, "not a number")

        if str(duration.get_attribute("class")) == "digits":
            raise BadRequiredFieldException("Required field \"duration\" was filled bad")

        #case 4
        self.sender(duration, "")

        if str(duration.get_attribute("class")) != "digits":
            raise BadRequiredFieldException("Required field \"duration\" was filled bad")

    def test_film_adding_rating_field(self):

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

        rating = driver.find_element_by_name("rating")

        #case 1
        self.sender(rating, "666")

        if str(rating.get_attribute("class")) != "number":
            raise BadRequiredFieldException("Required field \"rating\" was filled bad")

        #case 2
        self.sender(rating, "-1")

        if str(rating.get_attribute("class")) != "number":
            raise BadRequiredFieldException("Required field \"rating\" was filled bad")

        #case 3
        self.sender(rating, "not a number")

        if str(rating.get_attribute("class")) == "number":
            raise BadRequiredFieldException("Required field \"rating\" was filled bad")

        #case 4
        self.sender(rating, "")

        if str(rating.get_attribute("class")) != "number":
            raise BadRequiredFieldException("Required field \"rating\" was filled bad")

    def test_film_adding_trailer_field(self):

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

        trailer = driver.find_element_by_name("trailer")

        #case 1
        self.sender(trailer, "666")

        if str(trailer.get_attribute("class")) == "url":
            raise BadRequiredFieldException("Required field \"trailer\" was filled bad")

        #case 2
        self.sender(trailer, "-1")

        if str(trailer.get_attribute("class")) == "url":
            raise BadRequiredFieldException("Required field \"trailer\" was filled bad")

        #case 3
        self.sender(trailer, "some text")

        if str(trailer.get_attribute("class")) == "url":
            raise BadRequiredFieldException("Required field \"trailer\" was filled bad")

        #case 4
        self.sender(trailer, "")

        if str(trailer.get_attribute("class")) != "url":
            raise BadRequiredFieldException("Required field \"trailer\" was filled bad")

        #case 5
        self.sender(trailer, "http://www.ru")

        if str(trailer.get_attribute("class")) != "url":
            raise BadRequiredFieldException("Required field \"trailer\" was filled bad")

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

        self.sender(imbdid, "666")

        if str(imbdid.get_attribute("class")) != "digits":
            raise BadRequiredFieldException("Required field \"imbdid\" was filled bad")

        name = driver.find_element_by_name("name")

        self.sender(name, "Test Film Full Data")

        aka = driver.find_element_by_name("aka")

        self.sender(aka, "Scary Test Film Full Data")

        year = driver.find_element_by_name("year")

        self.sender(year, "1937")

        if str(year.get_attribute("class")) != "required digits":
            raise BadRequiredFieldException("Required field \"year\" was filled bad")

        duration = driver.find_element_by_name("duration")

        self.sender(duration, "13")

        if str(duration.get_attribute("class")) != "digits":
            raise BadRequiredFieldException("Required field \"duration\" was filled bad")

        rating = driver.find_element_by_name("rating")

        self.sender(rating, "777")

        if str(rating.get_attribute("class")) != "number":
            raise BadRequiredFieldException("Required field \"rating\" was filled bad")

        format = driver.find_element_by_name("format")

        self.sender(format, "VHS")

        if str(format.get_attribute("class")) != "required ui-autocomplete-input":
            raise BadRequiredFieldException("Required field \"format\" was filled bad")

        trailer = driver.find_element_by_name("trailer")

        self.sender(trailer, "http://www.ru")

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

        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_link_text("Home").click()

        time.sleep(1)

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

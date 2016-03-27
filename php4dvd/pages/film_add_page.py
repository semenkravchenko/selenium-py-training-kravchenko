from php4dvd.pages.page import Page
from selenium.webdriver.common.by import By


class FilmAddPage(Page):

    @property
    def save_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Save\"]")

    @property
    def submit_search_button(self):
        return self.driver.find_element_by_css_selector("input[type=\"submit\"]")

    @property
    def imdb_search_field(self):
        return self.driver.find_element_by_id("imdbsearch")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.ID, "imdbsearch"))

    @property
    def imdbid(self):
        return self.driver.find_element_by_name("imdbid")

    @property
    def year(self):
        return self.driver.find_element_by_name("year")

    @property
    def duration(self):
        return self.driver.find_element_by_name("duration")

    @property
    def rating(self):
        return self.driver.find_element_by_name("rating")

    @property
    def trailer(self):
        return self.driver.find_element_by_name("trailer")

    @property
    def name(self):
        return self.driver.find_element_by_name("name")

    @property
    def aka(self):
        return self.driver.find_element_by_name("aka")

    @property
    def format(self):
        return self.driver.find_element_by_name("format")

    @property
    def notes(self):
        return self.driver.find_element_by_name("notes")

    @property
    def taglines(self):
        return self.driver.find_element_by_name("taglines")

    @property
    def plotoutline(self):
        return self.driver.find_element_by_name("plotoutline")

    @property
    def plots(self):
        return self.driver.find_element_by_name("plots")

    @property
    def languages(self):
        return self.driver.find_element_by_name("languages")

    @property
    def subtitles(self):
        return self.driver.find_element_by_name("subtitles")

    @property
    def audio(self):
        return self.driver.find_element_by_name("audio")

    @property
    def video(self):
        return self.driver.find_element_by_name("video")

    @property
    def country(self):
        return self.driver.find_element_by_name("country")

    @property
    def genres(self):
        return self.driver.find_element_by_name("genres")

    @property
    def director(self):
        return self.driver.find_element_by_name("director")

    @property
    def writer(self):
        return self.driver.find_element_by_name("writer")

    @property
    def producer(self):
        return self.driver.find_element_by_name("producer")

    @property
    def music(self):
        return self.driver.find_element_by_name("music")

    @property
    def cast(self):
        return self.driver.find_element_by_name("cast")

    @property
    def home_link(self):
        # return self.driver.find_element((By.LINK_TEXT, "Home"))
        return self.driver.find_element_by_link_text("Home")



from php4dvd.model.user import User
from php4dvd.pages.internal_page import InternalPage
from php4dvd.pages.login_page import LoginPage
from php4dvd.pages.film_add_page import FilmAddPage
from php4dvd.pages.film_info_page import FilmInfoPage
from php4dvd.pages.user_management_page import UserManagementPage
from php4dvd.pages.user_profile_page import UserProfilePage
from php4dvd.pages.imdb_search_result_page import ImdbSearchResultPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.keys import Keys


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.user_profile_page = UserProfilePage(driver, base_url)
        self.user_management_page = UserManagementPage(driver, base_url)
        self.film_add_page = FilmAddPage(driver, base_url)
        self.film_info_page = FilmInfoPage(driver, base_url)
        self.imdb_search_result_page = ImdbSearchResultPage(driver, base_url)

    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(alert_is_present()).accept()

    def ensure_logout(self):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            self.logout()

    def login(self, user):
        lp = self.login_page
        lp.is_this_page
        lp.username_field.send_keys(user.username)
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def ensure_login_as(self, user):
        element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            # we are on internal page
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user)

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_logged_in_as(self, user):
        return self.is_logged_in() \
            and self.get_logged_user().username == user.username

    def is_not_logged_in(self):
        return self.login_page.is_this_page

    def get_logged_user(self):
        self.internal_page.user_profile_link.click()
        upp = self.user_profile_page
        upp.is_this_page
        return User(username=upp.user_form.username_field.get_attribute("value"),
                    email=upp.user_form.email_field.get_attribute("value"))

    def add_user(self, user):
        self.internal_page.user_management_link.click()
        ump = self.user_management_page
        ump.is_this_page
        ump.user_form.username_field.send_keys(user.username)
        ump.user_form.email_field.send_keys(user.email)
        ump.user_form.password_field.send_keys(user.password)
        ump.user_form.password1_field.send_keys(user.password)
        #ump.user_form.role_select.select_by_visible_text(user.role)
        ump.user_form.submit_button.click()

    def get_films_on_page(self):
        ip = self.internal_page
        return ip.movies_searcher

    def open_add_film_form(self):
        ip = self.internal_page
        ip.add_button.click()

    def is_field_works(self, element, keys, required_class, is_required = True):
        class BadRequiredFieldException(Exception):pass

        fap = self.film_add_page

        fap.is_this_page

        exec("fap."+element+".clear()")
        exec("fap."+element+".send_keys(str(keys))")
        exec("fap."+element+".send_keys(Keys.TAB)")

        if is_required:
            element_class_attribute = ""

            exec("element_class_attribute = fap."+element+".get_attribute(\"class\")")

            if str(element_class_attribute) != required_class:
                raise BadRequiredFieldException("Required field ", element, " was filled bad")
            else:
                return True

        else:
            return True

    def search_and_add_film_from_imdb(self, search_target):
        ip = self.internal_page
        fap = self.film_add_page
        isrp = self.imdb_search_result_page

        fap.is_this_page
        fap.imdb_search_field.send_keys(search_target)
        fap.submit_search_button.click()

        isrp.is_this_page
        isrp.is_element_visible((By.LINK_TEXT, search_target))
        #isrp.click_at_the_element((By.LINK_TEXT, search_target))
        isrp.click_at_the_link_text_element(search_target)

        fap.is_element_visible((By.CSS_SELECTOR, "img[alt=\"Save\"]"))
        fap.submit_search_button.click()

        # fap.home_link.click()
        # ip.is_element_visible((By.CLASS_NAME, "title"))

        fap.home_return()
        ip.is_this_page

    def home_return_call(self):
        ip = self.internal_page
        ip.home_return()

    def is_film_list_changed(self, films_before_changing, films_after_changing):
        class SmthWentWrongException(Exception):pass

        if len(films_before_changing) == len(films_after_changing):
            raise SmthWentWrongException("Film list was not changed")
        else:
            return True

    def remove_film(self):
        ip = self.internal_page
        fip = self.film_info_page

        ip.click_at_the_class_name_element("title")
        fip.is_this_page

        fip.remove_button.click()
        fip.accept_to_the_next_alert()

        ip.is_this_page














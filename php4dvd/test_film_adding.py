# -*- coding: utf-8 -*-
from model.user import User
import unittest

def test_film_adding_imdb_search(app):

    search_target_string = u"Криминальное чтиво"

    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    films_before_adding = app.get_films_on_page()

    app.open_add_film_form()
    app.search_and_add_film_from_imdb(search_target_string)

    films_after_adding = app.get_films_on_page()

    app.is_film_list_changed(films_before_adding, films_after_adding)

    app.logout()
    assert app.is_not_logged_in()

def test_film_adding_imbdid_field(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    app.open_add_film_form()

    app.is_field_works(element="imdbid", keys="666", required_class="digits")
    app.is_field_works(element="imdbid", keys="-1", required_class="digits error")
    app.is_field_works(element="imdbid", keys="not a number", required_class="digits error")
    app.is_field_works(element="imdbid", keys="", required_class="digits")

    app.logout()
    assert app.is_not_logged_in()

def test_film_adding_name_field(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    app.open_add_film_form()

    app.is_field_works(element="name", keys="13", required_class="required")
    app.is_field_works(element="name", keys="-1", required_class="required")
    app.is_field_works(element="name", keys="some name", required_class="required")
    app.is_field_works(element="name", keys="", required_class="required error")
    app.is_field_works(element="name", keys="!@#$%^&*()", required_class="required")

    app.logout()
    assert app.is_not_logged_in()

def test_film_adding_year_field(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    app.open_add_film_form()

    app.is_field_works(element="year", keys="1937", required_class="required digits")
    app.is_field_works(element="year", keys="-1", required_class="required digits error")
    app.is_field_works(element="year", keys="not a number", required_class="required digits error")
    app.is_field_works(element="year", keys="", required_class="required digits error")

    app.logout()
    assert app.is_not_logged_in()

def test_film_adding_duration_field(app):

    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    app.open_add_film_form()

    app.is_field_works(element="duration", keys="13", required_class="digits")
    app.is_field_works(element="duration", keys="-1", required_class="digits error")
    app.is_field_works(element="duration", keys="not a number", required_class="digits error")
    app.is_field_works(element="duration", keys="", required_class="digits")

    app.logout()
    assert app.is_not_logged_in()

def test_film_adding_rating_field(app):

    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    app.open_add_film_form()

    app.is_field_works(element="rating", keys="13", required_class="number")
    app.is_field_works(element="rating", keys="-1", required_class="number")
    app.is_field_works(element="rating", keys="not a number", required_class="number error")
    app.is_field_works(element="rating", keys="", required_class="number")

    app.logout()
    assert app.is_not_logged_in()

def test_film_adding_trailer_field(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    app.open_add_film_form()

    app.is_field_works(element="trailer", keys="13", required_class="url error")
    app.is_field_works(element="trailer", keys="-1", required_class="url error")
    app.is_field_works(element="trailer", keys="some text", required_class="url error")
    app.is_field_works(element="trailer", keys="", required_class="url")
    app.is_field_works(element="trailer", keys="http://www.ru", required_class="url")

    app.logout()
    assert app.is_not_logged_in()

def test_film_adding_full_data(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    app.open_add_film_form()
    films_before_adding = app.get_films_on_page()

    app.is_field_works(element="imdbid", keys="13", required_class="digits")
    app.is_field_works(element="name", keys="Seven", required_class="required")
    app.is_field_works(element="year", keys="1999", required_class="required digits")
    app.is_field_works(element="duration", keys="777", required_class="digits")
    app.is_field_works(element="rating", keys="5", required_class="number")
    app.is_field_works(element="format", keys="VHS", required_class="required ui-autocomplete-input")
    app.is_field_works(element="aka", keys="aka", required_class=None, is_required=False)
    app.is_field_works(element="notes", keys="notes", required_class=None, is_required=False)
    app.is_field_works(element="taglines", keys="taglines", required_class=None, is_required=False)
    app.is_field_works(element="plotoutline", keys="plotoutline", required_class=None, is_required=False)
    app.is_field_works(element="plots", keys="plots", required_class=None, is_required=False)
    app.is_field_works(element="languages", keys="Russian", required_class=None, is_required=False)
    app.is_field_works(element="subtitles", keys="subtitles", required_class=None, is_required=False)
    app.is_field_works(element="audio", keys="audio", required_class=None, is_required=False)
    app.is_field_works(element="video", keys="video", required_class=None, is_required=False)
    app.is_field_works(element="country", keys="country", required_class=None, is_required=False)
    app.is_field_works(element="genres", keys="genres", required_class=None, is_required=False)
    app.is_field_works(element="director", keys="director", required_class=None, is_required=False)
    app.is_field_works(element="writer", keys="writer", required_class=None, is_required=False)
    app.is_field_works(element="producer", keys="producer", required_class=None, is_required=False)
    app.is_field_works(element="music", keys="music", required_class=None, is_required=False)
    app.is_field_works(element="cast", keys="cast", required_class=None, is_required=False)

    app.home_return_call()

    films_after_adding = app.get_films_on_page()

    app.is_film_list_changed(films_before_adding, films_after_adding)

    app.logout()
    assert app.is_not_logged_in()

if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
from model.user import User
import unittest


def test_existed_film_local_searching(app):

    search_target = u"Криминальное чтиво"

    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    app.search_for_film(search_target)

    films_after_search = app.get_films_on_page()

    app.list_of_film_treatment(list_of_films=films_after_search, search_target=search_target)

    app.logout()
    assert app.is_not_logged_in()

def test_not_existed_film_local_searching(app):

    search_target = u"Красная шапочка"

    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    app.search_for_film(search_target, is_film_exists=False)

    films_after_search = app.get_films_on_page()

    app.list_of_film_treatment(list_of_films=films_after_search, search_target=search_target, is_film_exists=False)

    app.logout()
    assert app.is_not_logged_in()

if __name__ == "__main__":
    unittest.main()

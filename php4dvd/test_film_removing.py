# -*- coding: utf-8 -*-
from model.user import User
import unittest

def test_film_removing(app):

    class SmthWentWrongException(Exception):pass

    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

    films_before_removing = app.get_films_on_page()

    app.remove_film()

    films_after_removing = app.get_films_on_page()

    app.is_film_list_changed(films_before_removing, films_after_removing)

    app.logout()
    assert app.is_not_logged_in()

if __name__ == "__main__":
    unittest.main()

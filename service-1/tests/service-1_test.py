import unittest
from application import app, db
from application.models import lotr_character
from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
import requests


# Setting up our parent test class which is itself a child of another class (TestCase)
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///")
        app.config['SECRET_KEY'] = '24ygbnf2038jfhn023ndwj7gn2'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()


# This is testing that a Get request(g) is being displayed onto my html page(b) while also posting data with a post request(p) to service-5
class Test_Service_1(TestBase):
    def test_Get_And_Post_Requsts(self):
        with patch("requests.get") as g:
            g.return_value.text = "Lightning Fast"
            with patch("requests.post") as p:
                p.return_value.text = "Honed"
                response = self.client.get(url_for("Home"))
                self.assertIn(b"Lightning Fast", response.data)
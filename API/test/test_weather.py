import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from flask_jwt_extended import create_access_token
from ..models import Weather

class WeatherTestCase(unittest.TestCase):
    def setUp(self):
        '''create the app for testing'''
        self.app = create_app(config=config_dict['test'])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        '''tear down the database'''
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.client = None

    def test_post_weather_update_success(self):
        '''endpoint to test the post'''
        response = self.client.post('/weather', json={
            "city": "New York",
            "temperature": 25.5,
            "description": "Sunny"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('city', response.json)
        self.assertEqual(response.json['city'], 'New York')

    def test_post_weather_update_missing_fields(self):
        '''endpoint to test for missing field'''
        response = self.client.post('/weather', json={
            "city": "New York"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Missing required fields')

    def test_get_weather_update_success(self):
        '''testing the get endpoint'''
        weather = Weather(city="London", temperature=18.5, description="Cloudy")
        weather.save()
        response = self.client.get('/weather/London')
        self.assertEqual(response.status_code, 200)
        self.assertIn('city', response.json)
        self.assertEqual(response.json['city'], 'London')

    def test_get_weather_update_not_found(self):
        '''endpoint to test if weather update is not found'''
        response = self.client.get('/weather/UnknownCity')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'this city data is not on the database')


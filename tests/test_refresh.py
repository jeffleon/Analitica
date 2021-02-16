import unittest
from app.models import User, Role
from tests.test import BasicsTestCase
import requests
import json


class TestRefreshToken(BasicsTestCase):

    def test_refresh_token(self):
        user = {
            'username': 'karen', 
            'password': '1018485718'
        }
        session = requests.Session()
        res = session.post('http://localhost:8000/auth/login',
            json= user
        )

        token = json.loads(res.text)["access_token"]
        print("ok",res.headers)

        headers = {"authorization": 'Bearer {}'.format(token) }
        
        cookies = {"session": token}
        
        response = requests.post('http://localhost:8000/auth/refresh', headers=headers,
            json = user, cookies= cookies
        )
        
        print("ok my friend", response.headers)

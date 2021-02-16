import unittest
from app.models import User, Role
from tests.test import BasicsTestCase
import requests
import json


class TestLogin(BasicsTestCase):

    # success login
    def test_login(self):
        user = {
            'username': 'karen', 
            'password': '1018485718'
        }
        
        res = requests.post('http://localhost:8000/auth/login',
            json= user
        )
        
        self.assertEqual(res.status_code, 200)

    # wrong password
    def test_login_fail(self):
        user = {
            'username': 'karen', 
            'password': '123456789'
        }
        
        res = requests.post('http://localhost:8000/auth/login',
            json= user
        )
        
        self.assertEqual(res.status_code, 401)

    # wrong username
    def test_login_fail_2(self):
        user = {
            'username': 'karenxxxx', 
            'password': '1018485718'
        }
        
        res = requests.post('http://localhost:8000/auth/login',
            json= user
        )
       
        self.assertEqual(res.status_code, 401)

    # wrong params
    def test_login_fail_3(self):
        user = {
            'user': 'karen', 
            'password': '1018485718'
        }
        
        res = requests.post('http://localhost:8000/auth/login',
            json= user
        )
       
        self.assertEqual(res.status_code, 500)

    # wrong types
    def test_login_fail_4(self):
        user = {
            'user': 'karen', 
            'password': 1018485718
        }
        
        res = requests.post('http://localhost:8000/auth/login',
            json= user
        )
       
        self.assertEqual(res.status_code, 500)
    

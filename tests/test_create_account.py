import unittest
from app.models import User, Role
from tests.test import BasicsTestCase
import requests
import json

class TestCreateAccount(BasicsTestCase):

    # success create account
    def test_create_account(self):
        user = {
            'username': 'perexw', 
            'password': '12345678'
        }
        res = requests.post('http://localhost:8000/auth/create_account',
            json= user
        )
        
        self.assertEqual(res.status_code, 201)

    # wrong params
    def test_fail_create_account(self):
        user = {
            'us': 'perez', 
            'password': '12345678'
        }
        res = requests.post('http://localhost:8000/auth/create_account',
            json= user
        )
        
        self.assertEqual(res.status_code, 500)

    # account exists
    def test_exists_create_account(self):
        user = {
            'username': 'jefferson', 
            'password': '12345678'
        }
        res = requests.post('http://localhost:8000/auth/create_account',
            json= user
        )
        
        self.assertEqual(res.status_code, 401)

    # wrong types
    def test_wrong_type_create_account(self):
        user = {
            'username': 'jefferson', 
            'password': 12345678
        }
        res = requests.post('http://localhost:8000/auth/create_account',
            json= user
        )
        
        self.assertEqual(res.status_code, 401)

    
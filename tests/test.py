import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        # Crea un contexto de aplicación
    
    #def tearDown(self):
        #with self.app.app_context():
            # Elimina todas las tablas de la base de datos
            #db.session.remove()
            #db.drop_all()



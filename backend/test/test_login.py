#!/usr/bin/env python

import unittest
from uuid import uuid4
from src import create_app, get_db_client, get_db_instance
from config import AppConfig
from passlib.hash import pbkdf2_sha256


class TestConfig(AppConfig):
    TESTING = True
    DB_NAME = 'testdb_login'


class TestUserLogin(unittest.TestCase):
    def setUp(self):
        self._app = create_app(TestConfig)
        self._app_context = self._app.app_context()
        self._app_context.push()
        self._testdb = get_db_instance()


    def tearDown(self):
        get_db_client().drop_database(self._testdb)
        self._app_context.pop()


    def test_login(self):
        # Add a test user in database
        user_name = 'AniketGM'
        user_email = 'aniketgm@test.com'
        user_passwd = 'some-password'
        test_user = {
            "_id": uuid4().hex,
            "name": user_name,
            "email": user_email,
            "password": pbkdf2_sha256.hash(user_passwd)
        }
        self._testdb.users.insert_one(test_user)

        with self._app.test_client() as tc:
            # import pudb; pu.db
            # Test client call for login
            resp = tc.post('/api/login', json = {
                "email": user_email,
                "password": user_passwd
            })

            # Check if session contains logged_in and user attributes
            del test_user['password']
            with tc.session_transaction() as ssn:
                self.assertEqual(ssn['logged_in'], True, "Session's logged_in attribute should be True")
                self.assertEqual(ssn['user'], test_user, "Session's user attribute should contain user info")

            # Signout and delete the document from collection
            resp = tc.get('/api/signout')
            res = self._testdb.users.delete_one({ "name": user_name })

            # Check if the entry is deleted
            self.assertEqual(res.deleted_count, 1, "Only 1 document should be deleted")



import uuid
from flask import jsonify, session
from src import get_db_instance
from passlib.hash import pbkdf2_sha256

class UserAuth:

    # Get DB instance to manipulate data.
    def __init__(self) -> None:
        self._db = get_db_instance()

    # Start session when logged in OR signed in.
    def start_session(self, user: dict):
        data = {}
        if not session.get('logged_in', False):
            del user['password']
            session['logged_in'] = True
            session['user'] = user
            data = user
        else:
            data['message'] = 'Already logged in'
        return jsonify(data), 200

    # Called from signup to add new user. This will start the session as well.
    def add_new_user(self, user_info: dict):
        if user_info:
            if self._db.users.find_one({ 'email': user_info['email'] }):
                return jsonify({ 'error': 'Email already in use' }), 400

            user_info['password'] = pbkdf2_sha256.hash(user_info['password'])
            if self._db.users.insert_one(user_info):
                return self.start_session(user_info)
        else:
            return jsonify({ 'error': 'User information missing!' }), 500

    # Called from login to verify and start session.
    def get_existing_user(self, user_info: dict):
        if user_info:
            user = self._db.users.find_one({ 'email': user_info['email'] })
            if user and pbkdf2_sha256.verify(user_info['password'], user['password']):
                return self.start_session((user))
            else:
                return jsonify({ 'error': "Invalid user input" }), 400
        else:
            return jsonify({ 'error': 'User information missing!' }), 500

    # Called from logout to stop session.
    def stop_session(self):
        session.clear()
        return jsonify({'message': 'Logged out successfully'}), 200


def get_signup_data(name: str, email: str, pswd: str) -> dict:
    return {
        '_id': uuid.uuid4().hex,
        'name': name,
        'email': email,
        'password': pswd
    }

def get_login_data(email: str, pswd: str) -> dict:
    return {
        'email': email,
        'password': pswd
    }


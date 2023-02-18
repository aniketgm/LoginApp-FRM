from src.auth import auth_blueprint as abp
from flask import request
from src.models import UserAuth, get_login_data, get_signup_data

@abp.route('/api/signup', methods=['POST'])
def signup():
    userinfo = request.get_json()
    data = {}
    if userinfo is not None:
        name = userinfo['name']
        email = userinfo['email']
        password = userinfo['password']
        data = get_signup_data(name, email, password)
    return UserAuth().add_new_user(data)

@abp.route('/api/login', methods=['POST'])
def login():
    userinfo = request.get_json()
    data = {}
    if userinfo is not None:
        email = userinfo['email']
        password = userinfo['password']
        data = get_login_data(email, password)
    return UserAuth().get_existing_user(data)

@abp.route('/api/logout', methods=['POST'])
def logout():
    return UserAuth().stop_session()


from flask_cors import cross_origin
from src.auth import auth_blueprint as abp
from flask import request
from src.models import UserAuth, get_login_data, get_signup_data

@abp.route('/api/signup', methods=['POST'])
@cross_origin()
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
@cross_origin()
def login():
    userinfo = request.get_json()
    data = {}
    if userinfo is not None:
        email = userinfo['email']
        password = userinfo['password']
        data = get_login_data(email, password)
    return UserAuth().get_existing_user(data)

@abp.route('/api/logout', methods=['POST'])
@cross_origin()
def logout():
    print('Got here...')
    UserAuth().stop_session()
    print('Done...')


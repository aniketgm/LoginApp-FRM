from src.auth import auth_blueprint as abp
from flask import request
from src.models import UserAuth, get_login_data, get_signup_data

@abp.route('/api/signup', methods=['POST'])
def signup():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    data = get_signup_data(name, email, password)
    return UserAuth().add_new_user(data)

@abp.route('/api/login', methods=['POST'])
def login():
    email = request.form.get('email', '')
    password = request.form.get('password', '') 
    data = get_login_data(email, password)
    return UserAuth().get_existing_user(data)

@abp.route('/api/logout')
def logout():
    UserAuth().stop_session()


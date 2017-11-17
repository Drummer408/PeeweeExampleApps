#1/usr/bin/env python3

import getpass

from models import db, User

active_user = None

def initialize():
    db.connect()
    db.create_tables([User], safe = True)

def login_loop():
    while True:
        username = input('Enter username: ')
        password = getpass.getpass('Enter password: ')
        user_content = User.get_user(username)
        if validate_credentials(user_content, password):
            break
        print('\nInvalid username or password. Please try again.\n')
    active_user = user_content

def validate_credentials(user_content, password):
    return user_content != None and user_content.password == password

def menu_loop():
    pass

if __name__ == "__main__":
    initialize()
    User.create_user('Chris Khedoo', 'test123!', 'chriskhedoo@gmail.com', 'CEO/Chairman', 'US East', True)
    login_loop()
    menu_loop()
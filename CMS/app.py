#1/usr/bin/env python3

import getpass

from models import db, User

def initialize():
    db.connect()
    db.create_tables([User], safe = True)

def login_loop():
    while True:
        username = input('Enter username: ')
        password = getpass.getpass('Enter password: ')
        if validate_credentials(username, password):
            break
        print('\nInvalid username or password. Please try again.\n')

def validate_credentials(username, password):
    user = User.get_user(username)
    return user != None and user.password == password

def menu_loop():
    pass

if __name__ == "__main__":
    initialize()
    User.create_user('Chris Khedoo', 'test123!', 'chriskhedoo@gmail.com', 'CEO/Chairman', 'US East', True)
    login_loop()
    menu_loop()
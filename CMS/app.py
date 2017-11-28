#!/usr/bin/env python3

import datetime
import getpass

from models import db, User, Login

active_user = None

def initialize():
    db.connect()
    db.create_tables([User, Login], safe = True)

def login_loop():
    while True:
        username = input('Enter username: ').strip()
        password = getpass.getpass('Enter password: ').strip()
        login_record = Login.get_login_record(username)
        if Login.validate_credentials(login_record, password):
            break
        print('\nInvalid username or password. Please try again.\n')
    global active_user
    active_user = User.get_user_record('Chris Khedoo')

def menu_loop():
    print('Welcome, {}!                 {}'.format(active_user.username, datetime.datetime.now().strftime('%A %B %d, %Y %I:%M:%S%p')))

if __name__ == "__main__":
    initialize()
    User.create_user_record('Chris Khedoo', 'chriskhedoo@gmail.com', 'CEO/Chairman', 'US East')
    Login.create_login_record('Chris Khedoo', 'test123!')
    login_loop()
    menu_loop()

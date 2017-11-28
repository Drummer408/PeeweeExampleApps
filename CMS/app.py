#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import getpass

from models import db, User, Login

active_user = None

def initialize():
    """Initialize the database."""
    db.connect()
    db.create_tables([User, Login], safe = True)

def login_loop():
    """Allow the user to login."""
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
    """Show the menu."""
    print('\nWelcome, {}!                 {}'.format(active_user.username, datetime.datetime.now().strftime('%A %B %d, %Y %I:%M:%S%p')))
    print()

    choice = None
    while choice != 'q':
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        print('q) Quit')
        choice = input('Enter a selection from above: ').lower().strip()

        if choice in menu:
            menu[choice]()
        elif choice != 'q':
            print('\nInvalid selection. Please try again.\n')

    print('\nSession terminated.\n')

def add_user():
    """Add a user"""
    pass

def search_user():
    """Search for a user"""
    pass

def modify_user():
    """Modify a user's information"""
    pass

def remove_user():
    """Remove a user"""
    pass

menu = OrderedDict([
    ('a', add_user),
    ('s', search_user),
    ('m', modify_user),
    ('r', remove_user)
])

if __name__ == "__main__":
    initialize()
    User.create_user_record('Chris Khedoo', 'chriskhedoo@gmail.com', 'CEO/Chairman', 'US East')
    Login.create_login_record('Chris Khedoo', 'test123!')
    login_loop()
    menu_loop()

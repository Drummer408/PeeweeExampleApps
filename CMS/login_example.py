#!/usr/bin/env python3

import getpass

username = input('Enter username: ')
password = getpass.getpass('Enter password: ')
confirm_password = getpass.getpass('Confirm password: ')

if password == confirm_password:
    print('Welcome, {}!\n'.format(username))
else:
    print("Passwords don't match!\n")
    
#!/usr/bin/env python3

import datetime
import random

from peewee import *

db = SqliteDatabase('cms.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = PrimaryKeyField()
    username = CharField(max_length = 12, unique = True)
    email = CharField(unique = True)
    join_date = DateTimeField(default = datetime.datetime.now)
    title = CharField(max_length = 70)
    region = CharField(max_length = 20)
    
    @classmethod
    def create_user_record(cls, username, email, title, region):
        id = cls.generate_user_id()
        try:
            cls.create(
                user_id = id,
                username = username,
                email = email,
                title = title,
                region = region)
            return True
        except IntegrityError:
            return False

    @classmethod
    def get_user_record(cls, username):
        user_record = None
        try:
            user_record = cls.get(cls.username == username)
        except User.DoesNotExist:
            pass
        return user_record

    @staticmethod
    def generate_user_id():
        while (True):
            id = random.randint(1000000, 9999999)
            try:
                user_content = User.get(User.user_id == id)
            except User.DoesNotExist:
                break
        return id

class Login(BaseModel):
    username = ForeignKeyField(User, to_field = 'username')
    password = CharField(max_length = 100)

    @classmethod
    def create_login_record(cls, username, password):
        try:
            cls.create(
                username = username,
                password = password
            )
            return True
        except IntegrityError:
            return False

    @classmethod
    def get_login_record(cls, username):
        login_record = None
        try:
            login_record = cls.get(cls.username == username)
        except Login.DoesNotExist:
            pass
        return login_record

    @staticmethod
    def validate_credentials(login_record, password):
        return login_record != None and login_record.password == password

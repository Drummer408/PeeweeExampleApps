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
    password = CharField(max_length = 100)
    email = CharField(unique = True)
    join_date = DateTimeField(default = datetime.datetime.now)
    title = CharField(max_length = 70)
    region = CharField(max_length = 20)
    is_admin = BooleanField(default = False)
    
    @classmethod
    def create_user(cls, username, password, email, title, region, is_admin):
        id = cls.generate_user_id()
        try:
            cls.create(
                user_id = id,
                username = username,
                password = password,
                email = email,
                title = title,
                region = region,
                is_admin = is_admin)
        except IntegrityError:
            print('\nUser already exists!\n')

    @staticmethod
    def generate_user_id():
        while (True):
            id = random.randint(1000000, 9999999)
            try:
                user_content = User.get(User.user_id == id)
            except User.DoesNotExist:
                break
        return id

def initialize():
    db.connect()
    db.create_tables([User], safe = True)

if __name__ == "__main__":
    initialize()

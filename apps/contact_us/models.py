"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth
from pydal.validators import *


def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()

# Complete. 
db.define_table('contact_requests',
                Field('name', requires=IS_NOT_EMPTY()),
                Field('email', requires=IS_EMAIL()),
                Field('phone', requires=IS_NOT_EMPTY()),
                Field('message', 'text', requires=IS_NOT_EMPTY()),
                Field('created_on', 'datetime', default=get_time),
                Field('user_email', default=get_user_email),
)

db.commit()

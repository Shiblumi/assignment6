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

# Define db table
db.define_table('contact_requests',
                Field('name', requires=IS_NOT_EMPTY(),),
                Field('email', requires=IS_EMAIL()), 
                Field('phone', requires=IS_NOT_EMPTY()),
                Field('message', 'text'),
                Field('created_on', 'datetime', default=get_time),
                Field('user_email', default=get_user_email),
)

# Adjust db field visibility on form
db.contact_requests.created_on.readable = False
db.contact_requests.created_on.writable = False
db.contact_requests.user_email.readable = False
db.contact_requests.user_email.writable = False

db.contact_requests.id.readable = False
db.contact_requests.id.writable = False

db.commit()

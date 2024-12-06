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
                Field('name'),
                Field('email'),
                Field('phone'),
                Field('message', 'text'),
                Field('created_on', 'datetime', default=get_time),
                Field('user_email', default=get_user_email),
)

# Adjust db field visibility on form
db.contact_requests.created_on.writable = False
db.contact_requests.user_email.writable = False

# Adjust db field validation
db.contact_requests.name.requires = IS_NOT_EMPTY()
db.contact_requests.email.requires = IS_EMAIL()
db.contact_requests.phone.requires = IS_NOT_EMPTY()

db.commit()

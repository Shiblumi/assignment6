from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.url_signer import URLSigner
from .models import get_user_email
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid, GridClassStyleBulma


# Index page
@action('index', method=["GET", "POST"])
@action.uses('index.html', db, auth.user)
def index():
    form = Form(db.contact_requests, formstyle=FormStyleBulma)
    if form.accepted:
        redirect(URL('index'))
    return dict(form=form)

# Admin Page
@action('contact_requests', method=["GET", "POST"])
@action.uses('contact_requests.html', db, auth.user)
def contact_requests():
    user_email = get_user_email()
    if user_email != 'admin@example.com':
        redirect(URL('index'))
        
    grid = Grid(
                path=URL('contact_requests'),
                query=db.contact_requests,
                orderby=~db.contact_requests.created_on,
                search_queries=[
                    ('Search by Name', lambda val: db.contact_requests.name.contains(val)),
                    ('By Message', lambda val: db.contact_requests.message.contains(val))
                ],
                editable=False,
                deletable=True,
                create=False,
                details=False,
                grid_class_style=GridClassStyleBulma,
                )
    
    return dict(grid=grid)
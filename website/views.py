from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event
from . import db

# Create a Blueprint for the main part of the application
mainbp = Blueprint('main', __name__)

# Route to display the main index page
@mainbp.route('/')
def index():
    # Retrieve a list of events from the database
    events = db.session.scalars(db.select(Event)).all()
    return render_template('index.html', events=events)

# Route to search for events
@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        # Get the search query from the request
        query = "%" + request.args['search'] + "%"
        # Search for events whose description contains the query
        events = db.session.scalars(db.select(Event)).where(Event.description.like(query))
        return render_template('index.html', events=events)
    else:
        # If no search query provided, redirect to the main index page
        return redirect(url_for('main.index'))

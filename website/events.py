from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Comment
from .forms import EventForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

# Create a Blueprint for events
bp = Blueprint('event', __name__, url_prefix='/events')

# Show the details of an event
@bp.route('/<id>')
def show(id):
    # Retrieve the event with the given ID
    event = db.session.scalar(db.select(Event).where(Event.id == id))
    # Create a CommentForm
    form = CommentForm()
    return render_template('events/show.html', event=event, form=form)

# Create a new event
@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = EventForm()
    if form.validate_on_submit():
        db_file_path = check_upload_file(form)
        # Create a new event and add it to the database
        event = Event(
            name=form.name.data,
            description=form.description.data,
            image=db_file_path,
            venue=form.venue.data,
            date=form.date.data
        )
        db.session.add(event)
        db.session.commit()
        flash('Successfully created new event', 'success')
        return redirect(url_for('event.create'))
    return render_template('events/create.html', form=form)

# Function to handle file uploads
def check_upload_file(form):
    fp = form.image.data
    filename = fp.filename
    BASE_PATH = os.path.dirname(__file__)
    upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
    db_upload_path = '/static/image/' + secure_filename(filename)
    fp.save(upload_path)
    return db_upload_path

# Add a comment to an event
@bp.route('/<id>/comment', methods=['GET', 'POST'])
@login_required
def comment(id):
    form = CommentForm()
    event = db.session.scalar(db.select(Event).where(Event.id == id))
    if form.validate_on_submit():
        comment = Comment(
            text=form.text.data,
            event=event,
            user=current_user
        )
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added', 'success')
    return redirect(url_for('event.show', id=id))

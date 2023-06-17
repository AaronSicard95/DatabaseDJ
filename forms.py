"""Forms for playlist app."""

from wtforms import SelectField, SelectMultipleField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import Length
from wtforms_alchemy import QuerySelectMultipleField


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField('Name', validators=[Length(min=1, message="Name must be at least 1 character")])
    description = StringField('Description')


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    title = StringField('Name', validators=[Length(min=1, message="Title must be at least 1 character")])
    artist = StringField('Name', validators=[Length(min=1, message="Artist must be at least 1 character")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    songs = QuerySelectMultipleField('Songs To Add')

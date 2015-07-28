from flask.ext.wtf import form
from wtform import StringField, Select StringField
from wtforms.validators import DataRequired

class EventSearch(Form)
	event_name = StringField('event_name'), validators=[DataRequired()]
	location = SelectField('location'),choices=[('BrassTap MT','BrassTap DT', 'MadSo CT')]
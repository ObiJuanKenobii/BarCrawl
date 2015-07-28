from flask import render_template
from t_app import my_app
@my_app.route('/')
@my_app.route('/index')
def index():
	return render_template('index.html')

from flask import Blueprint
from flask import render_template, request
from flask import redirect
from flask import url_for
from flask_login import login_user, login_required, logout_user, current_user
import random 
views = Blueprint('views', __name__)

@views.route('/')
# @login_required
def index():
    return render_template('index.html')
    # return redirect(url_for('views.submit'))


@views.route('/demo')
def demo():
    return render_template("demo.html")

@views.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form
        string = data['textarea']
        formatted_string_list = string.split('\r\n')
        list_with_index = list(enumerate(formatted_string_list))
        winner = random.choice(list_with_index)
        return render_template("demo.html", list_with_index=list_with_index, winner=winner)
 
    return render_template("submitname.html")

@views.route('/winner', methods=['POST', 'GET'])
def winner():

    return render_template("winner.html")

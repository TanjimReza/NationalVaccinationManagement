from flask import Blueprint
from flask import render_template, request
from flask import redirect
from flask import url_for
from flask_login import login_user, login_required, logout_user, current_user
import random 
from . import db
from functools import wraps
from .models import RegularUser, Hospital, Vaccine, User_Vaccine_Info, Vaccine_Request, NationalSystem,Hospital_Vaccine_Stock
views = Blueprint('views', __name__)



def hospital_required(func):
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            if current_user.email.split('@')[1] == 'hospital.com':
                return func(*args, **kwargs)
            else:
                return redirect(url_for('views.dashboard'))
        else:
            return redirect(url_for('auth.login'))
    return wrapper


@views.route('/')
# @login_required
def index():
    return render_template('index.html')
    # return redirect(url_for('views.submit'))

@views.route('/dashboard')
def dashboard():
    print(f"{current_user=} is logged in")
    return render_template('dashboard.html')


@views.route('/home', methods=['GET', 'POST'])  
@login_required
def home():
    return render_template('home.html')

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

@views.route('/vaccineregistration', methods=['POST', 'GET'])
def vaccineregistration():
    if request.method == 'POST':
        data = request.form
        print(data)
       
    if request.method == 'POST':
        print(request.form.get('nid_number'))
        new_user_vaccine_info = User_Vaccine_Info(
            v_user_id = RegularUser.query.filter_by(nid=request.form.get('nid_number')).first().nid,
            v_hospital_id = Hospital.query.filter_by(hospital_id=request.form.get('hospital_id')).first().hospital_id,
            vaccine_name = request.form.get('vaccine_for'),
        )
        db.session.add(new_user_vaccine_info)
        db.session.commit()
        print(f"\n\n VACCINE ADDED \n\n")
        return redirect(url_for('views.dashboard'))
    
    hospitals = Hospital.query.all()
    print(hospitals)
    
    context = {'hospitals': hospitals}
    print(context)
    return render_template("vaccine-registration.html", context=context) 



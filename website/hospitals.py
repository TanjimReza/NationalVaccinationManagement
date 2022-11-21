from flask import Blueprint
from flask import render_template, request
from flask import redirect
from flask import url_for
from flask_login import login_user, login_required, logout_user, current_user
import random 
from . import db
from functools import wraps
from .models import RegularUser, Hospital, Vaccine, User_Vaccine_Info, Vaccine_Request, NationalSystem,Hospital_Vaccine_Stock

hospital = Blueprint('hospitals', __name__)

@hospital.route('/hospitals')
def hospital_view():
    print("Here")
    return render_template('dashboard.html')

@hospital.route('/request-vaccine', methods=['POST', 'GET'])
def request_vaccine():
    
    return render_template('request-vaccine.html')
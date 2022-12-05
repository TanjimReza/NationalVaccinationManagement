from flask import Blueprint
from flask import render_template, request
from flask import redirect
from flask import url_for
from flask_login import login_user, login_required, logout_user, current_user
import random 
from . import db
from functools import wraps
from .models import RegularUser, Hospital, Vaccine, UserVaccineInfo, VaccineRequest, NationalSystem,HospitalVaccineStock

admin = Blueprint('admin', __name__)

def require_admin(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if current_user.is_authenticated:
            if current_user.email.split('@')[1] == 'admin.com':
        
                return f(*args, **kwargs)
            else:
                return redirect(url_for('views.dashboard'))
        
        else:
            return redirect("/")
    return decorated_func
@admin.route('/national-vaccine-stock', methods=['POST', 'GET'])
@require_admin
def national_vaccine_stock():
    print("here")
    if request.method == 'POST':
        print("POST DATA:")
        data = request.form
        print(data)
        vaccine_name = data['add_vaccine_name']
        add_amount = 0 
        remove_amount = 0
        try: 
            add_amount = int(data['add_vaccine_amount'])
        except:
            remove_amount = int(data['remove_vaccine_amount'])
        print(f"{vaccine_name=}, {add_amount=}, {remove_amount=}")
        vaccine = Vaccine.query.filter_by(vaccine_name=vaccine_name).first()
        vaccine.vaccine_amount = vaccine.vaccine_amount + add_amount - remove_amount
        
        db.session.commit()

    
        print("VACCINE STOCK UPDATED")
        return redirect(url_for('admin.national_vaccine_stock'))
    
    
    vaccines = Vaccine.query.all()
    print(vaccines)
    return render_template("national-vaccine-stock.html", vaccines=vaccines)

@admin.route('/add-new-vaccine', methods=['POST', 'GET'])
@require_admin
def add_new_vaccine():
    if request.method == 'POST':
        print("POST DATA:")
        data = request.form
        print(data)
        new_vaccine = Vaccine(
            vaccine_name = data['new_vaccine_name'],
            vaccine_amount = data['new_vaccine_amount'],
        )
        db.session.add(new_vaccine)
        db.session.commit()
        print("VACCINE ADDED")
        return redirect(url_for('admin.national_vaccine_stock'))
    return render_template("add-new-vaccine.html")


@admin.route('/permit-hospitals', methods=['POST', 'GET'])
@require_admin
def permit_hospitals():
    if request.method == 'POST':
        print("POST DATA:")
        data = request.form
        print("\n\n\n DATA: ", data)
        hospital_id = data['hospital_name']
        hospital = Hospital.query.filter_by(hospital_id=hospital_id).first()
        print("HOSPITAL: ", hospital)
        hospital.status = "Approved"
        db.session.commit()
        print("HOSPITAL PERMITTED")
        return redirect(url_for('admin.permit_hospitals'))
    hospitals = Hospital.query.filter_by(status="Requested").all()
    print(hospitals)
    return render_template("permit-hospitals.html", hospitals=hospitals)
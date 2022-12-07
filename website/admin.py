from flask import Blueprint
from flask import render_template, request
from flask import redirect
from flask import url_for
from flask_login import login_user, login_required, logout_user, current_user
import random 
from . import db
from functools import wraps
from .models import RegularUser, Hospital, Vaccine, UserVaccineInfo, VaccineRequest, NationalSystem,HospitalVaccineStock

admin = Blueprint('admin', __name__, template_folder='templates/admin')

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

@admin.route('/hospital-requests', methods=['POST', 'GET'])
@require_admin
def hospital_requests():
    if request.method == "POST":
        data = request.form
        print(data)
        hospital_id = data['hospital_name']
        vaccine_amount = data['vaccine_amount']
        vaccine_serial = data['vaccine_name']
        request_id = data['request_id']
        hospital = Hospital.query.filter_by(hospital_id=hospital_id).first()
        vaccine = Vaccine.query.filter_by(vaccine_serial=vaccine_serial).first()
        
        hospital_vaccine_stock = HospitalVaccineStock.query.filter_by(hospital_id=hospital_id, vaccine_id=vaccine_serial).first()
        if hospital_vaccine_stock:
            hospital_vaccine_stock.vaccine_amount = hospital_vaccine_stock.vaccine_amount + int(vaccine_amount)
            db.session.commit()
            print("HOSPITAL STOCK UPDATED")
        
        else:
            new_hospital_stock = HospitalVaccineStock(
                hospital_id = hospital.hospital_id,
                vaccine_id = vaccine.vaccine_serial,
                vaccine_name = vaccine.vaccine_name,
                vaccine_amount = vaccine_amount)
            db.session.add(new_hospital_stock)
            db.session.commit()
            print("HOSPITAL STOCK ADDED")
            
        #! Bug-Fix: Multiple Entries of same vaccine in HospitalVaccineStock
        # new_hospital_stock = HospitalVaccineStock(
        #     hospital_id = hospital.hospital_id,
        #     vaccine_id = vaccine.vaccine_serial,
        #     vaccine_name = vaccine.vaccine_name,
        #     vaccine_amount = vaccine_amount)
        # db.session.add(new_hospital_stock)
        # db.session.commit()
        # print("HOSPITAL STOCK ADDED")
        
        vaccine_request = VaccineRequest.query.filter_by(id=request_id).first()
        vaccine_request.request_status = "Approved"
        db.session.commit()
        print("VACCINE REQUEST APPROVED")

        
    hospital_requests = VaccineRequest.query.all()
    return render_template("hospital-requests.html", hospital_requests=hospital_requests)
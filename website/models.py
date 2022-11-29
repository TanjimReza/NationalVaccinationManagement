from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class RegularUser(UserMixin, db.Model):
    nid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    mobile = db.Column(db.String(100))
    user_type = db.Column(db.String(100), default='regular')
    balance = db.Column(db.Integer)
    def get_id(self):
        return (self.email)

class NationalSystem(UserMixin, db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    user_type = db.Column(db.String(100), default='admin')
    def get_id(self):
        return (self.email)
    
class Hospital(UserMixin, db.Model):
    name = db.Column(db.String(100))
    hospital_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    address = db.Column(db.String(100), default='Dhaka')
    user_type = db.Column(db.String(100), default='hospital')

    def get_id(self):
        return (self.email)

class Hospital_Vaccine_Stock(db.Model):
    vaccine_id = db.Column(db.Integer, primary_key=True)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.hospital_id'))
    vaccine_name = db.Column(db.String(100))
    vaccine_quantity = db.Column(db.Integer)
    

class Vaccine(db.Model):
    vaccine_serial = db.Column(db.Integer, primary_key=True)
    vaccine_name = db.Column(db.String(100), primary_key=True)
    vaccine_amount = db.Column(db.Integer, default=0)

class User_Vaccine_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    v_user_id = db.Column(db.Integer, db.ForeignKey('regular_user.nid'))
    v_hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.hospital_id'))
    vaccine_name = db.Column(db.String(100), db.ForeignKey('vaccine.vaccine_name'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
class Vaccine_Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    req_hid = db.Column(db.Integer)
    v_name = db.Column(db.String(100))
    req_amount = db.Column(db.Integer)
    req_date = db.Column(db.DateTime(timezone=True), default=func.now())
    approved_by = db.Column(db.Integer)
    approved_amount = db.Column(db.Integer) 
    status = db.Column(db.String(100), default='pending')
    approved_date = db.Column(db.DateTime(timezone=True), default=func.now())

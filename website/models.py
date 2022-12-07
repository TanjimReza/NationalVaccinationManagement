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
    status = db.Column(db.String(100), default='NotVerified')


    def get_id(self):
        return (self.email)

class HospitalVaccineStock(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.hospital_id'))
    vaccine_id = db.Column(db.Integer, db.ForeignKey('vaccine.vaccine_serial'))
    vaccine_name = db.Column(db.String(100))
    vaccine_amount = db.Column(db.Integer)



class Vaccine(db.Model):
    vaccine_serial = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vaccine_name = db.Column(db.String(100), default='Covid-19')
    vaccine_amount = db.Column(db.Integer, default=0)

    
class UserVaccineInfo(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('regular_user.nid'))
    user_name = db.Column(db.String(100))
    vaccine_id = db.Column(db.Integer, db.ForeignKey('vaccine.vaccine_serial'))
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.hospital_id'))
    vaccine_name = db.Column(db.String(100))
    vaccine_status = db.Column(db.String(100), default='NotTaken')
    vaccine_serial = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vaccine_date = db.Column(db.DateTime(timezone=True), default=func.now())
 

class VaccineRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vaccine_id = db.Column(db.Integer, db.ForeignKey('vaccine.vaccine_serial'))
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.hospital_id'))
    vaccine_name = db.Column(db.String(100))
    request_amount = db.Column(db.Integer)
    request_status = db.Column(db.String(100), default='Pending')


    


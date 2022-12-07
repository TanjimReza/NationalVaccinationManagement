from flask import Blueprint,render_template,redirect,url_for,request, flash
from .models import RegularUser, Hospital, Vaccine, UserVaccineInfo, VaccineRequest, NationalSystem
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email, password)
        
        if email.split('@')[1] == 'admin.com':
            print(f"Admin User Detected! Logging In: {email} from National System")
            user = NationalSystem.query.filter_by(email=email).first()
        elif email.split('@')[1] == 'hospital.com':
            print(f"Hospital User Detected! Logging In: {email} from Hospital")
            user = Hospital.query.filter_by(email=email).first()
        else: 
            print(f"Regular User Detected! Logging In: {email} from Regular User")
            user = RegularUser.query.filter_by(email=email).first()
        print(f"{user=} Found! Initiating Password Check")
        if user:
            if check_password_hash(user.password, password):
                print("Password Verified!")
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html")



@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    print("SIGNUP")
    if request.method == 'POST':
        print(request.form)
        email = request.form.get('email')
        password = request.form.get('password')
        last_name = request.form.get('last_name').lower()
        
        regular, admin, hospital = RegularUser.query.filter_by(email=email).first(), \
                                   NationalSystem.query.filter_by(email=email).first(),\
                                   Hospital.query.filter_by(email=email).first()
        
        if any([regular, admin, hospital]):
            print("Email already exists")
            if regular:
                flash('Regular user email already exists.', category='error')
            if admin:
                flash('Admin email already exists.', category='error')
            if hospital:
                flash('Hospital email already exists.', category='error')
                
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            pass
        elif len(password) < 4:
            flash('Password must be greater than 3 characters.', category='error')
            pass
        else: 
            if last_name.lower() == "admin":
                print("Creating ADMIN")
                new_user = NationalSystem(
                    admin_id = request.form.get('nid_number'),
                    name = request.form.get('first_name'),
                    email=email, 
                    password=generate_password_hash(password, method='sha256'),
                    user_type = 'admin',
                    )
                db.session.add(new_user)
                db.session.commit()
                flash('Logged in successfully!', category='success')
                login_user(new_user, remember=True)
                print(f"\n\n ADMIN ADDED \n\n")
                return redirect(url_for('views.index'))
            if last_name.lower() == "hospital":
                print("Creating HOSPITAL")
                new_user = Hospital(
                    hospital_id = request.form.get('nid_number'),
                    name = request.form.get('first_name'),
                    email=email, 
                    password=generate_password_hash(password, method='sha256'),
                    )
                db.session.add(new_user)
                db.session.commit()
                flash('Logged in successfully!', category='success')
                login_user(new_user, remember=True)
                print(f"\n\n HOSPITAL ADDED \n\n")
                return redirect(url_for('views.index'))
            else:
                print("Creating REGULAR USER")
                new_user = RegularUser(
                    nid = request.form.get('nid_number'),
                    email=email, 
                    password=generate_password_hash(password, method='sha256'),
                    first_name = request.form.get('first_name'),
                    last_name = request.form.get('last_name'),
                    mobile = request.form.get('mobile'),
                    balance = 0,
                    user_type = 'regular',
                    )
                db.session.add(new_user)
                db.session.commit()
                flash('Logged in successfully!', category='success')
                login_user(new_user, remember=True)
                print(f"\n\n REGULAR USER ADDED \n\n")
                return redirect(url_for('views.dashboard'))

        # print(data)
    context = { 'title': 'TANJIM' }
    return render_template("signup.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

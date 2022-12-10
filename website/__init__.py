from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail, Message

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__, 
                static_url_path='/',
                static_folder='static',
                template_folder='templates',
                )
    # app.config['SECRET_KEY'] = 'FIFADSE2022GGLOLXD2022'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECRET_KEY'] = 'FIFADSE2022GGLOLXD2022'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql:///root:"no password"@localhost:3306/dsefifa'
#     app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://tanjimflask:tanjimflask@localhost/dsefifa"
    #app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://tanjimre_primeparkuser:cff70978c4053@cpanel.tanjimreza.me:3306/tanjimre_dsefifa"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://tanjimre_primeparkuser:cff70978c4053@server-arizona-vps.quattic.com:3306/tanjimre_dsefifa"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root@localhost/nvms"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://tanjimre_primeparkuser:cff70978c4053@bdix.thedhaka.host:3306/nvms"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://fahadalm_nvms:dkh324As32@bdix.thedhaka.host:3306/fahadalm_nvms"

    # app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://fahadalm_test:Test007Test43@103.112.63.34/fahadalm_test"

    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    
    mail= Mail(app)
    app.config['MAIL_SERVER']='mail.kharapstudent.xyz'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'nvms@kharapstudent.xyz'
    app.config['MAIL_PASSWORD'] = 'dp8cZX]z%7*f'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)

    from .views import views
    from .auth import auth
    from .hospitals import hospitals
    from .admin import admin
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(hospitals, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    
    from .models import RegularUser,\
                        Hospital, \
                        Vaccine, \
                        UserVaccineInfo, \
                        VaccineRequest, \
                        NationalSystem
    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(email):
        # print(f"\
        #     :::::::  Loading user :::::::\n\
        #     {email=}\n\
        #     {email.split('@')[1]=}\n\n\
        #     ") 
        if email.split('@')[1] == 'admin.com':
            # print(f"Admin User Detected! Loading {email} from National System")
            user = NationalSystem.query.filter_by(email=email).first()
            # print(f"Loaded: {user}")
            return user
        if email.split('@')[1] == 'hospital.com':
            # print(f"Hospital User Detected! Loading {email} from Hospital")
            user = Hospital.query.filter_by(email=email).first()
            # print(f"Loaded: {user}")
            return user
        else:
            # print(f"Regular User Detected! Loading {email} from Regular User")
            user = RegularUser.query.filter_by(email=email).first()
            # print(f"Loaded: {user}")
            return user        
    
    return app
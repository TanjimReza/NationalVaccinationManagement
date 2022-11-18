from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

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
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://tanjimre_primeparkuser:cff70978c4053@server-arizona-vps.quattic.com:3306/tanjimre_dsefifa"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://tanjimflask:tanjimflask@localhost/nvms"


    db.init_app(app)
    migrate = Migrate(app, db)

    
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import RegularUser,\
                        Hospital, \
                        Vaccine, \
                        User_Vaccine_Info, \
                        Vaccine_Request, \
                        NationalSystem
    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(email):
        print(f"\
            :::::::  Loading user :::::::\n\
            {email=}\n\
            {email.split('@')[1]=}\n\n\
            ") 
        if email.split('@')[1] == 'admin.com':
            print(f"Admin User Detected! Loading {email} from National System")
            user = NationalSystem.query.filter_by(email=email).first()
            print(f"Loaded: {user}")
            return user
        if email.split('@')[1] == 'hospital.com':
            print(f"Hospital User Detected! Loading {email} from Hospital")
            user = Hospital.query.filter_by(email=email).first()
            print(f"Loaded: {user}")
            return user
        else:
            print(f"Regular User Detected! Loading {email} from Regular User")
            user = RegularUser.query.filter_by(email=email).first()
            print(f"Loaded: {user}")
            return user        
    return app
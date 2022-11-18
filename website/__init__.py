from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


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
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://tanjimre_primeparkuser:cff70978c4053@server-arizona-vps.quattic.com:3306/tanjimre_dsefifa"


    db.init_app(app)
    

    
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Winners
    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    
    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()



app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfasfashthahsdfdsgd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web.db'

bcrypt = Bcrypt(app)


from web.views import views


app.register_blueprint(views, url_prefix='/')
db.init_app(app)



with app.app_context():
    db.create_all()



    

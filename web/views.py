from flask import Blueprint, render_template, request
from web.forms import RegistrationForm
from web.models import User
from web.init import db
from web.init import bcrypt

views = Blueprint('views', __name__,)





@views.route('/')
def home():
    return render_template('index.html')

@views.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data and form.email.data and form.username.data:
            print(form.password.data)
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            new_user = User(name=form.username.data,  email=form.email.data, password=hashed_password)
            print(new_user)
            db.session.add(new_user)
            db.session.commit()
    return render_template('register.html', form=form)

@views.route('/login/', methods=['GET', 'POST'])
def log_in():




    return render_template('login.html')

@views.route('/posts/')
def ps():
    return render_template('post.html')
    
        


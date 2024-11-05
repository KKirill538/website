from web.init import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), unique=False, nullable=False)

    def __repr__(self):
        return f'user({self.id}, {self.name}, {self.email})'



    
    
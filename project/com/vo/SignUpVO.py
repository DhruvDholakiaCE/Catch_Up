from project import db
from project.com.vo.LoginVO import LoginVO

class SignUpVO(db.Model):
    __tablename__ = "signupmaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column('firstname', db.String(30), nullable=False)
    lastname = db.Column('lastname', db.String(30), nullable=False)
    gender = db.Column('gender', db.String(20), nullable=False)
    category = db.Column('category', db.String(20), nullable=False)
    signup_LoginId = db.Column('signup_LoginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'gender': self.gender,
            'category': self.category,
            'signup_loginId': self.signup_LoginId
        }


db.create_all()

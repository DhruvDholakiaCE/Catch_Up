from project import db
from project.com.vo.LoginVO import LoginVO

class PersonalVO(db.Model):
    __tablename__ = "personalmaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    description = db.Column('description', db.String(200))
    contact_number = db.Column('contact_number', db.String(20))
    contact_email = db.Column('contact_email', db.String(50))
    address = db.Column('address', db.String(200))
    
    personal_loginId = db.Column('personal_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'description': self.description,
            'contact_number': self.contact_number,
            'contact_email': self.contact_email,
            'address': self.address,
            'personal_loginId':self.personal_loginId
        }

db.create_all()

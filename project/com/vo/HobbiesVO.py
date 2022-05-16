from project import db
from project.com.vo.LoginVO import LoginVO

class HobbiesVO(db.Model):
    __tablename__ = "hobbiesmaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    hobbies = db.Column('hobbies',db.String(20))
    hobbies_loginId = db.Column('hobbies_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'hobbies': self.hobbies,
            'hobbies_lognId': self.hobbies_loginId
        }

db.create_all()

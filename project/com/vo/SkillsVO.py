from project import db
from project.com.vo.LoginVO import LoginVO

class SkillsVO(db.Model):
    __tablename__ = "skillsmaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    skills = db.Column('skills',db.String(20))
    skills_loginId = db.Column('skills_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'skills': self.skills,
            'skills_loginId': self.skills_loginId
        }

db.create_all()

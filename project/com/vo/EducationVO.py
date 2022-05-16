from project import db
from project.com.vo.LoginVO import LoginVO


class EducationVO(db.Model):
    __tablename__ = "edumaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    degree_name = db.Column('degree_name', db.String(100), nullable=False)
    institution_name = db.Column('institution_name', db.String(100), nullable=True)
    start_date = db.Column('start_date', db.Integer, nullable=False)
    end_date = db.Column('end_date', db.Integer, nullable=True)
    cgpa = db.Column('cgpa', db.Numeric, nullable=True)
    education_loginId = db.Column('education_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'degree_name': self.degree_name,
            'institution_name': self.institution_name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'cgpa': self.cgpa,
            'education_loginId': self.education_loginId
        }


db.create_all()

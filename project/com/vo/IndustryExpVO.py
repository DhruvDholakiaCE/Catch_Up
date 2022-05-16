from project import db
from project.com.vo.LoginVO import LoginVO

class IndustryVO(db.Model):
    __tablename__ = "industrymaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column('company_name',db.String(70))
    designation = db.Column('designation',db.String(50))
    work_description = db.Column('work_description',db.String(500))
    no_of_months = db.Column('no_of_months', db.Integer)
    industry_loginId = db.Column('industry_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'company_name': self.company_name,
            'designation': self.designation,
            'work_description': self.work_description,
            'no_of_months': self.no_of_months,
            'industry_loginId': self.industry_loginId
        }

db.create_all()

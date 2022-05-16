from project import db
from project.com.vo.LoginVO import LoginVO

class ProjectVO(db.Model):
    __tablename__ = "projectsmaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    project_title = db.Column('project_title',db.String(100))
    project_detail = db.Column('project_detail',db.String(500))
    project_loginId = db.Column('project_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'project_title': self.project_title,
            'project_detail': self.project_detail,
            'project_loginId': self.project_loginId
        }

db.create_all()

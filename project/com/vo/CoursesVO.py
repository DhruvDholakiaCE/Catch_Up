from project import db
from project.com.vo.LoginVO import LoginVO

class CoursesVO(db.Model):
    __tablename__ = "coursemaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    department = db.Column('department', db.String(10), nullable=False)
    course_no = db.Column('course_no', db.Integer, nullable=False)
    course_loginId = db.Column('course_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'department': self.department,
            'course_no': self.course_no,
            'course_loginId': self.course_loginId
        }

db.create_all()

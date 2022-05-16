from project import db
from project.com.vo.CoursesVO import CoursesVO


class CoursesDAO:
    # insert into database
    def insertCourses(self, coursesVO):
        db.session.add(coursesVO)
        db.session.commit()

    # fetch records from database
    def fetchCourses(self, coursesVO):
        courses_list = CoursesVO.query.filter_by(course_loginId=coursesVO.course_loginId).all()
        return courses_list

    # delete records from database
    def deleteCourses(self, coursesVO):
        CoursesVO.query.filter_by(Id=coursesVO.Id).delete()
        db.session.commit()

    def updateCourses(self, coursesVO):
        db.session.merge(coursesVO)
        db.session.commit()

    def fetchOtherCourses(self, coursesVO):
        course_list = db.session.query(CoursesVO).filter(CoursesVO.course_loginId != coursesVO.course_loginId).all()
        return course_list

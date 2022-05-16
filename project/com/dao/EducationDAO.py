from project import db
from project.com.vo.EducationVO import EducationVO

class EducationDAO:
    def insertEducation(self, educationVO):
        db.session.add(educationVO)
        db.session.commit()

    def fetchEducation(self, educationVO):
        edu_list = EducationVO.query.filter_by(education_loginId = educationVO.education_loginId).all()
        return edu_list

    def updateEducation(self, educationVO):
        education_list = EducationVO.query.filter_by(Id = educationVO.Id).first()
        education_list.degree_name = educationVO.degree_name
        education_list.institution_name = educationVO.institution_name
        education_list.start_date = educationVO.start_date
        education_list.end_date = educationVO.end_date
        education_list.cgpa = educationVO.cgpa
        education_list.education_loginId = educationVO.education_loginId
        db.session.commit()

    def fetchUserInfo(self, educationVO):
        edu_list = EducationVO.query.filter(EducationVO.education_loginId != educationVO.education_loginId).all()
        return edu_list



from project import db
from project.com.vo.CoursesVO import CoursesVO
from project.com.vo.CertificatesVO import CertificatesVO
from project.com.vo.HobbiesVO import HobbiesVO
from project.com.vo.EducationVO import EducationVO
from project.com.vo.ProjectVO import ProjectVO
from project.com.vo.PersonalVO import PersonalVO
from project.com.vo.SkillsVO import SkillsVO
from project.com.vo.IndustryExpVO import IndustryVO
from project.com.vo.SignUpVO import SignUpVO

from sqlalchemy import func
class ProfileDAO:
    def getProfileInfo(self, k, loginVO):

        VOs = [SignUpVO]
        VOs += [type(i) for i in k]
        base_query = db.session.query(*VOs)
        filter_params = []
        for i, j in zip(VOs[1:], k):
            if i == HobbiesVO:
                base_query = base_query.join(i, SignUpVO.signup_LoginId == HobbiesVO.hobbies_loginId)
                filter_params.append((i.hobbies, j.hobbies))

            elif i == CoursesVO:
                base_query = base_query.join(i, SignUpVO.signup_LoginId == CoursesVO.course_loginId)
                if j.department:
                    filter_params.append((i.department, j.department))
                if j.course_no:
                    filter_params.append((i.course_no, j.course_no))

            elif i == PersonalVO:
                base_query = base_query.join(i, SignUpVO.signup_LoginId == PersonalVO.personal_loginId)
                filter_params.append((i.firstname, j.firstname))
            elif i == IndustryVO:
                base_query = base_query.join(i, SignUpVO.signup_LoginId == IndustryVO.industry_loginId)
                filter_params.append((i.company_name, j.company_name))
        print(filter_params)

        for i in filter_params:
            base_query = base_query.filter(func.lower(i[0]) == func.lower(i[1]))

        results = base_query.filter(SignUpVO.signup_LoginId != loginVO.Id).all()
        results=[i[0] for i in results]
        return results

    def getOtherProfiles(self, signupVO):
        results = db.session.query(SignUpVO, PersonalVO, EducationVO).join(PersonalVO, SignUpVO.signup_LoginId == PersonalVO.personal_loginId)\
            .join(EducationVO, SignUpVO.signup_LoginId == EducationVO.education_loginId)\
            .filter(SignUpVO.signup_LoginId != signupVO.signup_LoginId).all()
        return results


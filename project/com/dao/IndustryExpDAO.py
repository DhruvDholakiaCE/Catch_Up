from project import db
from project.com.vo.IndustryExpVO import IndustryVO


class IndustryDAO:
    def insertIndustryExp(self, industryVO):
        db.session.add(industryVO)
        db.session.commit()

    def fetchIndustryExp(self, industryVO):
        Experience_list = IndustryVO.query.filter_by(industry_loginId=industryVO.industry_loginId).all()
        return Experience_list

    def updateIndustryExp(self, industryVO):
        Experience_list = IndustryVO.query.filter_by(Id=industryVO.Id).first()
        Experience_list.company_name = industryVO.company_name
        Experience_list.designation = industryVO.designation
        Experience_list.work_description = industryVO.work_description
        Experience_list.no_of_months = industryVO.no_of_months
        db.session.commit()

    def deleteIndustryExp(self, industryVO):
        IndustryVO.query.filter_by(Id=industryVO.Id, industry_loginId=industryVO.industry_loginId).delete()
        db.session.commit()

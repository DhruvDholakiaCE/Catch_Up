from project import db
from project.com.vo.PersonalVO import PersonalVO

class PersonalDAO:
    def insertPersonal(self, personalVO):
        db.session.add(personalVO)
        db.session.commit()

    def fetchPersonal(self, personalVO):
        personal_list = PersonalVO.query.filter_by(personal_loginId = personalVO.personal_loginId).all()
        return personal_list

    def updatePersonal(self, personalVO):
    	Personal_list = PersonalVO.query.filter_by(Id = personalVO.Id).first()
    	Personal_list.description = personalVO.description
    	Personal_list.contact_number = personalVO.contact_number
    	Personal_list.contact_email = personalVO.contact_email
    	Personal_list.address = personalVO.address
    	db.session.commit()

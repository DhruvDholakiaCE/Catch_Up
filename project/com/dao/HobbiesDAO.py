from project import db
from project.com.vo.HobbiesVO import HobbiesVO

class HobbiesDAO:
    def insertHobbies(self, hobbiesVO):
        db.session.add(hobbiesVO)
        db.session.commit()

    def fetchHobbies(self, hobbiesVO):
        hobbies_list = HobbiesVO.query.filter_by(hobbies_loginId = hobbiesVO.hobbies_loginId).all()
        return hobbies_list

    def updateHobbies(self, hobbiesVO):
    	db.session.merge(hobbiesVO)
    	db.session.commit()
    def deleteHobbies(self, hobbiesVO):
        HobbiesVO.query.filter_by(Id=hobbiesVO.Id).delete()
        db.session.commit()

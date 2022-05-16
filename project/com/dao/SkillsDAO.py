from project import db
from project.com.vo.SkillsVO import SkillsVO

class SkillsDAO:
    def insertSkills(self, skillsVO):
        db.session.add(skillsVO)
        db.session.commit()

    def fetchSkills(self, skillsVO):
        skills_list = SkillsVO.query.filter_by(skills_loginId = skillsVO.skills_loginId).all()
        return skills_list

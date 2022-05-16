from project import db
from project.com.vo.LoginVO import LoginVO

class AccountsVO(db.Model):
    __tablename__ = "accountsmaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    platform = db.Column('platfrom',db.String(20))
    link = db.Column('link',db.String(200))
    accounts_loginId = db.Column('accounts_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'platform': self.platform,
            'link': self.link,
            'skills_loginId': self.accounts_loginId
        }

db.create_all()

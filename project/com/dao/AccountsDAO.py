from project import db
from project.com.vo.AccountsVO import AccountsVO


class AccountsDAO:
    # insert into database
    def insertAccounts(self, accountsVO):
        db.session.add(accountsVO)
        db.session.commit()



    # fetch records from database
    def fetchAccounts(self, accountsVO):
        accounts_list = AccountsVO.query.filter_by(accounts_loginId=accountsVO.accounts_loginId).all()
        return accounts_list
    #
    # delete records from database
    def deleteAccounts(self, accountsVO):
        AccountsVO.query.filter_by(Id=accountsVO.Id, accounts_loginId=accountsVO.accounts_loginId).delete()
        db.session.commit()

    def updateAccounts(self, accountsVO):
        db.session.merge(accountsVO)
        db.session.commit()


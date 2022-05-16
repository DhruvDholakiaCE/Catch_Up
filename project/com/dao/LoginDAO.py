from project import db

from project.com.vo.LoginVO import LoginVO

class LoginDAO:
	def insertLogin(self, loginVO):
		db.session.add(loginVO)
		db.session.commit()

	def validateLogin(self, loginVO):
		loginList = LoginVO.query.filter_by(email = loginVO.email, password = loginVO.password)
		return loginList

	def validateUser(self, loginVO):
		loginList = LoginVO.query.filter_by(email = loginVO.email)
		return loginList

	def updatePassword(self, loginVO):
		loginList = LoginVO.query.filter_by(email = loginVO.email).first()
		loginList.password = loginVO.password
		db.session.commit()

	def fetchId(self, loginVO):
		fetchedId = LoginVO.query.filter_by(email = loginVO.email).first()
		return fetchedId.loginId
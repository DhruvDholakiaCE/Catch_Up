from project import db
from project.com.vo.CertificatesVO import CertificatesVO

class CertificatesDAO:
    def insertCertificates(self, certificatesVO):
        db.session.add(certificatesVO)
        db.session.commit()

    def fetchCertificates(self, certificatesVO):
        certificates_list = CertificatesVO.query.filter_by(certificates_loginId = certificatesVO.certificates_loginId).all()
        return certificates_list

    def deleteCertificates(self, certificatesVO):
        CertificatesVO.query.filter_by(Id=certificatesVO.Id, certificates_loginId=certificatesVO.certificates_loginId).delete()
        db.session.commit()

    def upadateCertificates(self, certificatesVO):
        db.session.merge(certificatesVO)
        db.session.commit()

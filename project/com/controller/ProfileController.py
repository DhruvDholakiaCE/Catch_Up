# importing Flask and other modules
from flask import Flask, request, render_template, redirect, url_for, session
from project.com.vo.LoginVO import LoginVO
from project.com.vo.CoursesVO import CoursesVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.CoursesDAO import CoursesDAO
from project.com.vo.EducationVO import EducationVO
from project.com.dao.EducationDAO import EducationDAO
from project.com.vo.CertificatesVO import CertificatesVO
from project.com.dao.CertificatesDAO import CertificatesDAO
from project.com.vo.HobbiesVO import HobbiesVO
from project.com.dao.HobbiesDAO import HobbiesDAO
from project.com.vo.IndustryExpVO import IndustryVO
from project.com.dao.IndustryExpDAO import IndustryDAO
from project.com.vo.PersonalVO import PersonalVO
from project.com.dao.PersonalDAO import PersonalDAO
from project.com.vo.ProjectVO import ProjectVO
from project.com.dao.ProjectDAO import ProjectDAO
from project.com.vo.SkillsVO import SkillsVO
from project.com.dao.SkillsDAO import SkillsDAO
from project.com.vo.SignUpVO import SignUpVO
from project.com.dao.SignUpDAO import SignUpDAO
from project.com.vo.AccountsVO import AccountsVO
from project.com.dao.AccountsDAO import AccountsDAO
from project.com.dao.ProfileDAO import ProfileDAO
from project import app
from project.com.controller.LoginController import userLoginSession

@app.route('/profile', methods=["GET", "POST"])
def userProfile():
    try:
        courseVO = CoursesVO()
        courseDAO = CoursesDAO()
        certificatesVO = CertificatesVO()
        certificatesDAO = CertificatesDAO()
        industryVO = IndustryVO()
        industryDAO = IndustryDAO()

        personalVO = PersonalVO()
        personalDAO = PersonalDAO()
        signupVO = SignUpVO()
        signupDAO = SignUpDAO()

        educationVO = EducationVO()
        educationDAO = EducationDAO()

        projectVO = ProjectVO()
        projectDAO = ProjectDAO()

        hobbiesVO = HobbiesVO()
        hobbiesDAO = HobbiesDAO()

        accountsVO = AccountsVO()
        accountsDAO = AccountsDAO()

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        loginVO.email = session['login_email']
        id = loginDAO.fetchId(loginVO)

        courseVO.course_loginId = id
        lst = courseDAO.fetchCourses(courseVO)
        courses = [i.as_dict() for i in lst]

        certificatesVO.certificates_loginId = id
        lst_certi = certificatesDAO.fetchCertificates(certificatesVO)
        certificates = [i.as_dict() for i in lst_certi]

        industryVO.industry_loginId = id
        lst_industry = industryDAO.fetchIndustryExp(industryVO)
        industryExp = [i.as_dict() for i in lst_industry]

        personalVO.personal_loginId = id
        lst_personal = personalDAO.fetchPersonal(personalVO)
        personal = [i.as_dict() for i in lst_personal]

        signupVO.signup_LoginId = id
        lst_signup = signupDAO.fetchUser(signupVO)
        signup = [i.as_dict() for i in lst_signup]

        educationVO.education_loginId = id
        lst_education = educationDAO.fetchEducation(educationVO)
        education = [i.as_dict() for i in lst_education]

        projectVO.project_loginId = id
        lst_project = projectDAO.fetchProjects(projectVO)
        project = [i.as_dict() for i in lst_project]

        hobbiesVO.hobbies_loginId = id
        lst_hobbies = hobbiesDAO.fetchHobbies(hobbiesVO)
        hobbies = [i.as_dict() for i in lst_hobbies]

        accountsVO.accounts_loginId = id
        lst_accounts = accountsDAO.fetchAccounts(accountsVO)
        accounts = [i.as_dict() for i in lst_accounts]

        if 'currentPage' not in session:
            session['currentPage'] = 'personal_information'

        return render_template("profilesetup_changes.html", title="profileSetup", courses=courses,
                               certificates=certificates, industryExp=industryExp, signup=signup, personal=personal,
                               education=education, projects=project, hobbies=hobbies, accounts=accounts)
    except Exception as ex:
        print(ex)


@app.route('/insertCourse', methods=["GET", "POST"])
def insertCourse():
    courseVO = CoursesVO()
    courseDAO = CoursesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = session['login_email']

    courseVO.course_no = request.form['courseno']
    courseVO.department = request.form['department']
    # courseVO.department = request.args.get('department')
    # courseVO.department = department
    courseVO.course_loginId = loginDAO.fetchId(loginVO)

    courseDAO.insertCourses(courseVO)
    session['currentPage'] = 'education'
    return redirect(url_for("userProfile"))


@app.route('/updateCourse', methods=["GET", "POST"])
def updateCourse():
    courseVO = CoursesVO()
    courseDAO = CoursesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    Id = request.args.get('Id')
    course_no = request.args.get('course_no')
    department = request.args.get('department')
    loginId = loginDAO.fetchId(loginVO)

    courseVO.Id = Id
    courseVO.course_no = course_no
    courseVO.department = department
    courseVO.course_loginId = loginId
    courseDAO.updateCourses(courseVO)
    session['currentPage'] = 'education'
    return redirect(url_for("userProfile"))


@app.route('/deleteCourse', methods=["GET"])
def deleteCourse():
    courseVO = CoursesVO()
    courseDAO = CoursesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = session['login_email']

    courseVO.Id = request.args.get('Id')
    # courseVO.course_no = ""
    # login_id = loginDAO.fetchId(loginVO)
    # courseVO.course_loginId = login_id
    courseDAO.deleteCourses(courseVO)
    session['currentPage'] = 'education'
    return redirect(url_for("userProfile"))


@app.route('/insertCertificates', methods=["POST"])
def insertCertificates():
    certificatesVO = CertificatesVO()
    certificatesDAO = CertificatesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = session['login_email']

    certificatesVO.certificates = request.form['certificates']

    certificatesVO.certificates_loginId = loginDAO.fetchId(loginVO)
    certificatesDAO.insertCertificates(certificatesVO)
    session['currentPage'] = 'skills'

    return redirect(url_for("userProfile"))


@app.route('/updateCertificates', methods=["GET", "POST"])
def updateCertificates():
    certificatesVO = CertificatesVO()
    certificatesDAO = CertificatesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    Id = request.args.get('Id')
    # certificates = request.form['certificate' + str(Id)]
    certificates = request.args.get('certificates')
    loginId = loginDAO.fetchId(loginVO)

    certificatesVO.Id = Id
    certificatesVO.certificates = certificates
    certificatesVO.course_loginId = loginId
    certificatesDAO.upadateCertificates(certificatesVO)
    session['currentPage'] = 'skills'
    return redirect(url_for("userProfile"))


@app.route('/deleteCertificates', methods=["GET"])
def deleteCertificates():
    certificatesVO = CertificatesVO()
    certificatesDAO = CertificatesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = session['login_email']
    Id = request.args.get('Id')
    certificatesVO.Id = Id
    certificatesVO.certificates_loginId = loginDAO.fetchId(loginVO)
    certificatesDAO.deleteCertificates(certificatesVO)
    session['currentPage'] = 'skills'
    return redirect(url_for("userProfile"))


@app.route('/insertIndustryExp', methods=["POST"])
def insertIndustryExp():
    industryVO = IndustryVO()
    industryDAO = IndustryDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = session['login_email']

    industryVO.company_name = request.form['company_name']
    industryVO.designation = request.form['designation']
    industryVO.work_description = request.form['work_description']
    industryVO.no_of_months = request.form['no_of_months']

    # courseVO.department = department
    login_Id = loginDAO.fetchId(loginVO)
    industryVO.industry_loginId = login_Id

    if request.form['Id'] == 'Null':
        industryDAO.insertIndustryExp(industryVO)
    else:
        industryVO.Id = request.form['Id']
        industryDAO.updateIndustryExp(industryVO)

    session['currentPage'] = 'experience'
    return redirect(url_for("userProfile"))


@app.route('/deleteIndustryExp', methods=["GET"])
def deleteIndustryExp():
    industryVO = IndustryVO()
    industryDAO = IndustryDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']
    login_Id = loginDAO.fetchId(loginVO)
    industryVO.industry_loginId = login_Id
    Id = request.args.get('Id')
    industryVO.Id = Id
    industryDAO.deleteIndustryExp(industryVO)
    session['currentPage'] = 'experience'
    return redirect(url_for("userProfile"))


@app.route('/insertPersonalInfo', methods=["POST"])
def insertPersonalInfo():
    personalVO = PersonalVO()
    personalDAO = PersonalDAO()
    signupVO = SignUpVO()
    signupDAO = SignUpDAO()

    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    # Id = request.args.get('Id')
    # course_no = request.form['course_no'+str(Id)]
    # department = request.form['department']
    id = loginDAO.fetchId(loginVO)

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    contact_email = request.form['contact_email']
    contact_number = request.form['contact_number']
    address = request.form['address']
    description = request.form['description']

    signupVO.firstname = firstname
    signupVO.lastname = lastname
    signupVO.signup_LoginId = id
    personalVO.personal_loginId = id
    personalVO.contact_email = contact_email
    personalVO.contact_number = contact_number
    personalVO.address = address
    personalVO.description = description

    if request.form['Id'] == 'Null':
        personalDAO.insertPersonal(personalVO)
    else:
        personalVO.Id = request.form['Id']
        personalDAO.updatePersonal(personalVO)

    signupDAO.updateUser(signupVO)

    session['currentPage'] = 'personal_information'
    return redirect(url_for("userProfile"))


@app.route('/insertEducation', methods=["GET", "POST"])
def insertEducation():
    educationVO = EducationVO()
    educationDAO = EducationDAO()

    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    # Id = request.args.get('Id')
    # course_no = request.form['course_no'+str(Id)]
    # department = request.form['department']
    id = loginDAO.fetchId(loginVO)

    degree_name = request.form['degree_name']
    start_date = request.form['start_date']
    institution_name = request.form['institution_name']
    end_date = request.form['end_date']
    cgpa = request.form['cgpa']

    educationVO.degree_name = degree_name
    educationVO.start_date = start_date
    educationVO.institution_name = institution_name
    educationVO.end_date = end_date
    educationVO.cgpa = cgpa
    educationVO.education_loginId = id

    if request.form['Id'] == 'Null':
        educationDAO.insertEducation(educationVO)
    else:
        educationVO.Id = request.form['Id']
        educationDAO.updateEducation(educationVO)

    session['currentPage'] = 'education'
    return redirect(url_for("userProfile"))


@app.route('/insertProject', methods=["POST"])
def insertProject():
    projectVO = ProjectVO()
    projectDAO = ProjectDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = session['login_email']

    projectVO.project_title = request.form['project_title']
    projectVO.project_detail = request.form['project_detail']
    projectVO.project_loginId = loginDAO.fetchId(loginVO)
    print('=------------------------------')
    print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')

    projectDAO.insertProject(projectVO)
    session['currentPage'] = 'skills'

    return redirect(url_for("userProfile"))


@app.route('/deleteProject', methods=["GET"])
def deleteProject():
    projectVO = ProjectVO()
    projectDAO = ProjectDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']
    login_Id = loginDAO.fetchId(loginVO)
    projectVO.project_loginId = login_Id
    Id = request.args.get('Id')
    projectVO.Id = Id
    projectDAO.deleteProject(projectVO)
    session['currentPage'] = 'skills'
    return redirect(url_for("userProfile"))


@app.route('/updateProject', methods=["GET", "POST"])
def updateProject():
    projectVO = ProjectVO()
    projectDAO = ProjectDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    Id = request.args.get('Id')
    projectVO.project_title = request.args.get('project_title')
    projectVO.project_detail = request.args.get('project_detail')
    projectVO.Id = Id
    loginId = loginDAO.fetchId(loginVO)
    projectVO.project_loginId = loginId
    
    projectDAO.updateProject(projectVO)
    session['currentPage'] = 'skills'
    return redirect(url_for("userProfile"))


@app.route('/insertHobbies', methods=["POST"])
def insertHobbies():
    hobbiesVO = HobbiesVO()
    hobbiesDAO = HobbiesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = session['login_email']

    hobbiesVO.hobbies = request.form['hobbies']
    hobbiesVO.hobbies_loginId = loginDAO.fetchId(loginVO)
    print('=------------------------------')
    print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')

    hobbiesDAO.insertHobbies(hobbiesVO)
    session['currentPage'] = 'skills'

    return redirect(url_for("userProfile"))


@app.route('/deleteHobbies', methods=["GET"])
def deleteHobbies():
    hobbiesVO = HobbiesVO()
    hobbiesDAO = HobbiesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']
    login_Id = loginDAO.fetchId(loginVO)
    hobbiesVO.hobbies_loginId = login_Id
    Id = request.args.get('Id')
    hobbiesVO.Id = Id
    hobbiesDAO.deleteHobbies(hobbiesVO)
    session['currentPage'] = 'skills'
    return redirect(url_for("userProfile"))


@app.route('/updateHobbies', methods=["GET", "POST"])
def updateHobbies():
    hobbiesVO = HobbiesVO()
    hobbiesDAO = HobbiesDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']

    Id = request.args.get('Id')
    hobbiesVO.hobbies = request.args.get('hobbies')
    hobbiesVO.Id = Id
    loginId = loginDAO.fetchId(loginVO)
    hobbiesVO.hobbies_loginId = loginId

    hobbiesDAO.updateHobbies(hobbiesVO)
    session['currentPage'] = 'skills'
    return redirect(url_for("userProfile"))


@app.route('/insertAccount', methods=["GET", "POST"])
def insertAccount():
    accountsVO = AccountsVO()
    accountsDAO = AccountsDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']
    loginId = loginDAO.fetchId(loginVO)

    platform = request.form['platform']
    link = request.form['link']

    accountsVO.platform = platform
    accountsVO.link = link
    accountsVO.accounts_loginId = loginId
    accountsDAO.insertAccounts(accountsVO)
    session['currentPage'] = 'accounts'
    return redirect(url_for("userProfile"))


@app.route('/updateAccounts', methods=["GET", "POST"])
def updateAccounts():
    accountsVO = AccountsVO()
    accountsDAO = AccountsDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()
    loginVO.email = session['login_email']
    loginId = loginDAO.fetchId(loginVO)

    Id = request.args.get('Id')
    platform = request.args.get('platform'+Id)
    link = request.args.get('link'+Id)
    print(id, ' ', platform,' ', link)

    accountsVO.Id = Id
    accountsVO.platform = platform
    accountsVO.link = link
    accountsVO.accounts_loginId = loginId
    accountsDAO.updateAccounts(accountsVO)

    session['currentPage'] = 'accounts'
    return redirect(url_for("userProfile"))


@app.route('/deleteAccounts', methods=["GET"])
def deleteAccounts():
    accountsVO = AccountsVO()
    accountsDAO = AccountsDAO()
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.email = session['login_email']
    Id = request.args.get('Id')
    accountsVO.Id = Id
    accountsVO.accounts_loginId = loginDAO.fetchId(loginVO)
    accountsDAO.deleteAccounts(accountsVO)
    session['currentPage'] = 'acconuts'
    return redirect(url_for("userProfile"))

@app.route('/searchProfile', methods=["POST"])
def searchProfile():
    resultIds = []
    firstname = request.form['firstname']

    if firstname:
        signupVO = SignUpVO()
        signupDAO = SignUpDAO()
        signupVO.firstname = firstname
        listbyname = signupDAO.fetchByName(signupVO)
        listbyname = [i.as_dict() for i in listbyname]
        ids = [i['signup_loginId'] for i in listbyname]
        resultIds += ids
    else:
        skills = request.form['skills']
        course_no = request.form['course_no']
        department = request.form['department']
        company_name = request.form['company_name']
        hobbiesVO = HobbiesVO()
        courseVO = CoursesVO()
        industryVO = IndustryVO()
        VOs = []
        if skills:
            hobbiesVO.hobbies = skills
            VOs.append(hobbiesVO)
        if course_no or department:
            courseVO.course_no= course_no
            if department:
                courseVO.department = department
            VOs.append(courseVO)
        if company_name:
            industryVO.company_name = company_name
            VOs.append(industryVO)


        loginVO = LoginVO()
        loginDAO = LoginDAO()
        loginVO.email = session['login_email']
        loginId = loginDAO.fetchId(loginVO)
        loginVO.Id = loginId
        profileDAO = ProfileDAO()
        filterresults = profileDAO.getProfileInfo(VOs, loginVO)
        filterresults = [i.as_dict() for i in filterresults]
        ids = [i['signup_loginId'] for i in filterresults]
        resultIds += ids
    results = []
    courses = []
    resultIds = set(resultIds)
    for i in resultIds:
        signupVO = SignUpVO()
        signupDAO = SignUpDAO()
        personalVO = PersonalVO()
        personalDAO = PersonalDAO()
        educationVO = EducationVO()
        educationDAO = EducationDAO()
        coursesVO = CoursesVO()
        coursesDAO = CoursesDAO()

        signupVO.signup_LoginId = i
        personalVO.personal_loginId = i
        educationVO.education_loginId = i
        coursesVO.course_loginId = i

        signupInfo = signupDAO.fetchUser(signupVO)
        personalInfo = personalDAO.fetchPersonal(personalVO)
        educationInfo = educationDAO.fetchEducation(educationVO)
        coursesInfo = coursesDAO.fetchCourses(coursesVO)

        if len(signupInfo)!=0 and len(personalInfo)!=0 and len(educationInfo)!=0 and len(coursesInfo)!=0:
            signupInfo = [i.as_dict() for i in signupInfo]
            personalInfo = [i.as_dict() for i in personalInfo]
            educationInfo = [i.as_dict() for i in educationInfo]
            print(signupInfo,personalInfo,educationInfo)

            results.append((signupInfo[0], personalInfo[0], educationInfo[0]))
            coursesInfo = [i.as_dict() for i in coursesInfo]
            courses.append(coursesInfo)

    print(results)
    return render_template("dashboard.html", email=session['login_email'], results = results, courses= courses)

@app.route('/loadDashboard', methods=["GET", "POST"])
def loadDashboard():
    if userLoginSession():
        loginVO = LoginVO()
        loginDAO = LoginDAO()
        loginVO.email = session['login_email']
        loginId = loginDAO.fetchId(loginVO)

        signupVO = SignUpVO()
        signupVO.signup_LoginId = loginId
        profileDAO = ProfileDAO()
        results = profileDAO.getOtherProfiles(signupVO)
        print(results)
        results = [(i[0].as_dict(),i[1].as_dict(),i[2].as_dict()) for i in results]
        print(results)
        coursesVO = CoursesVO()
        coursesDAO = CoursesDAO()
        courses = []
        for i in results:
            coursesVO.course_loginId = i[0]['signup_loginId']
            courses_list= coursesDAO.fetchCourses(coursesVO)
            courses_list = [i.as_dict() for i in courses_list]
            courses.append(courses_list)
        print(courses)

        return render_template("dashboard.html", email=session['login_email'], results = results, courses= courses)
    else:
        return redirect(url_for('userLogin'))

@app.route('/showProfile', methods=["GET", "POST"])
def searchedProfile():
    try:
        courseVO = CoursesVO()
        courseDAO = CoursesDAO()
        certificatesVO = CertificatesVO()
        certificatesDAO = CertificatesDAO()
        industryVO = IndustryVO()
        industryDAO = IndustryDAO()

        personalVO = PersonalVO()
        personalDAO = PersonalDAO()
        signupVO = SignUpVO()
        signupDAO = SignUpDAO()

        educationVO = EducationVO()
        educationDAO = EducationDAO()

        projectVO = ProjectVO()
        projectDAO = ProjectDAO()

        hobbiesVO = HobbiesVO()
        hobbiesDAO = HobbiesDAO()

        accountsVO = AccountsVO()
        accountsDAO = AccountsDAO()

        id = request.args.get('id')


        courseVO.course_loginId = id
        lst = courseDAO.fetchCourses(courseVO)
        courses = [i.as_dict() for i in lst]

        certificatesVO.certificates_loginId = id
        lst_certi = certificatesDAO.fetchCertificates(certificatesVO)
        certificates = [i.as_dict() for i in lst_certi]

        industryVO.industry_loginId = id
        lst_industry = industryDAO.fetchIndustryExp(industryVO)
        industryExp = [i.as_dict() for i in lst_industry]

        personalVO.personal_loginId = id
        lst_personal = personalDAO.fetchPersonal(personalVO)
        personal = [i.as_dict() for i in lst_personal]

        signupVO.signup_LoginId = id
        lst_signup = signupDAO.fetchUser(signupVO)
        signup = [i.as_dict() for i in lst_signup]

        educationVO.education_loginId = id
        lst_education = educationDAO.fetchEducation(educationVO)
        education = [i.as_dict() for i in lst_education]

        projectVO.project_loginId = id
        lst_project = projectDAO.fetchProjects(projectVO)
        project = [i.as_dict() for i in lst_project]

        hobbiesVO.hobbies_loginId = id
        lst_hobbies = hobbiesDAO.fetchHobbies(hobbiesVO)
        hobbies = [i.as_dict() for i in lst_hobbies]

        accountsVO.accounts_loginId = id
        lst_accounts = accountsDAO.fetchAccounts(accountsVO)
        accounts = [i.as_dict() for i in lst_accounts]

        if 'currentPage' not in session:
            session['currentPage'] = 'personal_information'

        return render_template("show_profile.html", title="profileSetup", courses=courses,
                               certificates=certificates, industryExp=industryExp, signup=signup, personal=personal,
                               education=education, projects=project, hobbies=hobbies, accounts=accounts)
    except Exception as ex:
        print(ex)

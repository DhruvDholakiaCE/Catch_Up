from project import app
import unittest



class FlaskTestCases(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.post('/',follow_redirects=True)
        self.assertTrue(response, "/login")

    def test_signup(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertTrue(b'Sign Up' in response.data)

    def test_correct_signup(self):
        tester = app.test_client(self)
        tester.get('/signup', content_type='html/text')
        response = tester.post('/insertUser',
                               data=dict(firstname="admin", lastname="tester", email="admin@uwaterloo00.ca",
                                         password="Abcd1234", confirmpassword="Abcd1234", gender="female",
                                         category="student"), follow_redirects=True)
        
        self.assertTrue(response, "/login")

    def test_incorrect_signup(self):
        tester = app.test_client(self)
        tester.get('/signup', content_type='html/text')
        response = tester.post('/insertUser',
                               data=dict(firstname="admin", lastname="tester", email="admin@uwaterloo00.ca",
                                         password="Abcd1234", confirmpassword="Abcd1234", gender="female",
                                         category="student"), follow_redirects=True)
        self.assertIn(b'User already exists!', response.data)

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Forgot Password?' in response.data)

    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd1234"),
                               follow_redirects=True)
        self.assertTrue(b'Welcome admin@uwaterloo00.ca.', response.data)

    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="tester@uwaterloo00.ca", password="Abcd1234"),
                               follow_redirects=True)
        self.assertIn(b'Login Failed!', response.data)

    def test_forgotPassword(self):
        tester = app.test_client(self)
        response = tester.get('/forgotPassword', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_forgotPassword_loads(self):
        tester = app.test_client(self)
        response = tester.get('/forgotPassword', content_type='html/text')
        self.assertTrue(b'Save' in response.data)

    def test_forgotPassword_change_password(self):
        tester = app.test_client(self)
        response = tester.post('/updatePassword', data=dict(email="admin@uwaterloo00.ca", confirmpswd="Abcd12345"),
                               follow_redirects=True)
        self.assertTrue(response, "/login")

    def test_forgotPassword_no_user_exist(self):
        tester = app.test_client(self)
        response = tester.post('/updatePassword', data=dict(email="admin@uwaterloo009.ca", confirmpswd="Abcd1234"),
                               follow_redirects=True)
        self.assertIn(b'Please enter valid username.',response.data)

    def test_aboutUs(self):
        tester = app.test_client(self)
        response = tester.post('/AboutUs', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_aboutUs_page(self):
        tester = app.test_client(self)
        response = tester.post('/AboutUs', content_type='html/text')
        self.assertTrue(b'About Us' in response.data)

    def test_dashboard(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/loadDashboard', content_type='html/text',follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/loadDashboard', content_type='html/text')
        self.assertTrue(b'Advance Filter' in response.data)

    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/userLogoutSession',follow_redirects=True)
        self.assertTrue(response, "/login")

    def test_profile_setup(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/profile', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_profile_setup_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/profile', content_type='html/text')
        self.assertTrue(b'Profile' in response.data)

    def test_insert_course_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/insertCourse', data=dict(courseno=651,department="ECE"))
        self.assertTrue(response, "/profile")


    def test_delete_course_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/deleteCourse',follow_redirects=True)
        self.assertTrue(response, "/profile")

    def test_insert_certificates_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/insertCertificates', data=dict(certificates="Oracle Java SE 8"))
        self.assertTrue(response, "/profile")

    def test_update_certificates_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/updateCertificates', data=dict(Id=1,certificates="Oracle Java SE 8"))
        self.assertTrue(response, "/profile")

    def test_delete_certificates_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/deleteCertificates',follow_redirects=True)
        self.assertTrue(response, "/profile")

    def test_insert_industry_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/insertIndustryExp', data=dict(company_name="CG",designation="SDE",work_description="SDE",no_of_months=24))
        self.assertTrue(response, "/profile")

    def test_delete_industry_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/deleteIndustryExp', follow_redirects=True)
        self.assertTrue(response, "/profile")

    def test_insert_personal_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/insertPersonalInfo', data=dict(firstname="P",lastname="J",contact_email="p@gmail.com",contact_number="12345",description="hi",address="India"))
        self.assertTrue(response, "/profile")

    def test_insert_education_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/insertEducation', data=dict(Id=1,degree_name="bachelors",start_date=2019,institution_name="college",end_date=2022,cgpa=4))
        self.assertTrue(response, "/profile")

    def test_insert_project_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/insertProject', data=dict(project_title="catch-up",project_detail="flask application"))
        self.assertTrue(response, "/profile")

    def test_update_project_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('updateProject',data=dict(Id=1,project_title="catch-up",project_detail="flask application"))
        self.assertTrue(response, "/profile")

    def test_delete_project_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/deleteProject', follow_redirects=True)
        self.assertTrue(response, "/profile")

    def test_insert_hobbies_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/insertHobbies', data=dict(hobbies="swim"))
        self.assertTrue(response, "/profile")

    def test_update_hobbies_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/updateHobbies', data=dict(Id=1,hobbies="swim"))
        self.assertTrue(response, "/profile")

    def test_delete_hobbies_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/deleteHobbies', follow_redirects=True)
        self.assertTrue(response, "/profile")


    def test_insert_account_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/insertAccount', data=dict(platform="LinkedIn",link="http.com"))
        self.assertTrue(response, "/profile")

    def test_update_account_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/updateAccounts', data=dict(Id=1,platform="LinkedIn",link="http.com"))
        self.assertTrue(response, "/profile")

    def test_delete_account_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="admin@uwaterloo00.ca", password="Abcd12345"),
                               follow_redirects=True)
        response = tester.get('/deleteAccounts', follow_redirects=True)
        self.assertTrue(response, "/profile")


if __name__ == '__main__':
    unittest.main()

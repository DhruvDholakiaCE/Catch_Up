# importing Flask and other modules
from flask import Flask, request, render_template, redirect, url_for, session
from project.com.vo.LoginVO import LoginVO
from project.com.vo.SignUpVO import SignUpVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.SignUpDAO import SignUpDAO
from project.com.controller.LoginController import userLoginSession, userLogoutSession

from project import app



@app.route('/signup', methods=["GET"])
def userSignup():


    try:
        if not userLoginSession():
            return render_template("signup.html", title = "SignUp")
        else:
            return redirect(url_for('loadDashboard'))
    except Exception as ex:
        print(ex)


@app.route('/insertUser', methods=["GET", "POST"])
def signup():
    try:
        if not userLoginSession():
            # getting input with name = lname in HTML form
            firstname = request.form['firstname']
            # getting input with name = lname in HTML form
            lastname = request.form['lastname']
            # getting input with name = fname in HTML form
            email = request.form['email']
            # getting input with name = lname in HTML form
            password = request.form['password']
            # getting input with name = lname in HTML form
            gender = request.form['gender']
            # getting input with name = lname in HTML form
            category = request.form['category']

            loginVO = LoginVO()
            loginDAO = LoginDAO()
            loginVO.email = email
            loginVO.password = password

            # loginDAO.insertLogin(loginVO)
            print("LoginVO inserted")

            signupVO = SignUpVO()
            signupDAO = SignUpDAO()

            signupVO.firstname = firstname
            signupVO.lastname = lastname
            signupVO.gender = gender
            signupVO.category = category

            print(signupVO.signup_LoginId)


            lst = loginDAO.validateUser(loginVO)

            lst = [i.as_dict for i in lst]
            if len(lst) == 0:
                loginDAO.insertLogin(loginVO)
                signupVO.signup_LoginId = loginVO.loginId
                signupDAO.insertUser(signupVO)
                return render_template("login.html", msg1 = "Account created successfully", title = "Login")
            else:
                return render_template("signup.html", msg="User already exists!", title = "SignUp")
        else:
            return redirect(url_for('loadDashboard'))
    except Exception as ex:
        print(ex)

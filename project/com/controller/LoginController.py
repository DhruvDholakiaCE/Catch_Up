# importing Flask and other modules
from flask import Flask, request, render_template, session, url_for, redirect
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO


from project import app


# Flask constructor

# A decorator used to tell the application
# which URL is associated function

@app.route('/', methods=["GET", "POST"])
def userLogin():
    try:
        session.clear()
        return render_template("login.html", title = "Login")
    except Exception as ex:
        print(ex)


@app.route('/login', methods=["GET", "POST"])
def login():
    if not userLoginSession():
        if request.method == "POST":
            # getting input with name = fname in HTML form
            email = request.form['email']
            # getting input with name = lname in HTML form
            password = request.form['password']

            loginVO = LoginVO()
            loginDAO = LoginDAO()

            loginVO.email = email
            loginVO.password = password

            lst = loginDAO.validateLogin(loginVO)
            lst = [i.as_dict for i in lst]
            if len(lst) == 0:
                return render_template("login.html", msg="Login Failed!", title = "Login")
            else:
                session['login_Id'] = loginVO.loginId
                session['login_email'] = loginVO.email
                return redirect(url_for('loadDashboard'))

        return render_template("login.html")
    else:
        return redirect(url_for('loadDashboard'))




@app.route('/userLoginSession')
def userLoginSession():
    try:
        if 'login_Id' and 'login_email' in session:
            return True
        else:
            return False
    except Exception as ex:
        print(ex)


@app.route("/userLogoutSession", methods=['GET'])
def userLogoutSession():
    try:
        session.clear()
        return redirect(url_for('userLogin'))
    except Exception as ex:
        print(ex)

@app.route("/AboutUs", methods=['GET','POST'])
def AboutUs():
    try:
        return render_template('AboutUs.html', title = "About Us")
    except Exception as ex:
        print(ex)


@app.route('/forgotPassword', methods=["GET"])
def forgotPassword():

    try:
        if not userLoginSession():
            return render_template("forgot_password.html", title = "Forgot Password")
        else:
            return redirect(url_for('loadDashboard'))
    except Exception as ex:
        print(ex)


@app.route('/updatePassword', methods=["GET", "POST"])
def updatePassword():
    try:
        if not userLoginSession():
            # getting input with name = fname in HTML form
            email = request.form['email']
            # getting input with name = lname in HTML form
            password = request.form['confirmpswd']
            loginVO = LoginVO()
            loginDAO = LoginDAO()

            loginVO.email = email
            lst = loginDAO.validateUser(loginVO)
            lst = [i.as_dict for i in lst]
            if len(lst) == 0:

                return render_template("forgot_password.html",msg = "Please enter valid username.", title = "Forgot Password")
            else:
                print("___________INSIDE ELSE updatePassword_________")
                loginVO.password = password
                loginDAO.updatePassword(loginVO)
                return render_template("login.html", msg1 = "Password updated successfully.")
        else:
            return redirect(url_for('loadDashboard'))
    except Exception as ex:
        print(ex)

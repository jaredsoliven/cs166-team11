from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def hello_world():
    return render_template('login.html')

@app.route("/index", methods=['GET', 'POST'])
def index_page():
    return render_template('index.html', form=request.form)
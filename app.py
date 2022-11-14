from flask import Flask, redirect, url_for, render_template, request
import mysql.connector

app = Flask(__name__)

dataBase = mysql.connector.connect(
    host="localhost",
    user="okcolumb",
    password="olivia101022",
    database="okcolumb"
)

cursorObject = dataBase.cursor()
  
# creating table
studentRecord = """CREATE TABLE YouAreConnected (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""
  
# table created
cursorObject.execute(studentRecord)
  
# disconnecting from server
dataBase.close()




@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template("login.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template("signup.html")


if __name__ == "__main__":
    app.run()

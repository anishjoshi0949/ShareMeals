from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
import jinja2

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mysql1234'
app.config['MYSQL_DB'] = 'sharemeals'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template("landing_page_donor.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        user = request.form.get('username')
        password = request.form.get('password')
        cur.execute("select * from donor where name = '%s';"%(user))
        data = cur.fetchone()

        if password == data[-1]:
            print("valid successfully")
            return render_template("landing_page_donor.html")

        else:
            return render_template('donor_login.html')

        # print(user)
        # print(password)

    return render_template('donor_login.html')
@app.route('/donate', methods=['GET', 'POST'])
def donate():
    cur = mysql.connection.cursor()
    cur.execute("select * from ngo where reqchk='yes';")
    ngolist = cur.fetchall()


    return render_template("ngo_list.html", ngolist=ngolist)

if __name__ == "__main__":
    app.run(debug=True)

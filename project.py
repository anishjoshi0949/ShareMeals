from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mysql1234'
app.config['MYSQL_DB'] = 'sharemeals'

mysql = MySQL(app)


# @app.route('/', methods=['GET', 'POST'])
# def hello_world():
#     if request.method == 'POST':
#         print(request.form['email'])
        # username = request.form['username']
        # email = request.form['email']
        # pswd = request.form['pswd']
        # contact = request.form['contact']
        # address = request.form['address']
        # conn= mysql.connector.connect(host="localhost", user="root", password= "unlockmysql",database="sharemeals")
        # cur=conn.cursor()
        # # cur = mysql.connection.cursor()
        # cur.execute("insert into donor values('%s','%s','%s','%s','%s')"%(username,address,contact,email,pswd))
        # conn.commit()

    # return 'Hello, World!'
    # return render_template('donor_login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        print(user)
        print(password)
        # username = request.form['username']
        # email = request.form['email']
        # pswd = request.form['pswd']
        # contact = request.form['contact']
        # address = request.form['address']
        # conn= mysql.connector.connect(host="localhost", user="root", password= "unlockmysql",database="sharemeals")
        # cur=conn.cursor()
        # # cur = mysql.connection.cursor()
        # cur.execute("insert into donor values('%s','%s','%s','%s','%s')"%(username,address,contact,email,pswd))
        # conn.commit()

    # return 'Hello, World!'
    return render_template('donor_login.html')


# @app.route('/', methods = ['GET','POST'])
# def login():
#     if request.method=='POST':
#         x  = request.form.get('email')
#         y = request.form.get('pswd')
#         print(x)
#         print(y)
#     return render_template('login.html')


# @app.route('/login', methods = ['GET','POST'])
# def login():

# @app.route('/login', methods = ['GET','POST'])
# def login():

if __name__ == "__main__":
    app.run(debug=True)
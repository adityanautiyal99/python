"""file to reterieve field in database"""
from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'aditya'
app.config['MYSQL_PASSWORD'] = 'Aditya99#'
app.config['MYSQL_DB'] = 'aditya'
mysql = MySQL(app)

@app.route('/')
def users():
    """function to reterieve data from database"""
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM myinfo")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

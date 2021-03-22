"""file to delete field in database"""
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'aditya'
app.config['MYSQL_PASSWORD'] = 'Aditya99#'
app.config['MYSQL_DB'] = 'aditya'
mysql = MySQL(app)

@app.route('/')
def users():
    """function to delete database"""
    name = input("Enter name you want to delete : ")
    number = int(input("Enter phone number of the field you want to delete : "))
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM myinfo WHERE phone=%s AND name=%s", (number, name))
    mysql.connection.commit()
    cur.close()
    return "deleted"

if __name__ == '__main__':
    app.run(debug=True)

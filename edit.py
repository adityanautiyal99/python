"""file to edit database"""
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
    """edit function to change the desired values"""
    name = input("name you want to change : ")
    phone = input("Phone number to match the field to be updated : ")
    cur = mysql.connection.cursor()
    cur.execute("UPDATE myinfo SET name=%s WHERE phone=%s", (name, phone))
    mysql.connection.commit()
    cur.close()
    return "edited"

if __name__ == '__main__':
    app.run(debug=True)

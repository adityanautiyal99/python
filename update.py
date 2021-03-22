"""file to update database"""
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'aditya'
app.config['MYSQL_PASSWORD'] = 'Aditya99#'
app.config['MYSQL_DB'] = 'aditya'
mysql = MySQL(app)

@app.route('/')
def update():
    """function to update the database"""
    # checking if value already exists or not if not then add it to tabel.
    name = input("name you want to add : ")
    phone = int(input("PHone number to be added : "))
    age = int(input(" address to be added : "))
    
    cur = mysql.connection.cursor()
    if cur.execute(f"SELECT * FROM myinfo WHERE phone=2345678"):
        return "ALready exists"
    else:
        cur.execute("INSERT INTO myinfo VALUES (%s, %s, %s)", (name, phone, age))
    mysql.connection.commit()
    cur.close()
    return "Inserted"

if __name__ == '__main__':
    app.run(debug=True)
    update()

import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(email):

	if(re.search(regex,email)):
		print("Valid Email")
	
	else:
		print("Invalid Email")


# Driver Code
if __name__ == '__main__' :

	# Enter the email
	# example email = "ankitrai326@gmail.com"
	email=input()
	# calling run function
	check(email)


#     name = input("name you want to address : ")
#     phone = int(input("PHone number to be added : "))
#     age = int(input(" address to be added : "))


# def users():
#     cur = mysql.connection.cursor()
#     cur.execute("INSERT INTO myinfo VALUES (%s, %s, %s)",('hi', 12345, 21))
#     mysql.connection.commit()
#     cur.close()
#     return "updated"


# def update():
#     # checking if value already exists or not if not then add it to tabel.    
#     if request.method == 'GET':
#         return render_template("create.html")
 
#     if request.method == 'POST':
#         name = request.form['name']
#         phone = request.form['phone']
#         age = request.form['age']
#     cur = mysql.connection.cursor()
#     if cur.execute(f"SELECT * FROM myinfo WHERE phone=12345678"):
#         return "ALready exists"
#     else:
#         cur.execute("INSERT INTO myinfo VALUES (%s, %s, %s)",(name, phone, age))
#     mysql.connection.commit()
#     cur.close()
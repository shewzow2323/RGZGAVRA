# def main():
#     visibleUser = "Anon"
#     visibleUser = session.get("username")
#     conn = psycopg2.connect(
#         host="127.0.0.1",
#         database = "knowledge_base_for_vlad",
#         user = "postgres",
#         password = "postgres",
#         port = 5432
# )
#     cur = conn.cursor()

#     cur.execute("SELECT * FROM users;")

#     result = cur.fetchall()

#     cur.close()
#     conn.close()

#     print(result)

#     return render_template('lab5.html', username = visibleUser)

# def dBConnect():
#     conn = psycopg2.connect(
#         host="127.0.0.1",
#         database = "knowledge_base_for_vlad",
#         user = "postgres",
#         password = "postgres",
#         port = '5432'
# )
#     return conn;

# def dBClose(cursor,connection):
#     cursor.close()
#     connection.close()

# @lab8.route('/lab8/login', methods=['GET', 'POST'])
# def loginPage():
#     errors = []
#     if request.method=='GET':
#         return render_template('login.html', errors=errors)

#     username=request.form.get('username')
#     password=request.form.get('password')

#     if not (username and password):
    
#         errors = []
#         errors = "Заполните все поля"
#         print(errors)
#         return render_template('login.html', errors=errors)

#     conn=dBConnect()
#     cur=conn.cursor()

#     cur.execute(f"SELECT id, password From users where username = '{username}';")
#     result = cur.fetchone()

#     if result is None:
#         errors = []
#         errors = 'Непавильный логин или пароль'
        
#         dBClose(cur,conn)
#         return render_template('login.html', errors=errors)

#     userID, hashPassword = result
    

#     if check_password_hash(hashPassword, password):
#             session['id'] = userID
#             session['username'] = username
#             dBClose(cur,conn)
#             return redirect ("/lab8")

#     else:
#             errors.append("Неправильный логин или пароль")
#             return render_template("login.html", errors=errors)

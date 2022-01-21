from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()
mysql.init_app(app)



@app.route('/')
def index():
    #show all todo's
    cursor = mysql.connection.cursor()
    
    cursor.execute(f"use todo_db;")
    cursor.execute(f"SELECT * FROM `todo`;")
    todo_list = cursor.fetchall()
    cursor.close()
    # print(todo_list)
    return render_template('base.html', todo_list=todo_list)
    

@app.route('/add', methods=['POST'])
def add():
    # add new item
    title = request.form.get("title")
    title1 = str(title)
    if title1 == "":
        return redirect(url_for("index"))
    else:
        cursor = mysql.connection.cursor()
        cursor.execute("use todo_db;")
        cursor.execute ("INSERT INTO `todo`(`title`, `complete`) VALUES (%s, %s)" % (title1, 0))
        mysql.connection.commit()
        cursor.close()
        # new_todo = Todo(title=title,complete=False)
        # db.session.add(new_todo)
        # db.session.commit()
        return redirect(url_for("index"))
        

@app.route("/update/<int:todo_id>")
def update(todo_id):
#     # Update item
    cursor = mysql.connection.cursor()
    cursor.execute("use todo_db;")
    cursor.execute ("UPDATE `todo` SET `complete`= {} Where `id` = {}".format(1,todo_id))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # Update item
    cursor = mysql.connection.cursor()
    cursor.execute("use todo_db;")
    cursor.execute("DELETE FROM `todo` WHERE id = {}".format(todo_id))
    mysql.connection.commit()
    cursor.close()
   
    return redirect(url_for("index"))


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)

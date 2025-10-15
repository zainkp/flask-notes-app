from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'repeat'
app.config['MYSQL_DB'] = 'notesdb'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM notes")
    notes = cur.fetchall()
    cur.close()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
    mysql.connection.commit()
    cur.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_note(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM notes WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
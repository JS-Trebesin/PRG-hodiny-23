import sqlite3, random
from flask import Flask, render_template, request, redirect, url_for, g

app = Flask(__name__)

DATABASE = "instance/database.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as file:
            db.cursor().executescript(file.read())
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
    # db = getattr(g, "_database", None)
    db = get_db()
    if db is not None:
        db.close()


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/bye")
def bye(): 
    return render_template("bye.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        input_class = request.form.get("class")
        message = request.form.get("message")
        grade = random.randint(1,5)

        cursor = get_db().cursor()
        cursor.execute(
            f"INSERT INTO students (student_name, class, student_message, grade) VALUES (?, ?, ?, ?)", 
            (name, input_class, message, grade)
        )

        get_db().commit()


    
    return render_template("form.html")

@app.route("/result")
def result():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    return render_template("result_all.html", rows=rows)

@app.route("/result2")
def result2():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print(rows)
    return render_template("result.html", name=rows[2][1], form_class=rows[2][2], message=rows[2][3])
    # return rows[2][1]

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
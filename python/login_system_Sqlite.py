from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

      
        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )
        user = cursor.fetchone()

        if user:
           
            if user[2] == password:
                message = f"Welcome {username} "
            else:
                message = "Wrong Password "
        else:
            message = "User Not Found "

        conn.close()

    return render_template("login.html", message=message)


app.run(debug=True)

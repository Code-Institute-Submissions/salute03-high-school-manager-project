import os
from flask import (
    Flask, render_template, request, flash, 
    redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_assignments')
def index():
    assignments = list(mongo.db.assignments.find())
    return render_template("index.html", assignments=assignments)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome,{}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or password")
            return redirect(url_for("login"))
    return render_template("login.html", page_title='login')


@app.route("/create_assignment/add", methods=['GET', 'POST'])
def create_assignment():
    if request.method == "POST":
        assignment = {
            "days_name": request.form.get("days_name"),
            "subject_name": request.form.get("subject_name"),
            "topic_name": request.form.get("topic_name"),
            "question": request.form.get("question"),
            "due_date": request.form.get("due_date"),
            "mark": request.form.get("mark"),
            "created_by": session["user"]
        }
        
        mongo.db.assignments.insert_one(assignment)
        flash("Assignments Successfully Added")
        return redirect(url_for("index"))

    days = mongo.db.days.find().sort("days_name", 1)
    return render_template("create_assignment.html", days=days)


@app.route("/edit_assignment/<assignment_id>", methods=["GET", "POST"])
def edit_assignment(assignment_id):
    if request.method == "POST":
        submit = {
            "days_name": request.form.get("days_name"),
            "subject_name": request.form.get("subject_name"),
            "topic_name": request.form.get("topic_name"),
            "question": request.form.get("question"),
            "due_date": request.form.get("due_date"),
            "mark": request.form.get("mark"),
            "created_by": session["user"]
        }
        mongo.db.assignments.update({"_id": ObjectId(assignment_id)}, submit)
        flash("Assignments Successfully Updated")
    
    assignment = mongo.db.assignments.find_one({"_id": ObjectId(assignment_id)})
    days = mongo.db.days.find().sort("days_name", 1)
    return render_template("edit_assignment.html", assignment=assignment, days=days) 


@app.route("/delete_assignment/<assignment_id>")
def delete_assignment(assignment_id):
    mongo.db.assignments.remove({"_id": ObjectId(assignment_id)})
    flash("Assignment Successfully Deleted")
    return redirect(url_for("index"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # reomove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)


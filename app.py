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

DATABASE = "high_school"
COLLECTION = "subjects"


@app.route('/')
@app.route('/get_subjects')
def index():
    subjects = list(mongo.db.subjects.find())
    return render_template("index.html", subjects=subjects)


@app.route("/delete_subject/<subject_id>")
def delete_subject(subject_id):
    print(subject_id)
    mongo.db.subjects.delete_one({"_id": ObjectId(subject_id)})
    print(mongo.db.courses.find_one({"_id": ObjectId(subject_id)}))
    flash("Subject successfully deleted")
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html", page_title='About')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
              request.form["name"]))

    return render_template("contact.html", page_title='Contact')


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


@app.route("/create_subject/add", methods=['GET', 'POST'])
def create_subject():
    if request.method == "POST":
        subjects = {
            "subject_name": request.form.get("subject_name"),
            "subject_number": request.form.get("subject_number"),
            "subject_description": request.form.get("subject_description"),
            "subject_mark": request.form.get("subject_mark"),
            "created_by": session["user"]
        }
        print(subjects)
        mongo.db.subjects.insert_one(subjects)
        flash("Subject Successfully Added")
        return redirect(url_for("index"))

    return render_template("create_subject.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
    # check if username already exists in db
        print(request.form.get("username"))
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username on file")
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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


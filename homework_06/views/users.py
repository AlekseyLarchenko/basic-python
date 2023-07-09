from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, User
import requests

users_app = Blueprint("users_app",
                      __name__, )


@users_app.route("/", endpoint="home")
def index_app():
    return render_template("index.html")


@users_app.route("/users/load", methods=["GET", "POST"], endpoint="load")
def users_load():
    if request.method == "GET":
        return render_template('loaduser.html')

    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = response.json()
    for user_data in users_data:
        name = user_data['name']
        email = user_data['email']
        username = user_data['username']
        user = User(name, email, username)
        db.session.add(user)
        db.session.commit()
    url = url_for("users_app.home")
    flash("Users loaded successfully")
    return redirect(url)


@users_app.route("/users/view", endpoint="view")
def users_view():
    users = db.session.query(User).all()
    return render_template('viewusers.html', users=users)

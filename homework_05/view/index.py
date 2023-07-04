from flask import render_template,Blueprint

index_app = Blueprint('index_app', __name__)


@index_app.route("/")
def app_index():
    return render_template('index.html')


@index_app.route("/about/", endpoint="about")
def app_about():
    return render_template('about.html')


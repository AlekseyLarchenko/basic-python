from flask import Flask
from views.users import users_app
from models import db
from os import getenv
from flask_migrate import Migrate

app = Flask(__name__)
app.register_blueprint(users_app)

config_class_name = getenv("CONFIG_CLASS", "ProductionConfig")
config_object = f'config.{config_class_name}'
app.config.from_object(config_object)

db.init_app(app)
migrate = Migrate(app=app, db=db)

if __name__ == "__main__":
    app.run()

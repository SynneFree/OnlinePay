# from app import routes
# from app import models
from flask import Flask
# from config import Config
from flask_login import LoginManager
if __name__ == '__main__':
    app.run()
app = Flask(__name__)
app.secret_key = 'fbaubfaibiuab21312/f'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'onlinepayment'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config.from_object(Config)

login = LoginManager(app)

from flask import Flask
from flask_json_schema import JsonSchema


app = Flask(__name__)
schema=JsonSchema(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///details.db'


conn = "mysql+pymysql://root:admin@localhost/eunimart"
app.config['SQLALCHEMY_DATABASE_URI'] = conn

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



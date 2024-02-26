from flask import Flask
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite://database.db'

db.init_app(app)

@app.route("/hello", method=["GET"])
def hello_world():
  return "hello somons noie outra ves"


if __name__== '__MAIN__':
  app.run(debug=True)
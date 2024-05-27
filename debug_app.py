from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/tatar/OneDrive/Documents/webScraper/instance/debug_app.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class TestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

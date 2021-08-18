from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///calculator.db"
db = SQLAlchemy(app)


class Arguments(db.Model):
    __tablename__ = "arguments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    value = db.Column(db.Float, nullable=False)


@app.route("/")
def main_page():
    return render_template("main_page.html")


if __name__ == '__main__':
    db.create_all()
    app.run()

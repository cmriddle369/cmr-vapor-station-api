from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_heroku import Heroku 
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://xfmozpoqnagdet:7f2a1ae5ad04e23f3855f26f365346f57c40b13b004fcbb3ad7fbd58739977a3@ec2-52-71-85-210.compute-1.amazonaws.com:5432/d73c8dhaa1ln0j"

db = SQLAlchemy(app)
ma = Marshmallow(app)
heroku = Heroku(app)
CORS(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key =True, unique=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String, nullable=False, unique=False)
    message= db.Column(db.String, nullable=False, unique=False)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "message")

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

@app.route("/contact/post", methods=["POST"])
def create_message():
    if request.content_type != "application/json":
        return jsonify("Error: Data must be sent as JSON.")

    post_data = request.get_json()
    name = post_data.get("name")
    email = post_data.get("email")
    message = post_data.get("message")

    record = Post(name, email, message)
    db.session.add(record)
    db.session.commit()

    return jsonify("Message Created")

@app.route("/contact/get", methods=["GET"])
def get_all_messages():
    all_messages = db.session.query(Post).all()
    return jsonify(post_schema.dump(all_messages))


if __name__ == "__main__":
    app.debug = True
    app.run()
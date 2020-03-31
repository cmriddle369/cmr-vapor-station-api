# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# import os

# app = Flask(__name__)

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
# db = SQLAlchemy(app)
# ma = Marshmallow(app)

# class Form(db.Model):
#     id = db.Column(db.Integer, primary_key =True)
#     name = db.Column(db.String(100), unique=False)
#     email = db.Column(db.String, unique=False)
#     message= db.Column(db.String, unique=False)

#     def __init__(self, name, email, message):
#         self.name = name
#         self.email = email
#         self.message = message

# class FormSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'name', 'email', 'message')

# contact_schema = ContactSchema()
# contacts_Schema = ContactSchema(many=True)

# @app.route('/form', methods=['POST'])
# def add_form():
#     name = request.json['name']
#     email = request.json['email']
#     message = request.json['message']

#     new_form = Form(name, email, message)

#     db.session.add(new_form)
#     db.session.commit()

#     form = Form.query.get(new_form.id)

#     return form_schema.jsonify(form)


# if __name__ == '__main__':
#     app.run(debug=True)
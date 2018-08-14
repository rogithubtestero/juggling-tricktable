from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from bson.objectid import ObjectId



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('tricktable.html')

@app.route('/square/')
def square():
    # num = float(request.form.get('number', 0))
    data = "muffputter"
    return data


@app.route('/add/')
def add():
    return render_template('jsoneditor.html')



#
# @app.route('/')
# def hello_world():
#     message = "nigger"
#     return render_template('tricktable.html', message=message)
#
#
if __name__ == '__main__':
    app.run(debug=True)
#





# this should be an ajax callback:
# thing = db.things.find_one({'_id': ObjectId('4ea113d6b684853c8e000001') })


#
# def import_json():
#
#     from pymongo import MongoClient
#     from bson import json_util
#
#     client = MongoClient()
#     # client = MongoClient('localhost',27017)
#
#     db = client.db
#
#     with open('static/tricktable.json') as f:
#         data = f.read()
#
#     jsondata = json_util.loads(data)
#     db.jugglingtricktable.insert_many(jsondata)
#
#     r = db.jugglingtricktable.find()
#
#     ll = list(r)
#
#
#     with open('out.json', "x") as out:
#         out.write(json_util.dumps(ll))
#
#
#











#
# # This file contains an example Flask-User application.
# # To keep the example simple, we are applying some unusual techniques:
# # - Placing everything in one file
# # - Using class-based configuration (instead of file-based configuration)
# # - Using string-based templates (instead of file-based templates)
#
# from flask import Flask, render_template_string
# from flask_mongoengine import MongoEngine
# from flask_user import login_required, UserManager, UserMixin
#
#
# # Class-based application configuration
# class ConfigClass(object):
#     """ Flask application config """
#
#     # Flask settings
#     SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'
#
#     # Flask-MongoEngine settings
#     MONGODB_SETTINGS = {
#         'db': 'tst_app',
#         'host': 'mongodb://localhost:27017/tst_app'
#     }
#
#     # Flask-User settings
#     USER_APP_NAME = "Flask-User MongoDB App"      # Shown in and email templates and page footers
#     USER_ENABLE_EMAIL = False      # Disable email authentication
#     USER_ENABLE_USERNAME = True    # Enable username authentication
#     USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form
#
#
# def create_app():
#     """ Flask application factory """
#
#     # Setup Flask and load app.config
#     app = Flask(__name__)
#     app.config.from_object(__name__+'.ConfigClass')
#
#     # Setup Flask-MongoEngine
#     db = MongoEngine(app)
#
#     # Define the User document.
#     # NB: Make sure to add flask_user UserMixin !!!
#     class User(db.Document, UserMixin):
#         active = db.BooleanField(default=True)
#
#         # User authentication information
#         username = db.StringField(default='')
#         password = db.StringField()
#
#         # User information
#         first_name = db.StringField(default='')
#         last_name = db.StringField(default='')
#
#         # Relationships
#         roles = db.ListField(db.StringField(), default=[])
#
#     # Setup Flask-User and specify the User data-model
#     user_manager = UserManager(app, db, User)
#
#     # The Home page is accessible to anyone
#     @app.route('/')
#     def home_page():
#         # String-based templates
#         return render_template_string("""
#             {% extends "flask_user_layout.html" %}
#             {% block content %}
#                 <h2>Home page</h2>
#                 <p><a href={{ url_for('user.register') }}>Register</a></p>
#                 <p><a href={{ url_for('user.login') }}>Sign in</a></p>
#                 <p><a href={{ url_for('home_page') }}>Home page</a> (accessible to anyone)</p>
#                 <p><a href={{ url_for('member_page') }}>Member page</a> (login required)</p>
#                 <p><a href={{ url_for('user.logout') }}>Sign out</a></p>
#             {% endblock %}
#             """)
#
#     # The Members page is only accessible to authenticated users via the @login_required decorator
#     @app.route('/members')
#     @login_required    # User must be authenticated
#     def member_page():
#         # String-based templates
#         return render_template_string("""
#             {% extends "flask_user_layout.html" %}
#             {% block content %}
#                 <h2>Members page</h2>
#                 <p><a href={{ url_for('user.register') }}>Register</a></p>
#                 <p><a href={{ url_for('user.login') }}>Sign in</a></p>
#                 <p><a href={{ url_for('home_page') }}>Home page</a> (accessible to anyone)</p>
#                 <p><a href={{ url_for('member_page') }}>Member page</a> (login required)</p>
#                 <p><a href={{ url_for('user.logout') }}>Sign out</a></p>
#             {% endblock %}
#             """)
#
#     return app
#
#
# # Start development web server
# if __name__=='__main__':
#     app = create_app()
#     ## app.run(host='0.0.0.0', port=5000, debug=True)

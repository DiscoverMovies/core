"""
    Copyright (C) 2017 Sidhin S Thomas

    This file is part of discovermovie.

    discovermovies is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    discovermovie is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with discovermovie.  If not, see <http://www.gnu.org/licenses/>.
"""

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
#mail_sender.mail.init_app(app)

db = SQLAlchemy(app=app)


@app.errorhandler(404)
def not_found(status):
    return jsonify(status='error', reason='resource not found', information=str(status))


from discovermovies.core import core
from discovermovies.mod_forums import mod_forums
from discovermovies.mod_movie import mod_movie

app.register_blueprint(core)
app.register_blueprint(mod_forums)
app.register_blueprint(mod_movie)

db.create_all()

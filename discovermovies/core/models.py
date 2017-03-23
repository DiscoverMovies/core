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

from discovermovies import db, app


# Define models

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    verified = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, username, password, email, phone):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.verified = False

    def verify_user(self):
        self.verified = True

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return self.username

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'username': self.username,
        }


class Profile(db.Model):
    __tablename__ = 'Profile'
    username = db.Column(db.String(100), db.ForeignKey('User.username'), primary_key=True)
    #user = db.relationship('User', foreign_keys='Profile.user_id')
    name = db.Column(db.String(500), nullable=False)
    country = db.Column(db.String(2), nullable=True)
    state = db.Column(db.String(2), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    sex = db.Column(db.String(1), nullable=True)
    complete = db.Column(db.Boolean, default=False)

    def __init__(self, username):
        self.username = username
        self.name = ''


    def __str__(self):
        return self.name


class ForumTopic(db.Model):
    __tablename__ = 'ForumTopic'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_username = db.Column(db.String(100), db.ForeignKey('User.username'), primary_key=True)

class ForumReply(db.Model):
    __tablename__ = 'ForumReply'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('ForumTopic.id'))
    text = db.Column(db.Text,nullable=False)
    author_username = db.Column(db.String(100), db.ForeignKey('User.username'), primary_key=True)

class Recommendations(db.Model):
    __tablename__ = 'Recommendation'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey('User.username'), primary_key=True)
    movie_id = db.Column(db.Integer)
    level = db.Column(db.Integer,default=0)

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

import discovermovies
from discovermovies import db
from discovermovies.core import User


class ForumTopic(db.Model):
    __tablename__ = 'ForumTopic'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_username = db.Column(db.String(100), db.ForeignKey('User.username'), primary_key=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'title': self.title ,
            'body' : self.body,
            'author_username': self.author_username
        }

class ForumReply(db.Model):
    __tablename__ = 'ForumReply'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('ForumTopic.id'))
    text = db.Column(db.Text,nullable=False)
    author_username = db.Column(db.String(100), db.ForeignKey('User.username'), primary_key=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'topic_id': self.topic_id ,
            'id': self.id,
            'text': self.text,
            'author_username': self.author_username
        }
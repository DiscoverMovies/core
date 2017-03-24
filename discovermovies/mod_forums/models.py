import discovermovies
from discovermovies import db
from discovermovies.core import User


class ForumTopic(db.Model):
    __tablename__ = 'ForumTopic'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_username = db.Column(db.String(100), db.ForeignKey('discovermovies.core.User.username'), primary_key=True)

class ForumReply(db.Model):
    __tablename__ = 'ForumReply'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('ForumTopic.id'))
    text = db.Column(db.Text,nullable=False)
    author_username = db.Column(db.String(100), db.ForeignKey('User.username'), primary_key=True)
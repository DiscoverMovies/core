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
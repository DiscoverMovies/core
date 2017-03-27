from flask import Blueprint
from flask import request, jsonify

from discovermovies import db
from discovermovies.core.models import User
from discovermovies.mod_forums.models import ForumTopic, ForumReply
from discovermovies.utlils import get_error_json, check_token

forums = Blueprint('forums', __name__)


@forums.route('/forum/get/<int:forum_id>')
def get_forum(forum_id):
    forum = ForumTopic.query.filter_by(id=forum_id).first()
    if forum is None:
        return get_error_json('Forum topic does not exist', 'unknown_resource')
    return jsonify(status='OK', forum=forum.serialize)

@forums.route('/forum/all')
def get_all_forum():
    forum_list = ForumTopic.query.all()
    if forum_list is None:
        return get_error_json('Forum topic does not exist', 'unknown_resource')
    return jsonify(status='OK', forum=[i.serialize for i in forum_list])

@forums.route('/forum/replies/get/<int:forum_id>')
def get_all_replies(forum_id):
    replies = ForumReply.query.filter_by(topic_id=forum_id).all()
    if replies is None:
        return jsonify(status='OK', replies='None')
    return jsonify(status='OK', replies=[i.serialize for i in replies])


@forums.route('/forum/create', methods=['POST'])
def create_forum():
    try:
        username = check_token(request.form['token'])
        if username is None:
            return get_error_json('Invalid token', 'invalid_token')
    except KeyError:
        return get_error_json('Missing token', 'missing_data')
    try:
        title = request.form['title']
        text = request.form['text']
    except KeyError:
        return get_error_json('Missing data', 'missing_data')
    forum = ForumTopic()
    forum.author_username = username
    forum.title = title
    forum.body = text
    db.session.add(forum)
    db.session.commit()
    return jsonify(status='OK')


@forums.route('/forum/delete/<int:forum_id>', methods=['POST'])
def delete_forum(forum_id):
    try:
        username = check_token(request.form['token'])
        if username is None:
            return get_error_json('Invalid token', 'invalid_token')
    except KeyError:
        return get_error_json('Missing token', 'missing_data')

    forum= ForumTopic.query.filter_by(id=forum_id).first()
    if forum is None:
        return get_error_json('No topic corresponding to id','unknown_resource')
    db.session.delete(forum)
    db.session.commit()
    return jsonify(status='OK')


@forums.route('/forum/reply/post/<int:forum_id>', methods=['POST'])
def post_reply(forum_id):
    forum = ForumTopic.query.filter_by(id=forum_id).first()
    if forum is None:
        return get_error_json('No forum found to corresponding id', 'unkown_resource')
    try:
        text = request.form['text']
        username = check_token(request.form['token'])
        if username is None:
            return get_error_json('Invalid token', 'invalid_token')
    except KeyError:
        return get_error_json('Missing data', 'missing_data')
    reply = ForumReply()
    reply.text = text
    reply.author_username = username
    reply.topic_id = forum_id
    db.session.add(reply)
    db.session.commit()
    return jsonify(status='OK')

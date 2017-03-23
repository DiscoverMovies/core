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
import datetime

from flask import Blueprint, jsonify
from flask import request
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from werkzeug.security import check_password_hash, generate_password_hash

from discovermovies import db, app
from discovermovies.core.models import  User, Profile
from discovermovies.utlils import check_token

core = Blueprint("core", __name__)


@core.route('/user/auth', methods=['POST'])
def authenticate_user():
    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError:
        return jsonify(status='error', reason='missing data', code='missing_data')
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify(status='error', reason='incorrect username', code='incorrect_username')
    if check_password_hash(user.password, password):
        token = str(Serializer('1234abcd', expires_in=6000).dumps({'username': user.username}))
        return jsonify(status='OK',token=token)
    else:
        return jsonify(status='error', reason='incorrect password', code='incorrect_password')

@core.route('/user/create', methods=['POST'])
def create_user():
    try:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
    except KeyError:
        return jsonify(status='error',reason='missing data',code='missing_data')
    if User.query.filter_by(username=username).first() is not None:
        return jsonify(status='error',reason='duplicate username', code='duplicate_username')
    user = User(username,generate_password_hash(password),email,phone)
    profile = Profile(username)
    db.session.add(user)
    db.session.add(profile)
    db.session.commit()
    return jsonify(status='OK',token=str(Serializer('12345abcd', expires_in=6000).dumps({'id': user.username})))

@core.route('/user/check',methods=['GET'])
def check_user_exist():
    try:
        username = request.args['username']
    except KeyError:
        return jsonify(status='error', reason='missing data', code='missing_data')
    if User.query.filter_by(username=username).first() is not None:
        return jsonify(status='OK',exists=True)
    return jsonify(status='OK', exists=False)

@core.route('/user/search',methods=['GET'])
def search_user():
    try:
        username = request.args['username']
    except KeyError:
        return jsonify(status='error', reason='missing data', code='missing_data')
    userlist = User.query.filter(User.username.like('%'+username+'%')).all()
    return jsonify(userlist=[i.serialize for i in userlist])

@core.route('/user/data', methods=['GET'])
def get_user_data():
    try:
        username = check_token(request.args['token'])
        print(dict(request.args))
        if username is None:
            return jsonify(status='error',reason='invalid token',code='invalid_token')
    except KeyError:
        return jsonify(status='error',reason='missing token',code='missing_data')
    user = User.query.filter_by(username=username).first()
    profile = Profile.query.filter_by(username=username).first()
    data = {
        'username':user.username,
        'email': user.email,
        'phone': user.phone,
        'verified': user.verified,
        'name':profile.name,
        'sex': profile.sex,
        'dob': profile.date_of_birth,
        'country':profile.country,
        'state': profile.state,
        'complete': profile.complete
    }
    return jsonify(data)


@core.route('/user/update', methods=['POST'])
def update_user_data():
    try:
        print(dict(request.form))
        username = check_token(request.form['token'])
        if username is None:
            return jsonify(status='error',reason='invalid token',code='invalid_token')
    except KeyError:
        return jsonify(status='error',reason='missing token',code='missing_data')
    user = User.query.filter_by(username=username).first()
    profile = Profile.query.filter_by(username=username).first()
    try:
        profile.name = request.form['name']
        profile.sex = request.form['sex']
        profile.date_of_birth = datetime.datetime.strptime(request.form['dob'],'%Y-%m-%d').date()
        profile.country = request.form['country']
        profile.state = request.form['state']
    except KeyError:
        return jsonify(status='error',reason='missing data',code='missing_data')
    profile.complete = True
    db.session.commit()
    return jsonify(status='OK')


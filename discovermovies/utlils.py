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
import smtplib
import threading

from flask import copy_current_request_context
from flask import current_app
from flask import jsonify
from flask import render_template
from flask_mail import Mail, Message
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from discovermovies import app


def check_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None  # valid token, but expired
    except Exception:
        return None  # invalid token
    return data['username']


def get_error_json(reason, code):
    return jsonify(status='error', reason=reason, code=code)


def create_massege(to_email, subject, template, from_email=None, **kwargs):
    if not from_email:
        from_email = current_app.config['ROBOT_EMAIL']
    if not to_email:
        raise ValueError('Target email not defined.')
    body = 'helo'  # render_template(template, site_name=current_app.config['SITE_NAME'], **kwargs)
    subject = subject.encode('utf-8')
    body = body.encode('utf-8')
    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (
        from_email, to_email, subject, datetime.datetime.now(), body)
    return msg


def send_async(to_email, subject, template, from_email=None, **kwargs):
    message = create_massege(to_email, subject, template, from_email, **kwargs)

    @copy_current_request_context
    def send_message(message):
        mailer = smtplib.SMTP()
        mailer.connect('smtp.zoho.com', port=465)
        mailer.login('admin@trymake.com', 'Openshift')
        #TODO
        print(message)
        mailer.send('admin@trymake.com', 'sidhin.thomas@gmail.com', message)

    sender = threading.Thread(name='mail_sender', target=send_message, args=(message,))
    sender.start()

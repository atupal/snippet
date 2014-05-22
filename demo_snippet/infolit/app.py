#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import escape

from flask.ext.sqlalchemy import SQLAlchemy

from datetime import datetime
from functools import wraps
from hashlib import md5

import uuid
import re

app = Flask(__name__)
app.secret_key = uuid.uuid1().hex
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./infolit.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file::memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(80), unique=True)
    username = db.Column(db.Unicode(256), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, uid, username, password):
        self.uid = uid
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r-%r>' % (self.uid, self.username)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer)
    content = db.Column(db.Text)
    time = db.Column(db.DateTime)

    username = db.Column(db.Unicode(256), db.ForeignKey('user.username'))
    user = db.relationship('User',
            backref=db.backref('answers', lazy='dynamic'))

    def __init__(self, question_id, content, time, user):
        self.question_id = question_id
        self.content = content
        self.time = time
        self.user = user

    def __repr__(self):
        return '<%r - %r>' % (self.question_id, self.useruid)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('uid') is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        uid = session['uid']
        user = User.query.filter_by(uid=uid).first()
        answers = user.answers.all()
        if answers:
            return render_template('index.html', question_id=answers[-1].question_id, 
                    content=u'第 %d 题:%s' % (answers[-1].question_id, answers[-1].content))
        return render_template('index.html')
    else:
        uid = session['uid']
        user = User.query.filter_by(uid=uid).first()
        question_id = request.form.get('question_id')
        content = request.form.get('content')

        answer = Answer.query.filter_by(question_id=question_id, username=user.username)
        for ans in answer:
            db.session.delete(ans)
        db.session.add(Answer(question_id, content, datetime.now(), user))
        db.session.commit()
        return render_template('index.html', question_id=(int(question_id)+1)%31, content=u'第 %d 题:%s' % (int(question_id), content))

@app.route('/manage', methods=['GET'])
@login_required
def manage():
    uid = session['uid']
    if uid != 'admin':
        user = User.query.filter_by(uid=uid).first()
        answers = user.answers
    else:
        answers = Answer.query.all()
    return render_template('manage.html', answers=answers)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = escape(request.form.get('id', ''))
        password = escape(request.form.get('password', ''))
        user = User.query.filter_by(uid=id).first()
        if user and md5(password).hexdigest() == str(user.password):
            session['uid'] = id
            session['username'] = str(user.username.encode('utf-8'))
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error=1)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('uid', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'uid' in session:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('register.html')
    else:
        id = request.form.get('id')
        name = request.form.get('name')
        password = request.form.get('password')
        if not re.match('[a-z_A_A0-9]+$', id):
            return render_template('register.html', error=1)
        if not re.match(ur"[\u4e00-\u9fa5]+$", name):
            return render_template('register.html', error=2)
        if len(password) < 4 or len(password) > 100:
            return render_template('register.html', error=3)

        user_by_uid = User.query.filter_by(uid=id).first()
        user_by_name = User.query.filter_by(username=name).first()
        if user_by_uid or user_by_name:
            return render_template('register.html', error=4)

        user = User(id, name, md5(password).hexdigest())
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))


if __name__ == '__main__':
    db.create_all()
    # #admin = User('admin', '管理员'.decode('utf-8'), 'b103b688aefde4784c22ec4423e72e1b')
    #admin = User.query.filter_by(uid='admin').first()
    #answer = Answer(1, '哈哈哈哈哈哈哈哈哈哈'.decode('utf-8'), datetime.now(), admin)
    #db.session.add(answer)
    #db.session.commit()
    app.run('0.0.0.0', port=8080, debug=True)

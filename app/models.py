import sqlite3
from contextlib import closing
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask
from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))

    def __repr__(self):
        return '<User %r>' % self.username


class Entry(db.Model):
    ___tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text,nullable=False)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Entry %r>' % self.title


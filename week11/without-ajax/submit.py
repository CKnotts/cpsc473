#!/usr/bin/env python

from sqlite3 import DatabaseError

from bottle import install, get, post, request, template, run
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='./sqllite.db'))


@get('/')
def index():
    return template('form', result=None)


@post('/')
def query(db):
    query = request.forms.query
    try:
        cur = db.cursor()
        result = cur.execute(query)
        rows = result.fetchall()
        answer = rows
    except DatabaseError, e:
        answer = e.message

    return template('form', result=answer)

run(host='0.0.0.0', port=8080, debug=True, reloader=True)

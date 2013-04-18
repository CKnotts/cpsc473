#!/usr/bin/env python

import os
from sqlite3 import DatabaseError

from bottle import install, get, post, request, template, static_file, run
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='./sqllite.db'))

@get('/')
def index():
    return static_file('form.html', root=root)

@get('/ajax.js')
def js():
    return static_file('ajax.js', root=root)

def html_table(headings, rows):
    html = ['<table border="1">'
            '\t<tr>']

    for heading in headings:
        html.append('\t\t<th>%s</th>' % heading)
    html.append('\t</tr>')

    for row in rows:
        html.append('\t<tr>')
        for col in headings:
            html.append('\t\t<td>%s</td>' % row[col])
        html.append('\t</tr>')

    html.append('</table>')

    return '\n'.join(html)

@post('/')
def query(db):
    query = request.forms.query
    try:
        cur = db.cursor()
        result = cur.execute(query)
        rows = result.fetchall()

        if len(rows) > 0:
            return html_table(rows[0].keys(), rows)
        else:
            return '<p>\nNo rows returned.\n</p>'

    except DatabaseError, e:
        return e.message


root = os.path.dirname(os.path.realpath(__file__))
run(host='0.0.0.0', port=8080, debug=True, reloader=True)


#!/usr/bin/env python

import datetime

from bottle import get, post, request
from bottle import install, run

from bottle_mongo import MongoPlugin
from bson.objectid import ObjectId

# sudo service mongodb start
install(MongoPlugin(uri='localhost', db='discuss', json_mongo=True))


@get('/forums')
def list_forums(mongodb):
    return mongodb.topics.distinct('forum')


@get('/topics/:forum')
def list_topics(mongodb, forum):
    return mongodb.topics.find({'forum': forum}, {'title': 1})


@post('/topics/:forum')
def new_topic(mongodb, forum):
    id = mongodb.topics.insert(
        {'forum': forum,
         'title': request.json['title'],
         'posts': [
             {'user': request.json['user'],
              'text': request.json['text'],
              'date': datetime.datetime.utcnow()}
         ]})
    return {'_id': id}


@get('/topic/:id')
def list_posts(mongodb, id):
    return mongodb.topics.find({'_id': ObjectId(id)})


@post('/topic/:id')
def new_post(mongodb, id):
    mongodb.topics.update(
        {'_id': ObjectId(id)},
        {'$push':
         {'posts':
          {'user': request.json['user'],
           'text': request.json['text'],
           'date': datetime.datetime.utcnow()}}})

run(host='0.0.0.0', port=8080, debug=True, reloader=True)

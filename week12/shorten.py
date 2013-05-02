#!/usr/bin/env python

import random

from bottle import install, get, post, request
from bottle import template, abort, redirect, run
from bottle_redis import RedisPlugin

# sudo service redis-server start
install(RedisPlugin())

INIT_KEY = 10 * 36 ** 3


def next_key(rdb):
    rdb.setnx('next', INIT_KEY)

    incr = random.randint(1, 10)
    value = rdb.incr('next', incr)
    return base36encode(value)


# From http://en.wikipedia.org/wiki/Base_36#Python_Conversion_Code
def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')

    base36 = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36


@get('/')
def index(rdb):
    popular = rdb.zrevrange('hits', 0, 9, withscores=True)

    return template('index', popular=popular)


@post('/')
def shorten(rdb):
    input_url = request.forms.input_url

    scheme, netloc, _, _, _ = request.urlparts
    base_url = '%s://%s/' % (scheme, netloc)

    if input_url.startswith(base_url):
        short = input_url.replace(base_url, '', 1)
        output_url = rdb.get('short:' + short)
    else:
        output_url = rdb.get('long:' + input_url)

    if not output_url:
        key = next_key(rdb)
        output_url = base_url + key

        rdb.set('short:' + key, input_url)
        rdb.setnx('long:' + input_url, output_url)

    popular = rdb.zrevrange('hits', 0, 9, withscores=True)

    return template('index',
        input_url=input_url,
        output_url=output_url,
        popular=popular
    )


@get('/:key')
def follow(rdb, key):
    input_url = rdb.get('short:' + key)
    if not input_url:
        abort(404, 'No such shortened URL')

    output_url = rdb.get('long:' + input_url)
    link = '<a href="%s">%s</a>' % (output_url, input_url)
    rdb.zincrby('hits', link, 1)

    redirect(input_url)


run(host='0.0.0.0', port=8080, debug=True, reloader=True)

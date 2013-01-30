#!/usr/bin/env python

import os
import sys
import pprint

print 'Content-Type: text/plain'
print

print 'os.environ:'
print
for var, val in os.environ.items():
    if len(val) > 80:
        val = val[:80] + '...'
    print '%s=%s' % (var, val)
print

if os.environ['CONTENT_LENGTH']:
    length = int(os.environ['CONTENT_LENGTH'])
else:
    length = 0
print 'sys.stdin:'
print
print sys.stdin.read(length)

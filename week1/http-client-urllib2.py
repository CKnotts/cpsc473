#!/usr/bin/env python

import sys
import urllib2

for url in sys.argv[1:]:
    f = urllib2.urlopen(url)
    print f.info()
    for line in f.readlines():
        print line.rstrip()
    f.close()


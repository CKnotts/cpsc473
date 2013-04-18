#!/usr/bin/env python

import sys
import urllib2
import HTMLParser

class TitleParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            print data

parser = TitleParser()

for url in sys.argv[1:]:
    f = urllib2.urlopen(url)
    parser.feed(f.read())
    f.close()


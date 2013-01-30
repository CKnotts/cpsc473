#!/usr/bin/env python

import BaseHTTPServer

class EchoHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        response = '%s %s %s\n%s' % \
            (self.command, self.path, self.request_version, self.headers)

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        
        self.wfile.write(response)

    def do_POST(self):
        self.do_GET()
        self.wfile.write('\n')

        length = int(self.headers.getheader('Content-Length'))
        self.wfile.write(self.rfile.read(length))

BaseHTTPServer.test(EchoHTTPRequestHandler)


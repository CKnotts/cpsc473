#!/usr/bin/env python

import SocketServer


class HttpRequestHandler(SocketServer.StreamRequestHandler):
    allow_reuse_address = True

    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data:
                print
                break
            print data

endpoint = ('localhost', 8000)
server = SocketServer.TCPServer(endpoint, HttpRequestHandler)
server.serve_forever()

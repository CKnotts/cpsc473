#!/usr/bin/env python

import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
endpoint = ('www.fullerton.edu', 80)
client.connect(endpoint)

client.send("""
GET / HTTP/1.1
Host: localhost:8000
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.56 Safari/537.17
Accept-Language: en-US,en;q=0.8
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3

""")

# Notice that we left out the following header
# Accept-Encoding: gzip,deflate,sdch

while True:
    data = client.recv(1024)
    if not data:
        print
        break
    print data

client.close()

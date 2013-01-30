#!/usr/bin/env python

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
endpoint = ('localhost', 80)
client.connect(endpoint)

client.send("""
""")

while True:
    data = client.recv(1024)
    if not data:
        print
        break
    print data

client.close()


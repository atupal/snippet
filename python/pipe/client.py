# -*- coding: utf-8 -*-

from multiprocessing.connection import Client

address = ('localhost', 8000)

for x in range(0,5):
    conn = Client(address, authkey='secret password')
    conn.send('这是一个美丽的世界')
    print conn.recv_bytes()

    conn.close()

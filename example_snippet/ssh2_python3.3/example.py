# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.dirname( os.path.realpath(__file__) ))

import socket

import libssh2

DEBUG = False

usage = """Do a SSH remote command with username@hostname
Usage: %s <hostname> <username> <password> <command>""" % __file__[__file__.rfind('/')+1:]

def my_print(args):
    if DEBUG: print(args)

class SSHRemoteClient(object):
    def __init__(self, hostname, username, password, port=22):
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port

        self.session = libssh2.Session()
        self.session.set_banner()

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.hostname,self.port))
            self.session.startup(sock)
            my_print(self.session.last_error())
            self.session.userauth_password(self.username,self.password)
            my_print(self.session.last_error())
        except Exception as e:
            print(str(e))
            raise Exception(self.session.last_error())

        self.channel = self.session.open_session()
        my_print(self.session.last_error())

    def execute(self, command="uname -a"):
        buffer = 4096
        rc = self.channel.execute(command)
        my_print(rc)
        while True:
            data = self.channel.read(buffer)
            if data == '' or data is None: break
            my_print(type(data))
            print(data.strip())

        self.channel.close()

    def __del__(self):
        self.session.close()
        my_print(self.session.last_error())

if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            print(usage)
            sys.exit(1)
        src = SSHRemoteClient(sys.argv[1], sys.argv[2], sys.argv[3])
        src.execute(sys.argv[4])
    except Exception as e:
        print(str(e))
    except KeyboardInterrupt as e:
        sys.exit(1)

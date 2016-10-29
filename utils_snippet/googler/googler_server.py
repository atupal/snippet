#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import socket
import urllib2
import ssl
import traceback
import re
import contextlib
import threading

from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
from urllib2 import urlparse

class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.raw_request = request_text
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message

def read_data(connstream):
    ret = ""
    connstream.settimeout(10)
    data = connstream.read(4096)
    ret += data

    temp_request = HTTPRequest(ret)
    if ret.startswith("POST") and ("\r\n\r\n" not in ret or len(ret.split("\r\n\r\n")[1]) < int(temp_request.headers['Content-Length'])):
        connstream.settimeout(1)
        ret += connstream.read(4096)

    connstream.settimeout(10)
    return ret 

#HOST, PORT = '', 8080
HOST, PORT = '', 8081

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)

def proxy(request, rooturl):
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.settimeout(3)
    #wrap_socket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1_2)
    #wrap_socket.connect(("216.58.199.110", 443))
    #wrap_socket.send(request.raw_request)
    #response = wrap_socket.recv(65535)
    #wrap_socket.close()
    #return response.split("\r\n\r\n")


    #req = urllib2.Request("https://www.google.com/search?q=keyword&sourceid=chrome&ie=UTF-8")
    #google_url = "https://www.google.com" + request.path
    google_url = rooturl + request.path

    #if request.path.startswith("/__atupal/"):
        #google_url = "https://" + request.path.replace("/__atupal/", "")

    req = urllib2.Request(google_url)

    #req.add_header('User-Agent', 'Chrome')
    #req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36')

    if 'cookie' in request.headers:
        req.add_header('Cookie', request.headers['cookie'])

    for header in ["User-Agent"]:
        req.add_header(header, request.headers[header])

    req.add_header('Accept-Language', 'en,en-US;q=0.8,zh-CN;q=0.6,zh;q=0.4')
    req.add_header('accept-charset', 'UTF-8')

    with contextlib.closing(urllib2.urlopen(req, timeout=3)) as fd:
        return fd.headers, fd.read()

def remove_bad_headers(headers):
    return str(headers)\
              .replace("Transfer-Encoding: chunked\r\n", "")\
              #.replace("Connection: close\r\n", "Connection: keep-alive\r\n")

def handle_others(headers, response):
    headers_string = remove_bad_headers(headers)

    http_response = """\
HTTP/1.1 200 OK
""" + headers_string + "\r\n" + response

    return http_response

def handle_google(headers, response):
    headers_string = remove_bad_headers(headers)\
                    .replace(".hk", "")\
                    .replace("www.google.com", "vpn.atupal.org")\
                    .replace("google.com", "vpn.atupal.org")

    http_response = """\
HTTP/1.1 200 OK
""" + headers_string + "\r\n" + response

    return http_response\
           .replace("ssl.gstatic.com", "vpn.atupal.org/__atupal/ssl.gstatic.com")\
           .replace("www.gstatic.com", "vpn.atupal.org/__atupal/www.gstatic.com")\
           .replace("apis.google.com", "vpn.atupal.org/__atupal/apis.google.com")\
           .replace("www.google.com.hk", "vpn.atupal.org")\
           .replace("www.google.com", "vpn.atupal.org")

    #connstream.write(http_response.replace("www.google.com", "atupalvpn.cloudapp.net"))
    #connstream.shutdown(socket.SHUT_RDWR)
    #connstream.close()

def handle_youtube(headers, response):
    headers_string = remove_bad_headers(headers)

    http_response = """\
HTTP/1.1 200 OK
""" + headers_string + "\r\n" + response

    http_response = re.sub(r'https://([-a-z0-9]+)\.googlevideo.com', r'https://vpn.atupal.org/__atupal/\1.googlevideo.com', http_response, re.DOTALL)

    return http_response\
           .replace("s.ytimg.com", "vpn.atupal.org/__atupal/s.ytimg.com")\
           .replace("fonts.gstatic.com", "vpn.atupal.org/__atupal/fonts.gstatic.com")\
           .replace("i.ytimg.com", "vpn.atupal.org/__atupal/i.ytimg.com")\
           .replace("yt3.ggpht.com", "vpn.atupal.org/__atupal/yt3.ggpht.com")\
           .replace("pubads.g.doubleclick.net", "vpn.atupal.org/__atupal/pubads.g.doubleclick.net")\
           .replace("securepubads.g.doubleclick.net", "vpn.atupal.org/__atupal/securepubads.g.doubleclick.net")\
           .replace("tpc.googlesyndication.com", "vpn.atupal.org/__atupal/tpc.googlesyndication.com")\
           .replace("s.youtube.com", "vpn.atupal.org/__atupal/s.youtube.com")\
           .replace("googleads.g.doubleclick.net", "vpn.atupal.org/__atupal/googleads.g.doubleclick.net")\
           .replace("redirector.googlevideo.com", "vpn.atupal.org/__atupal/redirector.googlevideo.com")\
           .replace("www.youtube.com", "vpn.atupal.org")

def handle_stackoverflow(headers, response):
    headers_string = remove_bad_headers(headers)

    http_response = """\
HTTP/1.1 200 OK
""" + headers_string + "\r\n" + response

    return http_response\
           .replace("ajax.googleapis.com", "vpn.atupal.org/__atupal/ajax.googleapis.com")\
           .replace("cdn.sstatic.net", "vpn.atupal.org/__atupal/cdn.sstatic.net")\
           .replace("www.stackoverflow.com", "vpn.atupal.org")

passport = ""
with open("./passport") as fd:
    passport = fd.read().strip()
def route(request):
    authenticated = False
    rooturl = 'https://www.google.com'
    if 'cookie' in request.headers:
        google_cookies = []
        for cookie in request.headers['cookie'].strip(';').split(';'):
            key, value = cookie.strip().split('=')[:2]
            if key == 'passport':
                if value == passport:
                    authenticated = True
            elif key == 'rooturl':
                rooturl = urllib2.unquote(value)
            else:
                google_cookies.append(cookie)
        google_cookies_string = ';'.join(google_cookies).replace("vpn.atupal.org", "google.com")
        request.headers['cookie'] = google_cookies_string

    if request.path.rstrip("/") == '/setcookie':
        if request.command == "GET":
            return """\
HTTP/1.1 200 OK

<!doctype html>
<html>
    <body>
        <form action="/setcookie" method="POST">
            <input type="text" name="passport" />
        </form>
    </body>
</html>
"""
        elif request.command == "POST":
            body = request.rfile.read()
            return """\
HTTP/1.1 200 OK
set-cookie:%s; expires=Wed, 26-Apr-2019 10:27:27 GMT; path=/; domain=vpn.atupal.org; HttpOnly

success
""" % body

    if not authenticated and request.path != "/favicon.ico":
        return """\
HTTP/1.1 200 OK

Hello, Hacker!
"""

    if request.path.rstrip("/") == '/setrooturl':
        return """\
HTTP/1.1 200 OK

<!doctype html>
<html>
    <body>
        <form action="/setcookie" method="POST">
            <input type="text" name="rooturl" />
        </form>
    </body>
</html>
"""

    requesturl = rooturl
    if request.path.startswith("/__atupal/"):
        urlparser = urllib2.urlparse.urlparse("https://" + request.path.replace("/__atupal/", ""))
        requesturl = "https://" + urlparser.hostname
        request.path = urlparser.path

    headers, response = proxy(request, requesturl)

    if "google.com" in rooturl:
        return handle_google(headers, response)

    if "youtube.com" in rooturl:
        return handle_youtube(headers, response)

    if "stackoverflow.com" in rooturl:
        handle_stackoverflow(headers, response)

    return handle_others(headers, response)

def listen_on_single_socket(client_connection, client_address):
    try:
        connstream = None
        if client_address[0] == '13.75.0.11':
            return
            #raise Exception("blocked IP")

        connstream = ssl.wrap_socket(client_connection,
                                     server_side=True,
                                     certfile="/home/atupal/chained.pem",
                                     keyfile="/home/atupal/domain.key",
                                     ssl_version=ssl.PROTOCOL_TLSv1_2)
        connstream.settimeout(10)

        while True:
            print(client_address)
            #request = client_connection.recv(4096)
            request = read_data(connstream)
            #print(request)
            if not request:
                return
            request = HTTPRequest(request)

            try:
                response_text = route(request)
            except Exception as ex:
                client_connection.sendall("""\
HTTP/1.1 200 OK

Internal Error!
""")
                print (traceback.format_exc())
                raise ex
            #client_connection.sendall(response_text)
            connstream.write(response_text)
            break

    except Exception as ex:
        print(''.join(['\033[91m', "Exception: ", str(ex), '\033[0m']))
    finally:
        #client_connection.close()
        try:
            if connstream:
                connstream.shutdown(socket.SHUT_RDWR)
                connstream.close()
        except Exception as ex:
            print (traceback.format_exc())
            print(''.join(['\033[91m', "Exception in close ssl socket: ", str(ex), '\033[0m']))
        finally:
            try:
                client_connection.close()
            except Exception as ex:
                print(''.join(['\033[91m', "Exception in close socket: ", str(ex), '\033[0m']))


while True:
    try:
        client_connection, client_address = listen_socket.accept()
        client_connection.settimeout(10)
        #listen_on_single_socket(client_connection, client_address)
        threading.Thread(target = listen_on_single_socket, args = (client_connection, client_address)).start()
    except KeyboardInterrupt:
        exit(0)
    except Exception as ex:
        print(''.join(['\033[91m', "Exception in main loop: ", str(ex), '\033[0m']))
        continue

import tornado
import tornado.ioloop
import tornado.gen
import tornado.httpclient
import pycurl

def prepare_curl_socks5(curl):
    curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)

@tornado.gen.coroutine
def main():
    # set CurlAsyncHTTPClient the default AsyncHTTPClient
    tornado.httpclient.AsyncHTTPClient.configure(
        "tornado.curl_httpclient.CurlAsyncHTTPClient")

    http_client = tornado.httpclient.AsyncHTTPClient()
    http_request = tornado.httpclient.HTTPRequest(
        "https://google.com",
        prepare_curl_callback=prepare_curl_socks5,
        proxy_host="127.0.0.1",
        proxy_port=8087
    )
    response = yield http_client.fetch(http_request)

    print response.body

if __name__ == '__main__':
    tornado.ioloop.IOLoop.instance().run_sync(main)

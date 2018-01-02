# -*- coding: utf-8 -*-

import web

urls = (
    '/', 'hello',
    '/get', 'get'
    )

app = web.application(urls, globals())


class hello:
  def GET(self):
    return '''
    <html>
      <body>
        <form action="/get", method="GET">
          <input name="name" type="text"/>
          <input type="submit"/>
        </form>

        <hr>
        <button id="btn">点击发送get请求</button>
        <script type="text/javascript">
          document.getElementById("btn").onclick = function(){
              document.getElementsByTagName("form")[0].submit();
            };
        </script>

      </body>
    </html>
    '''

class get:
  def GET(self):
    return '''
    <html>
      <body>
        %s
        <hr>

        <form action="/get", method="GET">
          <input name="name" type="text"/>
          <input type="submit"/>
        </form>

        <hr>
        <button id="btn">点击发送get请求</button>
        <script type="text/javascript">
          document.getElementById("btn").onclick = function(){
              document.getElementsByTagName("form")[0].submit();
            };
        </script>

      </body>
    </html>
    ''' % ( 'you input is:%s' % web.input() )


if __name__ == '__main__':
  app.run()

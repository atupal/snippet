#!/usr/bin/env python2

from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO

mytemplate = Template("Hello , ${name}")
buf = StringIO()
ctx = Context(buf, name="atupal")
mytemplate.render_context(ctx)
print buf.getvalue()


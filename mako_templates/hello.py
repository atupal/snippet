#!/urs/bin/env python2

from mako.template import Template

mytemplate = Template("Hello world!")
print mytemplate.render()

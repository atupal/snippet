#!/usr/bin/env python2
from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['./docs'])
mytemplate = Template("""<%include file="header.txt" /> Hello world!""", lookup=mylookup)
print mytemplate.render()

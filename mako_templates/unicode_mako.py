#!/bin/env python2
from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['./docs'], output_encoding='utf-8', encoding_errors="replace")

mytemplate = mylookup.get_template("header.txt")
print mytemplate.render()

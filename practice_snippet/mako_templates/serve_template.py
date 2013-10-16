#!/usr/bin/env python2
from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['./docs'], module_directory='./tmp')

'''
  we can also set the collection size use:
  TemplateLookup(directories=['./docs'], module_directory='./tmp', collection_size=500)
'''

def server_template(templatename, **kwargs):
  mytemplate = mylookup.get_template(templatename)
  print mytemplate.render(**kwargs)

if __name__ == "__main__":
  server_template("header.txt", name="name")

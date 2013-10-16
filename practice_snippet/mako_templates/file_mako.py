#!/urs/bin/env python2
from mako.template import Template

mytemplate = Template(filename="./mytmpl.html", module_directory="./tmp")
print mytemplate.render(name="atupal")

# since we add module_directory fact , it will create source code on the ./tmp
# when call next time it will automatically re-used

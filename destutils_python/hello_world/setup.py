
from distutils.core import setup, Extension

module1 = Extension('demo',
                    sources = ['demo.c'])


setup (name = 'hello_world',
       version = '1.0',
       description = 'this is a demo package',
       ext_modules = [module1])

#from setuptools import setup, Extension
from distutils.core import setup, Extension

setup (
    # Name of this package
    name = "examp",

    # Package version
    version = "0.1",

    # This tells setup how to find our util tests.
    test_suite = "test.examp_unittest",
   
    # Describes how to build the actual extension module from C source files.
    ext_modules = [
        Extension(
          "examp",        # Python name of the module
          ["src/examp.c"] # Source files to build
          )
      ],
    )

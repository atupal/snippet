from setuptools import setup, find_packages

setup(
    name = 'app',
    version = '0.1',
    packages = find_packages(),

    entry_points  = {
      'console_scripts': [
        'func = app.mod:func',
        'error = app.mod:error',
        ]
      }
    )

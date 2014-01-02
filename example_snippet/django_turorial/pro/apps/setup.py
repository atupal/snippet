import os
from setuptols import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djaong-polls',
    version='0.1',
    packages=['polls'],
    include_package_deta=True,
    license='BSD License',
    description='A simple Django app to conduct web-baseed polls',
    long_description=README,
    url='http://www.example.com/',
    author='atupal',
    classifiers=[
      'Environment :: Web Environment',
      'Frameworkd :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Operation System :: OS Independent',
      'Programming language :: Python',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Topic :: Internet :: WWW/HTTP',
      'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
)

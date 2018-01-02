
from the video:http://blip.tv/pycon-us-videos-2009-2010-2011/pycon-2011-reverse-engineering-ian-bicking-s-brain-inside-pip-and-virtualenv-4899496

systemized by [atupal](https://github.com/atupal)

## site-packages ##

### what is site-packages ###

site-package is where third-party installed modules go.

e.g. `/usr/lib/python2.7/site-packages/django` 
(Standard library in `/usr/lib/python2.7`)


### how does it work ###

Python import `site.py` at startup

e.g. `/usr/lib/python2.7/site.py`

e.g. site.py
```python
"""Append module search paths for third-party packages to sys.path.

****************************************************************
* This module is automatically imported during initialization. *
****************************************************************

In earlier versions of Python (up to 1.5a3), scripts or modules that
needed to use site-specific modules would place ``import site''
somewhere near the top of their code.  Because of the automatic
import, this is no longer necessary (but code that does it still
works).

This will append site-specific paths to the module search path.  On
Unix (including Mac OSX), it starts with sys.prefix and
sys.exec_prefix (if different) and appends
lib/python<version>/site-packages as well as lib/site-python.
On other platforms (such as Windows), it tries each of the
prefixes directly, as well as with lib/site-packages appended.  The
resulting directories, if they exist, are appended to sys.path, and
also inspected for path configuration files.

A path configuration file is a file whose name has the form
<package>.pth; its contents are additional directories (one per line)
to be added to sys.path.  Non-existing directories (or
non-directories) are never added to sys.path; no directory is added to
sys.path more than once.  Blank lines and lines beginning with
'#' are skipped. Lines starting with 'import' are executed.

For example, suppose sys.prefix and sys.exec_prefix are set to
/usr/local and there is a directory /usr/local/lib/python2.5/site-packages
with three subdirectories, foo, bar and spam, and two path
configuration files, foo.pth and bar.pth.  Assume foo.pth contains the
following:

  # foo package configuration
  foo
  bar
  bletch

and bar.pth contains:

  # bar package configuration
  bar

Then the following directories are added to sys.path, in this order:

  /usr/local/lib/python2.5/site-packages/bar
  /usr/local/lib/python2.5/site-packages/foo

Note that bletch is omitted because it doesn't exist; bar precedes foo
because bar.pth comes alphabetically before foo.pth; and spam is
omitted because it is not mentioned in either path configuration file.

After these path manipulations, an attempt is made to import a module
named sitecustomize, which can perform arbitrary additional
site-specific customizations.  If this import fails with an
ImportError exception, it is silently ignored.

"""
```

## virtualenv from scratch ##

### where does `sys.prefix` come from ###

Python/sysmodule.c

Python/getpath.c

If PYTHONHOME is set  that's sys.prefix

otherwhise sratr from the location of the Python binary, search upwards.

At each step, look for `lib/pythonX.X/os.py`

if it exists, we've found `sys.prefix`

if we never find it, fallback on hardcodeed --prefix from build.


### copy the python binary ###

create the landmark


fix sys.prefix

```shell
mkdir -p lib/python2.7
touch lib/python2.7/os.py
```

fix sys.exec_prefix

```shell
mkdir lib/python2.7/lib-dynload
```


we can copy the entire stdlib (include site.py) into our lib/python2.7


Works, but heavy



### bootstrap like a virtualenv ###
Write `orig-prefix.txt` to `lib/python2.7`

Contains the system Python's `sys.prefix`

Place our own, modified `site.py` in `lib/python2.7`

Our `site.py` reads `orig-prefix.txt` and adds system stdlib paths to sys.path

```
$ tree
.
├── bin
│   ├── python -> /home/atupal/src/github/snippet-git/python_snippet/virtualenv_from_scratch/scratch/bin/python2.7
│   └── python2.7
└── lib
    └── python2.7
        ├── lib-dynload
        └── os.py
        └── site.py
        └── orig-prefix.txt
```


## What about `bin/activate` ##

A shell convenience only.

Adds the virtualenv's `bin/` to the front of your shell `PATH`


### sometime you can't use the virtualenv's binary. Faking it ###

```python
import sys
sys.path.insert(0,
  "/path/to/venv/lib/python2.7/site-packages")

import site
site.addsitedir(
  "/path/to/venv/lib/python2.7/site-packages")

execfile("/path/to/venv/bin/activate_this.py")

```

## other approach ##
- rvirtualenv
- pythonv


## Pip's dirty little secret ##

Pip doesn't install packages at all

### install like pip ###
```shell
python -c
  "import setuptools;__file__=/p/to/setup.py;execfile(__file__)"
  install
  --single-version-externally-managed
  --record /tmp/pip-ZgGVWG-record/install-record.txt
```


setuptools workd by monkeypatching the builtin distutils

Thus, importing setuptools is enough to active its features.

This hack allows pip to do setuptools-only things (generate .egg-info metadata,
develop/editable installs) on all projects, even those that stick to pure distutils in 
their setup.py

### use pip api ###

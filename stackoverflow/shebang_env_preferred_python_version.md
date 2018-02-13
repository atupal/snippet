

link: http://stackoverflow.com/questions/18993438/shebang-env-preferred-python-version


```sh
#!/bin/sh
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''
```

```sh
#!/bin/bash
pfound=false; v0=2; v1=6
for p in /{usr/,}bin/python*; do  
  v=($(python -V 2>&1 | cut -c 7- | sed 's/\./ /g'))
  if [[ ${v[0]} -eq $v0 && ${v[1]} -eq $v1 ]]; then pfound=true; break; fi
done
if ! $pfound; then echo "no suitable python version (2.6.x) found."; exit 1; fi
$p - $* <<EOF

PYTHON SCRIPT GOES HERE

EOF
```

```sh
#!/bin/sh
''''exec python -u -- "$0" ${1+"$@"} # '''
```

```sh
#!/bin/sh
''':'
exec python -tt "$0" "$@"
'''
# The above shell shabang trick is more portable than /usr/bin/env and supports adding arguments to the interpreter (python -tt)
```

link: http://stackoverflow.com/questions/12070516/conditional-shebang-line-for-different-versions-of-python?lq=1

```sh
#!/bin/sh
# -*- mode: Python -*-

""":"
# bash code here; finds a suitable python interpreter and execs this file.
# prefer unqualified "python" if suitable:
python -c 'import sys; sys.exit(not (0x020500b0 < sys.hexversion < 0x03000000))' 2>/dev/null \
    && exec python "$0" "$@"
for pyver in 2.6 2.7 2.5; do
    which python$pyver > /dev/null 2>&1 && exec python$pyver "$0" "$@"
done
echo "No appropriate python interpreter found." >&2
exit 1
":"""

import sys
print sys.version
```

link: https://github.com/apache/cassandra/blob/trunk/bin/cqlsh

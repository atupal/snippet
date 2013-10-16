
ret = {}

import json

with open('result.raw') as fi:
  for line in fi:
    ind, l_r = line.strip().split(':')
    ret[ind] = {
        'right': l_r.split(',')[0],
        'left': l_r.split(',')[1]
        }

with open('result.json', 'w') as fi:
  fi.write(json.dumps(ret, indent=2))

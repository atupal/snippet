import requests
import json
from pprint import pprint
import time


s = requests.Session()
s.auth = ('atupal', 'TEtZczQ2OTAxMDI='.decode('base64'))

base_url = 'https://api.github.com'

# get sha
url = base_url + '/repos/atupal/github_api_test/branches'
r = s.get(url)
d = json.loads(r.content)
sha = d[0].get('commit').get('sha')
old_commit_sha = sha
pprint (d)
print 'get commit sha:', sha
branch = d[0].get('name')

def wrap_url(url):
  return url.replace(':repo', 'github_api_test').replace(':owner', 'atupal').replace(':sha', sha)

# get commit, tree sha
url = base_url + '/repos/:owner/:repo/git/commits/:sha'
url = wrap_url(url)
r = s.get(url)
d = json.loads(r.content)
sha = d.get('tree').get('sha')
old_tree_sha = sha
pprint (d)
print 'get tree sha:', sha

# get trees
url = base_url + '/repos/:owner/:repo/git/trees/:sha'
url = wrap_url(url)
r = s.get(url)
d = json.loads(r.content).get('tree')
for i in d:
  if i.get('path') == 'a_file':
    sha = i.get('sha')
    print 'get blob sha:', sha
    break
pprint (d)
print 'get the tree sha:', sha

# get a blob
url = base_url + '/repos/:owner/:repo/git/blobs/:sha'
url = wrap_url(url)
r = s.get(url)
d = json.loads(r.content)
pprint (d)
print 'get blob content:', d.get('content').decode('base64')


# create a new blob
url = base_url + '/repos/:owner/:repo/git/blobs'
url = wrap_url(url)
d = {
    'content': d.get('content').decode('base64') + 'new content:%d' % (int(time.time()) % 100),
    'encoding': 'utf-8'
    }
r = s.post(url, data=json.dumps(d))
d = json.loads(r.content)
sha = d.get('sha')
pprint (d)
print 'create a new blob:', sha

# create a new tree
url = base_url + '/repos/:owner/:repo/git/trees'
url = wrap_url(url)
d = {
    'base_tree': old_tree_sha,
    'tree': [
      {
        'path': 'a_file',
        'mode': '100644',
        'type': 'blob',
        'sha': sha
        }
      ]
    }
r = s.post(url, data=json.dumps(d))
d = json.loads(r.content)
sha = d.get('sha')
pprint (d)
print 'create a new tree'

# create a commit
url = base_url + '/repos/:owner/:repo/git/commits'
url = wrap_url(url)
d = {
    'message': 'commit from bot :-)',
    'author': {
      'name': 'atupal',
      'email': 'atupalykl@gmail.com'
      #'date': '2008-07-09T16:13:30+12:00'
      },
    'parents': [
      old_commit_sha
      ],
    'tree': sha
    }
r = s.post(url, data=json.dumps(d))
d = json.loads(r.content)
sha = d.get('sha')
pprint (d)
print 'create a  new commit'

# update the reference of master branch
url = base_url + '/repos/:owner/:repo/git/refs/' + 'heads/' + branch
url = wrap_url(url)
d = {
    'sha': sha,
    'force': True
    }
r = s.patch(url, data=json.dumps(d))
d = json.loads(r.content)
pprint (d)
print 'update a ref:'

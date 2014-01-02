#!/usr/bin/env python2

s = [
[114],
[105, 143],
[120, 182, 116],
[135, 151, 196, 182],
[194, 132, 152, 103, 199],
[133, 187, 103, 141, 140, 181],
[161, 101, 156, 196, 131, 148, 114],
[156, 183, 192, 110, 111, 179, 158, 137],
[129, 114, 103, 174, 191, 108, 158, 144, 115],
[113, 195, 179, 158, 200, 147, 189, 132, 140, 188],
[153, 114, 122, 113, 154, 147, 107, 121, 150, 183, 159],
[137, 101, 124, 112, 111, 126, 168, 117, 130, 188, 136, 102],
]

n = len(s)

dp = [ [-1] * (i+1) for i in xrange(n) ]


par = [ [''] * (i+1) for i in xrange(n) ]

for i in xrange(n):
  dp[-1][i] = s[-1][i]

for i in xrange(n-2, -1, -1):
  for j in xrange(i+1):
    if dp[i+1][j] > dp[i+1][j+1]:
      par[i][j] = 'L'
      dp[i][j] = dp[i+1][j] + s[i][j]
    else:
      par[i][j] = 'R'
      dp[i][j] = dp[i+1][j+1] + s[i][j]



from pprint import pprint

pprint( par )


ind = 0

for i in xrange(n):
  print s[i][ind]
  if par[i][ind] == 'R':
    ind += 1

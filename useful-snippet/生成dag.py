"""
生成随机DAG

首先随机生成一个 1 到N 的permutation。这个permutation就是DAG的拓扑序，然后每次随机从前往后连边，
这样就可以保证生成的是一个DAG了。
"""

from random import shuffle as sl
from random import randint as rd

def gn():
    num = rd(1,1000)
    return num
def w2f(f,num,fg):
    f.write(str(num))
    if fg==True:
        f.write('\n')
    else:
        f.write(' ')

def DataMake(c):
    MAXL =100000;
    f = open('data'+str(c)+'.in','w')
    n = 1000
    node = range(1,n+1)
    sl(node)
    sl(node)
    m = rd(1,min(n*n,5000))
    w2f(f,n,0);w2f(f,m,1)
    for i in range(0,m):
        p1 = rd (1,n-1)
        p2 = rd (p1+1,n)
        x = node[p1-1]
        y = node[p2-1]
        l = rd(1,MAXL)
        w = gn()
        w2f(f,x,0);w2f(f,y,0);w2f(f,l,0);w2f(f,w,1)
    k = gn()
    w2f(f,k,1)
    for i in range(0,k):
        w2f(f,gn(),1)
    print n,' node',m,' edges',k,'Queries'
    f.close()

DataMake(1)
print 'Done'

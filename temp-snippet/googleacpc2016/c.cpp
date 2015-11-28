#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int n;
typedef long long ll;

struct node{
  int left;
  int right;
  int val;
} nodes[330000];
int cnt;

char s[40];
void insert(int root, int p, int idx) {
  if (nodes[root].val == 1) return;
  if (p == idx) {
    nodes[root].val = 1;
    return;
  }
  if (s[idx] == 0) {
    if (nodes[root].left == -1) {
      nodes[root].left = cnt++;
    }
    insert(nodes[root].left, p, idx+1);
  } else {
    if (nodes[root].right == -1) {
      nodes[root].right = cnt++;
    }
    insert(nodes[root].right, p, idx+1);
  }

  if (nodes[root].left != -1 && nodes[root].right != -1 &&
      nodes[ nodes[root].left ].val == 1 && nodes[ nodes[root].right ].val == 1) {
    nodes[root].val = 1;
  }
}

void add(ll ip, int p) {
  for (int i = 31; i > -1;  -- i) {
    s[i] = ip%2;
    ip/=2;
  }
  insert(0, p, 0);
}

void output(ll s, int len) {
  s = s << (32-len);
  printf("%lld.%lld.%lld.%lld/%d\n", s/256/256/256, s%(256*256*256)/256/256, s%(256*256)/256, s%256, len);
}

void visit(int root, ll s, int len) {
  if (root==-1)return;
  if (nodes[root].val == 1) {
    output(s, len);
    return;
  }
  visit(nodes[root].left, s*2, len+1);
  visit(nodes[root].right, s*2+1, len+1);
}

void solve() {
  memset(nodes, -1, sizeof(nodes));
  cnt = 1;
  scanf("%d", &n);
  int a[4], p;
  for (int i = 0; i < n; ++ i) {
    scanf("%d.%d.%d.%d/%d", a, a+1, a+2, a+3, &p);
    ll s = 0;
    for (int i = 0; i < 4; ++ i) {
      s = s*256+(ll)a[i];
    }
    add(s, p);
  }
  visit(0, 0, 0);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int cas=1; cas<=T; ++ cas) {
    printf("Case #%d:\n", cas);
    solve();
  }

  return 0;
}


#include <stdlib.h>


int main() {
  int n;

  int fuuuuuuuuuuuck[n];
  int *heheheheheheheh;
  heheheheheheheh = (int *) malloc (888);  // 为了方便观测设置为 888 (4,8的倍数) 了，没用 sizeof.

  int * const nima = (int *) malloc (444);  // 同上
  nima[1] = 1314;


  fuuuuuuuuuuuck[1] = 13;
  heheheheheheheh[1] = 14;

  return 0;
}

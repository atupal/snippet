#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>

int main() {
  pid_t p1,p2;
  p1=fork();
  if(p1!=0) {
    printf("p1 process id is  %d\n",getpid());
    wait();
    system("ps ");
  } else {
    p2=fork();
    if(p2!=0) {
      printf("p2 process id is  %d\n",getpid());
      exit(0);
    } else {
      printf("p3 process id is  %d\n",getpid());
    }
    exit(0);
  }

  return 0;
}

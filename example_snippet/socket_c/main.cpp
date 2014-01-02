#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define MYPORT 8000

#define DEST_IP "125.39.240.113"  // qq.com
#define DEST_PORT 80

#define BACKLOG 10

void bind_to_addr() {
  int sockfd;
  struct sockaddr_in my_addr;

  sockfd = socket(AF_INET, SOCK_STREAM, 0);

  my_addr.sin_family = AF_INET;
  my_addr.sin_port = htons(MYPORT);
  my_addr.sin_addr.s_addr = inet_addr("0.0.0.0");
  memset(&(my_addr.sin_zero), 0, 8);

  bind(sockfd, (struct sockaddr *)&my_addr, sizeof(struct sockaddr));

  listen(sockfd, BACKLOG);

  unsigned int sin_size = sizeof(struct sockaddr_in);
  struct sockaddr_in client_addr;
  int new_fd = accept(sockfd, (struct sockaddr *)&client_addr, &sin_size);
}


void connect_to_addr() {
  int sockfd;
  struct sockaddr_in dest_addr;

  sockfd = socket(AF_INET, SOCK_STREAM, 0);

  dest_addr.sin_family = AF_INET;
  dest_addr.sin_port = htons(DEST_PORT);
  dest_addr.sin_addr.s_addr = inet_addr(DEST_IP);
  memset(&(dest_addr.sin_zero), 0, 8);

  connect(sockfd, (struct sockaddr *)&dest_addr, sizeof(struct sockaddr));

}

int main() {
  bind_to_addr();

  return 0;
}

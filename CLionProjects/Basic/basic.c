#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <signal.h>

void catch_int(int sig_num);

int main() {
  printf( "hello world\n" );
  signal(SIGINT, catch_int);
  for(;;)
    sleep(1);
}

void catch_int(int sig_num){
  printf("Don't do that");
  fflush(stdout);
}
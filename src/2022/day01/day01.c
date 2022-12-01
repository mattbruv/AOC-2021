#include "stdio.h"

extern int part1();
extern int part2();

int main() {

  int p1 = part1();
  printf("%d\n", p1);

  int p2 = part2();
  printf("%d\n", p2);

  return 0;
}
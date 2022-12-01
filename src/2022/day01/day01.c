#include "stdio.h"

#include <time.h>

extern int part1();
extern int part2();

int main() {

  clock_t start, end;
  double cpu_time_used;
  int p1 = 0;

  start = clock();
  for (int i = 0; i < 1000000; i++) {
    p1 = part1();
  }
  end = clock();
  cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC / 1000000;

  printf("%d\n", p1);

  int p2 = part2();
  printf("%d\n", p2);
  printf("Done in %.50f seconds\n", cpu_time_used);

  return 0;
}
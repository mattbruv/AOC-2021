#include <stdio.h>

int foo[2] = {1, 2};
int x = 1;

int main() {
  //
  int *x = &foo[0];

  return *x;
}
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <conio.h>

void osish(int a, int b)
{
  printf("%d ", a);
  if (a == b)
  {
    return;
  }

  osish(a + 1, b);
}

void kamayish(int a, int b)
{
  printf("%d ", a);
  if (a == b)
  {
    return;
  }

  kamayish(a - 1, b);
}

int main()
{
  int a, b;
  scanf("%d", &a);
  scanf("%d", &b);
  if (a < b)
  {
    osish(a, b);
  }
  else if (a > b)
  {
    kamayish(a, b);
  }
}

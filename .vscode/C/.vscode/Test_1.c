#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <conio.h>

int main()
{
  int arr[5][5];
  srand(time(NULL));
  for (int i = 0; i < 5; ++i)
  {
    for (int j = 0; j < 5; ++j)
    {
      arr[i][j] = rand() % 9 + 1;
      printf("%d ", arr[i][j]);
    }
    puts("");
  }

  puts("");

  for (int i = 0; i < 5; ++i)
  {
    for (int j = 0; j < 5; ++j)
    {
      if (i == j || i + j == 5 - 1)
      {
        arr[i][j] = 0;
      }
    }
  }

  for (int i = 0; i < 5; ++i)
  {
    for (int j = 0; j < 5; ++j)
    {
      printf("%d ", arr[i][j]);
    }
    puts("");
  }
}

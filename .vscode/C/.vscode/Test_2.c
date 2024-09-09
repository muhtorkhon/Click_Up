#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <conio.h>

int main()
{
  int arr[10] = {-1, -1, 1, 5, 5, 6, 7, 8, 8};
  int nigga[10];
  int count = 0;
  int key;
  for (int i = 0; i < 10; i++)
  {
    key = 1;
    for (int j = 0; j < count; j++)
    {
      if (arr[i] == nigga[j])
      {
        key = 0;
        break;
      }
    }
    if (key)
    {
      nigga[count] = arr[i];
      count++;
    }
  }
  for (int i = 0; i < count; i++)
  {
    printf("%d ", nigga[i]);
  }
}

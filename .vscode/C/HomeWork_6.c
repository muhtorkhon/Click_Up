#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <conio.h>

void Fifth(int Index, int num, char a[])
{
  int i;
  for (int i = Index; num; ++i, --num)
  {
      printf("%c",a[i]);
  }
}

int main()
{
  int ind, num;
  char a[50];
  printf("Char => ");
  scanf("%[^\n]%*c", a);
  printf("Enter Index: ");
  scanf("%d", &ind);
  printf("Enter Number: ");
  scanf("%d", &num);
  Fifth(ind, num, a);
  // printf("%s", a);
  return 0;
}
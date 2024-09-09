#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <conio.h>

int main()
{
  char let[256] = "";
  scanf("%[^\n]", let);

  for (int i = 0; let[i]; i++)
  {
    if (let[i] == 'a' || let[i] == 'e' || let[i] == 'i' || let[i] == 'u' || let[i] == 'o')
    {
      let[i] = '*';
    }
    else if (let[i] == 'A' || let[i] == 'E' || let[i] == 'I' || let[i] == 'U' || let[i] == 'O')
    {
      let[i] = '*';
    }
  }

  for (int i = 0; let[i]; i++)
  {
    printf("%c", let[i]);
  }
}
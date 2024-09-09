#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <conio.h>
#include <string.h>

int main()
{
  FILE *f = fopen("old.txt", "r");
  FILE *F = fopen("new.txt", "w");

  char word[100];
  while (fscanf(f, "%s", word) != EOF)
  {
    int len = strlen(word);
    if (len % 2 != 0 || isupper(word[0]))
    {
      fprintf(F, "%s ", word);
    }
  }
  fclose(f);
  fclose(F);
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <string.h>

int main()
{
  FILE *inputFile = fopen("text.txt", "w");
  char let[256];
  scanf("%[^\n]", let);
  fwrite(let, 1, strlen(let), inputFile);
  fclose(inputFile);

  FILE *outputFile = fopen("text.txt", "r");
  char ch;
  int count = 0;
  while ((ch = fgetc(outputFile)) != EOF)
  {
    if ((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z'))
    {
      count++;
    }
  }
  printf("%d => Ta", count);
  fclose(outputFile);
}

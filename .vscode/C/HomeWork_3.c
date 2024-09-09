#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <string.h>

void new1(char *arr, int n)
{
  for (int i = 0; i < n - 1; i++)
  {
    for (int j = 0; j < n - i - 1; j++)
    {
      if (arr[j] < arr[j + 1])
      {
        char temp = arr[j];
        arr[j] = arr[j + i];
        arr[j + i] = temp;
      }
    }
  }
}

void new2(char *arr, int n)
{
  for (int i = 0; i < n - 1; ++i)
  {
    for (int j = 0; j < n - i - 1; j++)
    {
      if (arr[j] > arr[j + 1])
      {
        char temp1 = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp1;
      }
    }
  }
}
int main()
{

  FILE *inputFile = fopen("text3.txt", "w");
  char let[256];
  scanf("%[^\n]", let);
  fwrite(let, 1, strlen(let), inputFile);
  fclose(inputFile);
  int length = strlen(let);

  FILE *outputFile = fopen("text3.txt", "r");
  FILE *Test = fopen("TestText.txt", "w");
  char ch;
  int count = 0;
  char number[100];
  while ((ch = fgetc(outputFile)) != EOF)
  {
    if (isdigit(ch))
    {
      number[count++] = ch;
      fputc(ch, Test);
    }
  }
  fclose(outputFile);
  fclose(Test);
  new1(number, count);
  FILE *new1 = fopen("new1.txt", "w");
  for (int i = 0; i < count; ++i)
  {
    fputc(number[i], new1);
  }
  fclose(new1);

  new2(number, count);
  FILE *new2 = fopen("new2.txt", "w");
  for (int i = 0; i < count; ++i)
  {
    fputc(number[i], new2);
  }
  fclose(new2);
}

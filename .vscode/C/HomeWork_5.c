#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <string.h>

int main()
{
  FILE *inputFile, *outputFile;
  char operator;
  int num1, num2, result;

  inputFile = fopen("input.txt", "r");

  while (fscanf(inputFile, "%d %c %d", &num1, &operator, & num2) != EOF)
  {
    switch (operator)
    {
    case '+':
      result = num1 + num2;
      break;
    case '-':
      result = num1 - num2;
      break;
    case '*':
      result = num1 * num2;
      break;
    case '/':
      if (num2 != 0)
      {
        result = num1 / num2;
      }
      fprintf(outputFile, "%d %c %d = %d\n", num1, operator, num2, result);
    }
  }
  fclose(inputFile);
  fclose(outputFile);
}
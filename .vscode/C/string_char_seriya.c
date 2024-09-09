#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <string.h>

/// katta va kichik harflarni almashtirish
/*
int main()
{
  char let[256] = "";
  scanf("%[^\n]", let);
  for (int i = 0; let[i]; ++i)
  {
    if (islower(let[i]))
    {
      let[i] = toupper(let[i]);
    }
    else if (isupper(let[i]))
    {
      let[i] = tolower(let[i]);
    }
  }
  printf("%s ", let);
}
*/

/// Birinchi va ohirgi raqamlar ortasidagi matinlar;
/*
int main()
{
  char let[256] = "";
  scanf("%[^\n]", let);
  int first = 0, last = 0, key = 1;
  for (int i = 0; let[i]; ++i)
  {
    if (isalnum(let[i]))
    {
      if (key)
      {
        first = i;
        key = 0;
      }
      else
      {
        last = i;
      }
    }
  }
  for (int i = first + 1; i < last; ++i)
  {
    printf("%c", let[i]);
  }
}
*/

/// Birinchi va ohirgi harflar ortasidagi matinlar;
/*
int main()
{
  char let[256] = "";
  scanf("%[^\n]", let);
  int first = 0, last = 0, key = 1;
  for (int i = 0; let[i]; ++i)
  {
    if (isalpha(let[i]))
    {
      if (key)
      {
        first = i;
        key = 0;
      }
      else
      {
        last = i;
      }
    }
  }
  for (int i = first + 1; i < last; ++i)
  {
    printf("%c", let[i]);
  }
}
*/

/// matinni teskari tartipda yozish
/*
void Reverse(char arr[], int n)
{
  for (int i = n - 1; i >= 0; --i)
  {
    printf("%c",arr[i]);
  }
}

int main()
{
  char let[256] = "";
  scanf("%[^\n]", let);
  int n = strlen(let);
  Reverse(let, n);
}
*/

/// alphabet bo'yicha sortlash;
/*
void Fifth(char a[])
{
  char ch;
  int n = strlen(ch);
  for (int i = 0; i < n - 1; ++i)
  {
    for (int j = i + 1; j < n; ++j)
    {
      if (islower(a[i]))
      {
        if (a[i] > a[j])
        {
          ch = a[i];
          a[i] = a[j];
          a[j] = ch;
        }
      }
    }
  }
}

int main()
{
  char c[50];
  scanf("%[^\n]", c);
  Fifth(c);
  printf("%s", c);
}
*/

/// n-chi indxden i-chi indexgacha bolgan matinni chiqariberadi
/*
void Fifth(int Index, int num, char a[], char ch[])
{
  int i;
  for (int i = 0; i < num && a[Index + i]; ++i)
  {
    ch[i] = a[Index + i];
  }
  ch[i];
}

int main()
{
  int ind, num;
  char a[50];
  char ch[50];
  printf("Char => ");
  scanf("%[^\n]", a);
  printf("Enter Index: ");
  scanf("%d", &ind);
  printf("Enter Number: ");
  scanf("%d", &num);
  Fifth(ind, num, a, ch);
  printf("%s", ch);
  return 0;
}
*/



#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <string.h>

// Kator bo'yicha sort_lash
/*
int main()
{
int n;
scanf("%d", &n);
int arr[n][n];
srand(time(NULL));
for (int i = 0; i < n; ++i)
{
  for (int j = 0; j < n; ++j)
  {
    // printf("[%d:%d] ", i, j);
    arr[i][j] = rand() % 9 + 1;
    printf("%d ", arr[i][j]);
  }
  puts("");
}
puts("");

for (int i = 0; i < n; ++i)
{
  for (int j = 0; j < n - 1; ++j)
  {
    for (int k = 0; k < n - j - 1; ++k)
    {
      if (arr[i][k + 1] < arr[i][k])
      {
        int temp = arr[i][k];
        arr[i][k] = arr[i][k + 1];
        arr[i][k + 1] = temp;
      }
    }
  }
}
for (int i = 0; i < n; ++i)
{
  for (int j = 0; j < n; ++j)
  {
    printf("%d ", arr[i][j]);
  }
  puts("");
}
}
*/

// matrisa ustunlarining yigindisi
/*
int main()
{
int n, m;
scanf("%d", &n);
scanf("%d", &m);
int arr[n][m];
srand(time(NULL));

for (int i = 0; i < n; ++i)
{
  for (int j = 0; j < m; ++j)
  {
    arr[i][j] = rand() % 9 + 1;
    printf("%d ", arr[i][j]);
  }
  puts("");
}
puts("");

int arr2[m];
for (int j = 0; j < m; ++j)
{
  arr2[j] = 0;
}

for (int i = 0; i < n; ++i)
{
  for (int j = 0; j < m; ++j)
  {
    arr2[j] += arr[i][j];
  }
}
for (int j = 0; j < m; ++j)
{
  printf("%d - ustun => %d\n", j + 1, arr2[j]);
}
}
*/

/// different shakillar
/*
int main()
{
int n;
scanf("%d", &n);
int arr[n][n];
srand(time(NULL));
for (int i = 0; i < n; ++i)
{
  for (int j = 0; j < n; ++j)
  {
    arr[i][j] = rand() % 9 + 1;
    printf("%d ", arr[i][j]);
  }
  puts("");
}
puts("");
for (int i = 0; i < n; ++i)
{
  for (int j = 0; j < n; ++j)
  {
    ///  ==>  kres shakl  <==
    // if (i == j || j + i== n - 1) printf("* ");
    // else printf("%d ", arr[i][j]);

    ///  ==>  To'rli shakil <==
    // if ((j + i) % 2 == 0) printf("* ");
    // else printf("%d ", arr[i][j]);

  }
  puts("");
}
}
*/

// qatorlar bitta keyingisi bilan ozgatishi
/*
void First(int a, int arr[a][a])
{
  srand(time(0));
  for (int i = 0; i < a; ++i)
  {
    for (int j = 0; j < a; ++j)
    {
      arr[i][j] = rand() % 9 + 1;
      printf("%d ", arr[i][j]);
    }
    puts("");
  }
  puts("");

  int temp;
  for (int i = 0; i < a / 2; ++i)
  {
    for (int j = 0; j < a; ++j)
    {
      temp = arr[i][j];
      arr[i][j] = arr[a - 1 - i][j];
      arr[a - 1 - i][j] = temp;
    }
  }

  puts("Result:");
  for (int i = 0; i < a; ++i)
  {
    for (int j = 0; j < a; ++j)
    {
      printf("%d ", arr[i][j]);
    }
    puts("");
  }
}

int main()
{
  int a;
  scanf("%d", &a);
  int arr[a][a];
  First(a, arr);
}
*/

// ustunlar bitta keyingisi bilan ozgatishi
/*
void First(int a, int arr[a][a])
{
  srand(time(0));
  for (int i = 0; i < a; ++i)
  {
    for (int j = 0; j < a; ++j)
    {
      arr[i][j] = rand() % 9 + 1;
      printf("%d ", arr[i][j]);
    }
    puts("");
  }
  puts("");

  int temp;
  for (int i = 0; i < a ; ++i)
  {
    for (int j = 0; j < a / 2; ++j)
    {
      temp = arr[i][j];
      arr[i][j] = arr[i][a - 1 - j];
      arr[i][a - 1 - j] = temp;
    }
  }

  puts("Result:");
  for (int i = 0; i < a; ++i)
  {
    for (int j = 0; j < a; ++j)
    {
      printf("%d ", arr[i][j]);
    }
    puts("");
  }
}

int main()
{
  int a;
  scanf("%d", &a);
  int arr[a][a];
  First(a, arr);
}
*/

// int A[n * n] => {manfiy elementla jamlanmasi}
// int B[n * n] => {musbat elementla jamlanmasi}
/*
void Second(int n, int arr[n][n])
{
  srand(time(0));
  int sizeA = 0, sizeB = 0;
  int A[n * n], B[n * n];

  for (int i = 0; i < n; ++i)
  {
    for (int j = 0; j < n; ++j)
    {
      arr[i][j] = rand() % 42 - 21;
      printf("%d ", arr[i][j]);
    }
    puts("");
  }
  puts("");
  for (int i = 0; i < n; ++i)
  {
    for (int j = 0; j < n; ++j)
    {
      if (arr[i][j] < 0)
      {
        A[sizeA] = arr[i][j];
        sizeA++;
      }
      else if (arr[i][j] > 0)
      {
        B[sizeB] = arr[i][j];
        sizeB++;
      }
    }
  }
  printf("A = {");
  for (int i = 0; i < sizeA; ++i)
  {
    printf("%d", A[i]);
    if (i < sizeA - 1)
    {
      printf(", ");
    }
  }
  printf("}\n");

  printf("B = {");
  for (int i = 0; i < sizeB; ++i)
  {
    printf("%d", B[i]);
    if (i < sizeB - 1)
    {
      printf(", ");
    }
  }
  printf("}\n");
}

int main()
{
  int n;
  scanf("%d", &n);
  int arr[n][n];
  Second(n, arr);
}
*/


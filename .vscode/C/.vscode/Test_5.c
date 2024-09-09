#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <conio.h>
#include <string.h>

struct Dasturchi
{
  char name[256];
  int age[5];
  char language[256];
  char mutahasislik[256];
  int tajriba[5];
};

int main()
{
  struct Dasturchi mal1 = {"Ali", 28, "Java", "Backend", 2};
  struct Dasturchi mal1 = {"Botir", 22, "Pyton", "Backend", 3};
  struct Dasturchi mal1 = {"Umid", 35, "Js", "Frontend", 1};
  struct Dasturchi mal1 = {"Akbar", 31, "Jc", "Frontend", 2};
  struct Dasturchi mal1 = {"Nigga", 22, "C#", "Backend", 1};

  for (int i = 0; i < strlen(mal1.tajriba) >= 1; ++i)
  {
    printf("%s ", mal1.name);
  }

  // C# blan odashtirip qoydim #C esdan chiqip qolipdi )
}

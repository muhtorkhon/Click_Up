#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <string.h>

// void Find(char ch[])
// {
//   char c[50];
//   for(int i = 0; i<ch[i]; ++i)
//   {
//     printf("%c",ch[i]);
//   }
//   puts("");
//   for (int i = strlen(ch); i >= 0; --i)
//   {
//     printf("%c",ch[i]);
//   }
// }

// void Find(char ch[])
// {
//   for(int i = 0; i < strlen(ch)/2; ++i)
//   {
//     printf("%c",ch[i]);
//   }
//   for (int i = strlen(ch); i >= strlen(ch) / 2; --i)
//   {
//     printf("%c",ch[i]);
//   }
// }

// void Find(char ch[])
// {
//   int count = 0;
//   for(int i = 0; i<strlen(ch); ++i)
//   {
//       ++count ;
//   }
//   if(count % 2 == 0)
//   printf("Juft");
//   else printf("Toq");
// }

// void Find(char ch[])
// {
//   char temp;
//   for(int i = 0; i < strlen(ch) - 1; ++i)
//   {
//     for (int j = i + 1; j < strlen(ch); ++j)
//     {
//       if(ch[i] > ch[j])
//       {
//         temp = ch[i];
//         ch[i] = ch[j];
//         ch[j] = temp;
//       }
//     }
//   }
// }

//// ==>1
// struct Bola
// {
//   char name[50];
//   int Age;
// };

// int main()
// {
// struct Bola b3 = {"Sanjy", 22};
// struct Bola b2 = {"Zorro",24};
// struct Bola b1 = {"Luffy", 20};

// int check = b1.Age;
// if(check < b2.Age)
// {
//   printf("Name: %s\nAge: %d",b2.name,b2.Age);
// }
// else if(b2.Age < b3.Age )
// {
//   printf("Name: %s\nAge: %d", b3.name, b3.Age);
// }
// else
// {
//   printf("Name: %s\nAge: %d", b1.name, b1.Age);
// }
// }

/// ==> 2
// struct Student
// {
//   char name[50];
//   int age;
// };

// int main()
// {

//   struct Student st[5] =
//       {
//           {"Karim", 15},
//           {"Abror", 15},
//           {"Vali", 15},
//           {"Akromboy", 15},
//           {"Akbar", 15},
//       };

//   for (int i = 0; i < 5; ++i)
//   {
//     if (strlen(st[i].name) == 5 && st[i].name[0] == 'A')
//     {
//       printf("%s %d\n", st[i], st[i].age);
//     }
//   }
// }

/// ==> 3
// struct Talaba
// {
//   char name[50];
//   int scholarship;
//   int course;
// };

// int main()
// {
//   printf("How many student: ");
//   int n;
//   scanf("%d", &n);
//   struct Talaba t[n];
//   int count = 0;
//   for (int i = 0; i < n; ++i)
//   {
//     printf("Student name => ");
//     scanf("%s", t[i].name);
//     printf("Student scholarship => ");
//     scanf("%d", &t[i].scholarship);
//     printf("Student course => ");
//     scanf("%d", &t[i].course);
//   }
//   for (int i = 0; i < n; ++i)
//   {
//     if (t[i].course == 3)
//     {
//       count += t[i].scholarship;
//       printf("Name: %s\nScholarship: %d\nCourse: %d\n"
//       ,t[i].name,t[i].scholarship,t[i].course);
//     }
//   }
//   printf("\n%d", count);
// }

/// ==> 2
// struct Student
// {
//   char name[50];
//   int scholarship;
//   int course;
// };

// int main()
// {
//   int n;
//   scanf("%d", &n);
//   struct Student std[n];
//   for (int i = 0; i < n; i++)
//   {
//     printf("Student name => ");
//     scanf("%s", std[i].name);
//     printf("Student scholarship => ");
//     scanf("%d", &std[i].scholarship);
//     printf("Student course => ");
//     scanf("%d", &std[i].course);
//   }

//   for (int i = 0; i < n; ++i)
//   {
//     if (std[i].scholarship == 100000 && strlen(std[i].name) >= 5)
//     {
//       printf("Name: %s\nScholarship: %d\nCourse: %d\n", std[i].name, std[i].scholarship, std[i].course);
//     }
//   }
// }

// malloc
// calloc
// realloc
// free

// int n;
// scanf("%d", &n);
// int *arr = malloc(n * sizeof(int));

// for (int i = 0; i < n; i++)
// {
//   scanf("%d", &arr[i]); // arr+i; &*(arr+i);
// }

// for (int i = 0; i < n; i++)
// {
//   if (arr[i] > 0)
//   {
//     printf("%d ", arr[i]);
//   }
// }

/// struct 1
// struct Person
// {
//   char name[20];
//   int age;
//   int id;
// };

int main()
{
  /// ==> 1
  /*
    // FILE *f = fopen("C:/Users/Dior/OneDrive/Desktop/Nigga/test.txt", "w");
    // for (int i = 1; i <= 10; ++i)
    // {
    //   for (int j = 1; j <= 10; ++j)
    //   {
    //     fprintf(f, "%d * %d = %d\n", i, j, i * j);
    //   }
    //   fputs("\n",f);
    // }
    // fclose(f);

    // int n;
    // scanf("%d", &n);
    // int arr[n];
    // srand(time(NULL));
    // FILE *f = fopen("C:/Users/Dior/OneDrive/Desktop/Nigga/test1.txt", "w");

    // for (int i = 0; i < n; ++i)
    // {
    //   arr[i] = rand() % 10 + 1;
    //   printf("%d ", arr[i]);
    // }

    // puts("");

    // for (int i = 0; i < n - 1; ++i)
    // {
    //   for (int j = 0; j < n - 1 - i; ++j)
    //   {
    //     if (arr[j] > arr[j + 1])
    //     {
    //       char temp = arr[j];
    //       arr[j] = arr[j + 1];
    //       arr[j + 1] = temp;
    //     }
    //   }
    // }

    // puts("");

    // for (int i = 0; i < n; ++i)
    // {
    //   fprintf(f, "%d ", arr[i]);
    // }

    // fclose(f);

    /// ==> 2

    // char arr[] = "Salom bolalar nima gap niggas FN-105";
    // FILE *f = fopen("C:/Users/Dior/OneDrive/Desktop/Nigga/test2.txt", "w");

    // for(int i=0; arr[i]; ++i)
    // {
    //   if (arr[i] == 'a' || arr[i] == 'o' || arr[i] == 'e' || arr[i] == 'i' || arr[i] == 'u')
    //   {
    //     fprintf(f,"%c",arr[i]);
    //   }
    // }
    // fclose(f);

    /// ==> 3
    // char arr[] = "Salom bolalar nima gap bitch ass nigga FN-105";
    // FILE *f = fopen("C:/Users/Dior/OneDrive/Desktop/Nigga/test2.txt", "w");
    // char *ptr = strtok(arr, " ");
    // while (ptr)
    // {
    //   if (strlen(ptr) % 2 == 0)
    //   {
    //     fputs(ptr, f);
    //     fputc('\n', f);
    //   }
    //   ptr = strtok(NULL, " ");
    // }
    // fclose(f);
    /// ==> 4

    // int n;
    // printf("Number of arrays: ");
    // scanf("%d", &n);
    // int arr[n];
    // srand(time(NULL));
    // FILE *po = fopen("C:/Users/Dior/OneDrive/Desktop/Nigga/test.txtPositive", "w");
    // FILE *ne = fopen("C:/Users/Dior/OneDrive/Desktop/Nigga/test.txtNegative", "w");
    // for (int i = 0; i < n; ++i)
    // {
    //   arr[i] = rand() % 21 - 10;
    // }

    // for (int i = 0; i < n; ++i)
    // {
    //   if (arr[i] > 0)
    //   {
    //     fprintf(po, "%d ", arr[i]);
    //   }
    //   if (arr[i] < 0)
    //   {
    //     fprintf(ne, "%d ", arr[i]);
    //   }
    // }

    // fclose(po);
    // fclose(ne);

    // FILE *f = fopen("C:/Users/Dior/OneDrive/Desktop/Nigga/test.txtPositive", "r");
    // char el[256] = "";
    // int i=0;
    // while (el[i++] = fgetc(f) != EOF){}
    // printf("%s", el);
    // fclose(f);

    // FILE *f = fopen("C:/Users/Dior/OneDrive/Desktop/Nigga/test.txtNegative", "r");
    // char word[100]="";
    // while((fscanf(f,"%s",word)) != EOF )
    // {
    //   printf("%s ", word);
    // }
    // fclose(f);
  */
  ///==> Read
  // FILE *f = fopen("file1.txt", "r");
  // char c;
  // while (fread(&c, 1, 1, f) > 0)
  // {
  //   printf("%c",c);
  // }

  /// ==> Write
  // FILE *f = fopen("file2.txt", "w");
  // char c[1000] = "";
  // scanf("%[^\n]",c);
  // fwrite(c,1,strlen(c),f);

  /// ==> binary trush
  // FILE *f = fopen("file2.txt", "rb");
  // int n ;
  // fread(&n,4,1,f);
  // printf("%d\n",n);

  /// ==> Struct 1 , look above int main nigga
  // FILE *f = fopen("file2.txt","wb");
  // struct Person per = {"Diar" ,22, 26403};
  // fwrite(&per,sizeof(struct Person),1,f);
  // fclose(f);

  // FILE *f1 = fopen("file2.txt", "rb");
  // fread(&per, sizeof(struct Person), 1, f);
  // fclose(f1);

  // FILE *im = fopen("niggaIMG.png", "rb");
  // FILE *out = fopen("New_File.png", "wb");
  // int bayt;
  // while (fread(&bayt, 4, 1, im) > 0)
  // {
  //   fwrite(&bayt, 4, 1, out);
  // }

  // fclose(im);
  // fclose(out);

  /// 1
  // FILE *f = fopen("text.txt", "r");
  // int num, sum = 0, i = 0;
  // while (fscanf(f, "%d", &num) > 0)
  // {
  //   sum += num;
  //   i++;
  // }
  // fclose(f);
  // int total = sum/i;
  // printf("%d",total);

  /// 2 ---
  // FILE *f = fopen("Text3", "w");
  // char ch[100];
  // scanf("%[^\n]", ch);
  // fputs(ch, f);

  // FILE *input = fopen("output.txt", "w");
  // char buffer[100];
  // fgets(buffer, sizeof(buffer), input);
  // for (int i = strlen(buffer) - 1; i > 0; ++i)
  // {
  //   fprintf(input, buffer);
  // }

  // fclose(f);
  // fclose(input);

  FILE *w = fopen("TestText.txt", "w");
  char let[900];
  scanf("%[^\n]", let);
  fwrite(let, 1, strlen(let), w);
  fclose(w);
  FILE *r = fopen("TestText.txt", "r");
  char c;

  while (fread(&c, 1, 1, r) > 0)
  {
    printf("%c", c);
  }
  fclose(r);


}


/// Photo changing format
// int main()
// {
//   FILE *im = fopen("niggaIMG", "rb");
//   FILE *out = fopen("New_File.png", "wb");
//   int bayt;
//   while (fread(&bayt, 4, 1, im) > 0)
//   {
//     fwrite(&bayt, 4, 1, out);
//   }
//   fclose(im);
//   fclose(out);
// }
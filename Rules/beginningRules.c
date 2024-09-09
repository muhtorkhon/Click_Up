#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <string.h>

int main()
{
    /*
    // int a;
    // printf("Son kiriting: ");
    // scanf("%d", &a);
    // printf("A ning qiymati -> %d", a);


    // float a,b;
    // printf("A ga qiymat kiriting: ");
    // scanf("%f", &a);
    // printf("B ga qiymat kiriting: ");
    // scanf("%f", &b);
    // printf("%f + %f = %f", a, b, a+b)


    // int son1, son2, son3;
    // scanf("%d%d%d", &son1, &son2, &son3);
    // printf("son1 -> %d\nson2 -> %d\nson3 -> %d", son1, son2, son3);


    // char element;
    // printf("Element kiriting: ");
    // scanf("%c", &element);
    // printf("Natija -> %c", element);


    // int son1, son2;
    // char amal;
    // printf("Son kiriting: ");
    // scanf("%d", &son1);
    // printf("Amal kiriting: ");
    // scanf(" %c", &amal);
    // printf("Ikkinchi sonni kiriting: ");
    // scanf("%d", &son2);
    // printf("%d%c%d", son1, amal, son2);
        */

    /*
    // printf("%d\n"); // trash
    // printf("%d\n", 56.5); // trash
    // printf("%d\n", 'a'); // 97
    // printf("%d", '5'+5); // 58


    // printf("%f\n"); // trash
    // printf("%f\n", 56); // trash
    // printf("%f\n", 'a'); // trash
    // printf("%f\n", 45.6); // 45.6


    // printf("%c\n"); // trash
    // printf("%c\n", 97); // 'a'
    // printf("%c\n", 'a');// 'a'
    // printf("%c", 97.5); // trash


    // printf("%g\n", 56.3); --> Float uchun xzmat qiladi va ortiqcha nollarsiz chiqaziberadi
    // printf("%g", 56.358); /


    // printf("%.2f\n", 56.3);   \
    // printf("%.0f\n", 56.314);  \
                                    > nuqtada ko'rsatilgan honagacha sonlarni yahlidlab chiqazadi
    // printf("%.3f\n", 56.3246); /
    // printf("%.0f", 56.5670); /


    // printf("%5d\n", 23);              \
    // printf("%5d\n", 231223);            \
    // printf("%5d\n", 2223);               > Kiritilgan songacha kiymat qabul qilishga majbur agar son yetmasa ozidan 0 qoshadi
    // printf("%06d\n", 23);               /
    // printf("%02d\n", 2);              /
    // printf("%02d:%02d:%02d",2,24,13);


    int a,b;
    scanf("%2d", &a);
    scanf("%d", &b);
    printf("%d    -      %d", a,b);
    */

    /// string / char skills

    //    /// strcpy() ==> string copy
    /**
    char a[10] = "ABCDIFG";
    char b[10] = "12345";
    strcpy(a+3,b+1); /// ABC345
    printf("%s\n%s",a,b);
    **/

    /// strlen() ==> string length
    /**
    char matn[15] = "salom";
    printf("Res => %d",strlen(matn)); //// Res => 5
    **/

    /// strcat() ==> string concatenate
    /*
    //strcat(qabul qiluchi , yuboruvchi)
    char a[10] = "ABCDE";
    char b[10] = "12345";
    strcat(a,b);/// ABCDE12345
    printf("%s\n%s",a,b);
    */

    /// strcmp() ==> string compiler
    /*
    //strcmp("salom","salom");
    // 1 => 1-chi satr katta
    // 0 => Teng
    //-1 => 2-chi satr katta
    //------------------
    char a[50] = "salom";
    char b[50] = "salom";
    if(strcmp(a,b) == 0) puts("Teng");
    else puts("Teng emas");
    */

    /// strtok() ==> string tokenization
    /*
    char str[50] = "what is up Nigga";
    char *ptr = strtok(str," ");

    while(ptr != NULL)
    {
        printf("%s",ptr);
        ptr = strtok(NULL," ");
    }
    /// whatisupNigga
    */

    /// Working With Files

    // --------------------------------------------------------//

    // fputc( ' ' , f ) => file put char      | one element

    // --------------------------------------------------------//

    // fputs( "string" , f ) => file put string  | string

    //--------------------------------------------------------//

    // FILE *f = fopen("text.txt", "w");
    // char ch[100] = "";
    // scanf("%[^\n]",ch);
    // fprintf(f, "%s", ch) ;  //=> only for  ==> write <==

    //-------------------------------------------------------//

    // FILE *f = fopen("text.txt", "r");
    // fgetc() => file get char | only for ==> read <==
    // char el;
    // while(el = fgetc(f) != -1) // or EOF ==> End Of File | char
    // {
    //     printf("%c",el);
    // }

    // ------------------------------------------------------------------------------//

    // FILE *f = fopen("text.txt", "r");
    // fscanf(f,"%s", ozfaruvchi)  ==> only for read | Fayil ichidagi matinni o'qish uchun

    // char ch[100] = "";
    // while(fscanf(f,"%s",ch) != EOF)  // cahr uchun
    // {
    //     printf("%s\n", ch);
    // }

    // int num, sum = 0;
    // while (fscanf(f, "%d", &num) != EOF) // fscanf(f,"%d", &num) int uchun
    // {
    //     sum += num;
    // }
    // printf("%d",sum);

    // ---------------------------------------------------------------------------//

    // fread(&buffer, techta elementdan o'qilishi , nechi baytligi , f)

    // FILE *f = fopen("text.txt", "r");
    // char el;
    // while (fread(&el, 1, 1, f) > 0)
    // {
    //     printf("%c",el);
    // }

    // ------------------------------------------------------------------------------//



    // fclose(f);



}
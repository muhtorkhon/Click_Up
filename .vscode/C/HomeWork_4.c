#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <string.h>

int main()
{
    int N;
    printf("Enter N: ");
    scanf("%d", &N);

    FILE *outputFile = fopen("text.txt", "w");
    int sum = 0;
    for (int i = 1; i <= N; i++)
    {
        sum += i;
        if (i == 1)
        {
            fprintf(outputFile, "%d ", i);
        }
        else
        {
            fprintf(outputFile, "+ %d ", i);
        }
    }
    fprintf(outputFile, " =%d\n", sum);

    fclose(outputFile);
    return 0;
}

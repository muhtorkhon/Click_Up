#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

/// 1
// float Bol(float a, float b)
// {
//     float res = a/b;
//     return res;
// }
/// 2
// int ABC(int a)
// {
//     if(a>0) return a;
//     if(a<0) return (a * -1);
// }
/// 3
// int Min(int a, int b, int c, int d, int e)
// {
//     int min = a;
//     if(b<min) min = b;
//     if(c<min) min = c;
//     if(d<min) min = d;
//     if(d<min) min = e;
//     return min;
// }
/// the last
// float give(float a, float b)
// {
//     if(a+b>10 && a+b<20)
//     return 1;
//     else return 0;
// }

/// Toq index ni oldidagi ishorasini almashtirish;
int main()
{

    // srand(time(NULL));
    // int n,a;
    // scanf("%d",&n);
    // int arr[n] , arr1[n];
    // for(int i=0; i<n; i++)
    // {
    //     printf("[%d]:",i);
    //     arr[i] = rand()%21 - 10;
    //     printf("%d\n",arr[i]);
    // }

    // printf("Positive numbers %d\n",pos);
    // printf("Negative numbers %d\n",neg);

    // float a,b; the last
    // scanf("%f%f", &a,&b);
    // float res = give(a,b);
    // printf("%0.0f",res);

    // int a,b,c,d,e;  3
    // scanf("%d%d%d%d%d",&a,&b,&c,&d,&e);
    // int res = Min(a,b,c,d,e);
    // printf("Min =>%d",res);

    // int n;  2
    // scanf("%d",&n);
    // int res = ABC(n);
    // printf("%d",res);

    // float a,b;  1
    // scanf("%f%f",&a,&b);
    // float res = Bol(a, b);
    // printf("%f",res);

    /// char big or smal letter ?
    /*
    char c ;
    scanf("%c",&c);
    if('a' <= c && c <= 'z')
    {
        printf("You entred a litter letter=> %c", c);
    }
    else if('A' <= c && c <= 'Z')
    {
        printf("You entred a big letter=> %c", c);
    }
    else
    {
        printf("Enter only(one) letter !!!");
    }
    */

    /// char replace large letter with small or vice verca
    /*
    char c ,ch;
    scanf("%c",&c);
    if('a' <= c && c <= 'z')
    {

        printf("%c", c - 32);
    }
    else if('A' <= c && c <= 'Z')
    {
        printf("%c", c + 32);
    }
    */

    /// char alphabet
    /*
    char c = 97;
    while( c <='z')
    {
        printf("%c " , c);
        c=c+1;
    }
    */

    /// float output numbers from 1 to n/2
    /*
    float n , i = 1 , r = 1; //5
    scanf("%f",& n);
    while(i <= n)
    {
        printf("%.1f ", r);// 1 1 1.5
        ++i;
        r =  i / 2 ;
    }
    */

    /// int 1 dan n gacha bolgan toq sonlarni teskarisi
    /**
    int n, i = 1, r, a;
    scanf("%d",& n);
    while(i <= n)
    {
        if(i % 2 != 0)
        {
            a=i;
            r = 0;
            while(a!=0)
            {
                r = r * 10  + a % 10;
                a /= 10;
            }
            printf("%d ", r);
        }
        ++i;
    }
    **/

    /// int start (a+b) stop (a-b)
    /*
    int a, b, s , f;
    scanf("%d",& a);
    scanf("%d",& b);
    s = a - b;
    f = a + b;
    while(s <= f)
    {
        printf("%d\n", s);
        s += 1;
    }
    */

    /// int sum of numbers
    /*
    int n , i = 1, r = 0;
    scanf("%d",& n); /// 123

    do{
        r = r + n % 10; //r=3+2+1=0  / 12[3], 1[2], [1]
        n=n/10;  // 12/[3], 1/[2][3], [1][2][3]
    }while(n!=0);

    if(r % 2 == 0){
        while(i<=5){
            printf("Niggaev\n");
            ++i;
        }
    }

    else if(r % 2 != 0){
        while(i<=4){
            printf("BigDeeyy\n");
            ++i;
       }
    }
    */

    /// Finding odd and even numbers
    /*
    int n, r=0, odd = 0, even = 0;
    scanf("%d",&n);

    while(n!=0)
    {
        r = n % 10;
        if(r%2!=0)
        {
            odd += 1;
        }
        else if(r%2==0)
        {
            even += 1;
        }
        n = n / 10;
    }
    printf("odd numbers %d\n",odd);
    printf("even numbers %d\n",even);
    */

    /// from so'm to dollar
    /*
    float som ,res = 0, dollar_1 = 11200;
    printf("Enter so'm: ");
    scanf("%f",& som);
    res = som / dollar_1;
    printf("%g :dollar", res);
    */

    /// 1 bayt = 8 bit | 1 kb = 1024 bayt ....
    /*
    float bayt,kb;
    printf("[bayt] => ");
    scanf("%f",&bayt);
    kb = bayt / 1024;
    printf("[KB]=> %.1f", kb);
    */

    /// How many Hours Minutes and seconds are there in N secons
    /*
    int n, s, h,m;
    scanf("%d",& n);
    h=n/3600;
    n = n % 3600;
    m = n / 60;
    s = n % 60;
    printf("%d-hours %d-minutes %d-seconds",h,m,s);
    */

    /// change numbers from a to b
    /*
    int a,b; // a=1 : b=2
    printf("a => ");
    scanf("%d",& a);
    printf("b => ");
    scanf("%d",& b);
    a=a+b;//3
    b=a-b;//1
    a=a-b;//2
    printf("a => %d\n",a);
    printf("b => %d",b);
    */

    /// T=S/V
    /*
    float S,V = 7,T; // all km/h t == s/v
    scanf("%f",& S);
    T = S/V;
    printf("%.1f Hours",T);
    */

    /// How many Days Hours Minutes and seconds are there in N secons
    /*
    int n, d, h, m, s;
    scanf("%d",&n);
    d = n / 86400;
    n = n % 86400;
    h = n / 3600;
    n = n % 3600;
    m = n / 60;
    s = n % 60;
    printf("days- %d: hours- %d: minutes- %d: seconds-%d", d,h,m,s);
    */

    /// True and False
    /*
    int n , r;
    scanf("%d",&n);
    bool c = false;
    while (n>0)
    {
        r = n % 10;
        if(r==3)
        {
            c = true;
            break;
        }
        n=n/10;
    }
    if (c)
    {
        printf("TRUE\n");
    }
    else
    {
        printf("FALSE\n");
    }
    */
    /*
    int n , l, f;
    scanf("%d",& n);

    f = n % 10;

    while(n > 0)
    {
        l = n % 10;

        n /= 10;
    }
    printf("%d\n",f);
    printf("%d",l);
    */

    /// 1
    /*
    int a,b,c;
    scanf("%d",& a);
    scanf("%d",& b);
    scanf("%d",& c);
    if(abs(a - b) >= 10 || abs(a - c) >= 10 || abs(b - c) >= 10)
    printf("true");
    else
    printf("false");
    */

    /// 2
    /*
    int a,b;
    bool res ;
    scanf("%d %d",&a, &b);
    res = (a > 2) && (b <= 3);
    printf("%s", res? "True" : "False");
    */

    /// 3
    /*
    int a, b, c;
    int Count = 0;
    bool res;
    scanf("%d %d %d",&a, &b, &c);

        Count = Count + (a > 0);
        Count = Count + (b > 0);
        Count = Count + (c > 0);

    res = (Count == 2);
    printf("%s",res? "True" : "False");
    */

    /// 4
    /*
    int n,r1,r2,r3;
    bool res;
    scanf("%d",&n);//321
    r1 = n % 10;
    r2 = n / 10 % 10;
    r3 = n / 100;
    res = (r3<r2) && (r2<r1);
    printf("%s\n", res ? "True" : "False");
    */

    /// 5
    /*
    int n,r1,r2,r3;
    bool res;
    scanf("%d",&n);
    r1 = n % 10;
    r2 = n / 10 % 10;
    r3 = n / 100;
    res = (r3<r2 && r2<r1) || (r3>r2 && r2>r1);
    printf("%s\n", res ? "True" : "False");
    */

    /// 6
    /*
    int n, r, max = 0;
    scanf("%d",&n);
    for(int i = n; i; i = i / 10) // 1 2 3
    {
        r = i % 10;
        if(max < r)
        {
            max = r; // 3
        }
        r = 0;
    }
    printf("Max => %d",max);
    */

    /// 7 ------

    /// 8
    /*
    int a, b, c,d;
    int min,max, result;
    scanf("%d %d %d %d",&a, &b, &c, &d);
    if(a==b && a==c && a==d && b==c && b==d && c==d)
    {
        result = a+b+c+d;
        printf("Total result %d", result);
    }
    else
    {
        max = a;
        if(b > max) max = b;
        if(c > max) max = c;
        if(d > max) max = d;

        min = a;
        if(b < min) min = b;
        if(c < min) min = c;
        if(d < min) min = d;

        result = max - min ;
    }
    printf("Total result %d",result);
    */

    /// 9
    /*
    int a,b,c, multi = 1;
    scanf("%d",& a);
    scanf("%d",& b);
    scanf("%d",& c);

    if(a==b) multi = c;
    else if(a==c) multi = b;
    else if(b==c) multi = a;
    else multi = a*b*c;
    printf("%d",multi);
    */

    /*
    // int n;
    // scanf("%d",&n);

    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         if(j + i < n )
    //         {
    //             printf("*");
    //         }
    //         else
    //         printf(" ");
    //     }
    //     puts("");

    // }

    */

    /*
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         if(i > j - 1)
    //         {
    //             printf("*");
    //         }
    //         else
    //         printf(" ");
    //     }
    //     puts("");

    // }
    */

    /*
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         if(i == 0 || i==n-1 || j==0 || j== n-1)
    //         {
    //             printf("*");
    //         }
    //         else
    //         printf(" ");
    //     }
    //     puts("");

    // }

    */

    /// Armstrong numbers
    /*
    int n,a = 0, r = 0 ,count = 0 , sum;
    scanf("%d",&n);
    for(int i = n; i; i = i / 10)  count ++; // count
    for(int j = n; j; j = j / 10)
    {
        a = j % 10;
        sum = 1;
        for(int k = 1; k <= count; ++k)
        {
            sum = sum * a;
        }
        r=r+sum;
    }
        if(r == n)
        {
            printf("Armstrong number");
        }
        else
        printf("Not Armstrong number");
    */
}

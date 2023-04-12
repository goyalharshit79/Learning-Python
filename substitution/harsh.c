#include<cs50.h>
#include<ctype.h>
#include<string.h>
#include<stdio.h>

int main(int argc, string argv[])
{
    string alph[7];
    for(int i = 0 ; i < strlen(argv[1]) ; i++)
    {
        alph[i] = alph & argv[1][i];
    }

    printf("%c",alph);    
}
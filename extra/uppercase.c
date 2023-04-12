#include<cs50.h>
#include<stdio.h>
#include<string.h>

int main (void)
{
    string s = get_string("enter:");
    int l = strlen(s);

    for(int i = 0 ; i < l ; i++)
    {
        printf("%c",(s[i] - 32));
    }
    printf("\n");
}
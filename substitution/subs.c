#include<stdio.h>
#include<cs50.h>
#include<ctype.h>
#include<string.h>


int main(int argc, string argv[])
{
    int l;

    if(argc != 2)
    {
        printf("Usage: ./substituion key\n");
        return 1;
    }
    else
    {
        string key = argv[1];
        l = strlen(key);
        if (l == 26)
        {
            for(int i = 0 ; i < l ; i++)
            {
                if(isupper(key[i]) || islower(key[i]))
                {
                    continue;
                }
                else
                {
                    printf("Key must only contain alphabetic characters\n");
                    return 1;
                }
            }
        }
        else
        {
            for ( int i = 0 ; i < l ; )
            {
                if(isupper(key[i]) || islower(key[i]))
                {
                    j++;
                    continue;
                }
                else
                {
                    printf("Key must only contain alphabetic characters\n");
                    return 1;
                }
            }
            
        }
    }
}

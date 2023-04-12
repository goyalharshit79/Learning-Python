#include<stdio.h>

int main(void)
{
    char alph;
    printf("Enter the Max digit : ");
    scanf("%c", &alph);
    
for ( int k = 0 ; k < alph - 65 ; k++)
    {
        for (int i = 65 ; i <= alph-k ; i++)
        {
            printf("%c",i);
        }
        if (k > 0)
        {
            for (int sp = alph ; sp > (alph-(k+1)); sp-- )
            {
                printf(" ");
            }
            for (int j = alph-k ; j >= 65 ; j--)
            {
                printf("%c",j);
            }
        }
        else
        {
            for (int j = alph - 1 ; j >=65 ; j--)
            {
                printf("%c",j);
            }
        }
        printf("\n");
    }   
}

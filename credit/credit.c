#include<cs50.h>
#include<stdio.h>
#include<math.h>

int main(void)
{
/*     cn = credit number
    cs = check sum
    suma = sum of numbers multiplied by 2
    sumb = sum of the rest of the numbers
    cs = suma + sumb (checksum)
    x = multiples of 10 used to get different digits
    num = the number extracted from different places
    numa = if the extracted digits multiplication is bigger than 10 */

    long cn, x;
    int cs, suma, sumb, num, numa;


    //Getting a valid credit card number from the user.
    cn = get_long("Number:");
    if (cn < pow(10, 12))
    {
        printf("INVALID\n");
    }
    else
    {

        //Starting the sum of both kinds of numbers at 0.
        suma = 0;
        sumb = 0;


        //Getting different numbers that are going to be multiplied by 2.
        for (x = 100 ; x < (cn * 10) ; x = x * 100)
        {

            //Formula to start at the second to last place.
            num = ((cn % x) - (cn % (x / 10))) / (x / 10);
            //Multiplying the extracted number by 2.
            num = 2 * num;


            //Checking if the digit when doubled is a two digit number.
            if (num >= 10)
            {
                // Taking the digits seperately in the number.
                for (int i = 10 ; i < 101 ; i = i * 10)
                {
                    numa = ((num % i) - (num % (i / 10))) / (i / 10);
                    suma = suma + numa;
                }
                // Here the for loop could be avoided by simply saying, (numa = num - 9), bcz that always comes out to be the sum of the two digits of a two digit number
                //Ex - 12: 1+2 = 3 = 12 - 9;
                //Loop is used to just be cohesive;
            }
            //If the number is just one digit
            else
            {
                suma = suma + num;
            }
        }


        //Getting the digits that are not doubled
        for (x = 10 ; x < (cn * 10) ; x = x * 100)
        {
            //Formula starting at the last place.
            num = ((cn % x) - (cn % (x / 10))) / (x / 10);
            sumb = sumb + num;
        }


        //Checking the checksum of credit card number
        cs = suma + sumb;


        //Checking for the type of the card
        if ((cs % 10) == 0)
        {
            if (((cn > 34 * pow(10, 13)) && (cn < 35 * pow(10, 13))) || ((cn > 37 * pow(10, 13)) && (cn < 38 * pow(10, 13))))
            {
                printf("AMEX\n");
            }
            else if ((cn > 51 * pow(10, 14))  && (cn < 56 * pow(10, 14)))
            {
                printf("MASTERCARD\n");
            }
            else if (((cn > 4 * pow(10, 12)) && (cn < 5 * pow(10, 12))) || ((cn > 4 * pow(10, 15)) && (cn < 5 * pow(10, 15))))
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }

        else
        {
            printf("INVALID\n");
        }
        printf("%i",cs);
    }
}
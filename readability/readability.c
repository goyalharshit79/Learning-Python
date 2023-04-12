#include<stdio.h>
#include<string.h>
#include<cs50.h>
#include<ctype.h>

void number_words(string text, float *words, float *space, float *punct);

int main(void)
{
    //Getting the text input
    string text = get_string("Text:");
    
    /* l => number of letters in the input text
       sp => number of spaces
       avl => number of average letters per 100 words
       s => number of sentences in the text 
       avs => number of average sentences per 100 words
       index => value of the Coleman-Liau index
       w => number of words in input text*/
    float l, sp, s, w;
    float avl, avs, index; 

    //Counting the number of Letters, spaces and sentences.
    number_words(text, &l, &sp, &s);
    //Number of words
    w = sp + 1;
    //Average letters per 100 words (W)
    avl = (l / w) * 100;
    //Average Sentences per 100 letters
    avs = (s / w) * 100;

    //Calculating the index
    index = 0.0588 * avl - 0.296 * avs - 15.8;

    if (index <= 0.5)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 15.5)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.f\n", index);
    }

    
}


// Function that counts number of Letters, spaces and sentences.
void number_words(string text, float *letters, float *space, float *punctuation)
{
    float n = 0 ;
    float sp = 0;
    float end = 0;
    
    for (int i = 0 ; i <= strlen(text) ; i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            n++;
        }
        else if ((text[i] == 46) || (text[i] == 63) || (text[i] == 33))
        {
            end++;
        }
        else if (text[i] == ' ')
        {
            sp++;
        }
        else
        {
            continue;
        }

    }
    *space = sp;
    *letters = n;
    *punctuation = end;
}
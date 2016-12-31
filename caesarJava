#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("You didn't provide a number!\n");
        return 1;
    }else
    {
        int key = atoi(argv[1]);
        string phrase = GetString();

        if (phrase != NULL)
        {
            int phraseLength = strlen(phrase);

            for (int i = 0; i < phraseLength; i++)
            {
                if(isalpha(phrase[i]))
                {
                    if(islower(phrase[i]))
                    {
                        int lowerCipher = 0;
                        lowerCipher = phrase[i] + key;
                        if(lowerCipher >= 'a' && lowerCipher <='z')
                        {
                            printf("%c", phrase[i] + key);
                        }else
                        {
                            int lowerRemainder = 0;
                            lowerRemainder = (lowerCipher - 'z') % 26;
                            printf("%c", 97 + lowerRemainder - 1);
                        }
                    }else if(isupper(phrase[i]))
                    {
                        int upperCipher = 0;
                        upperCipher = phrase[i] + key;
                        if(upperCipher >= 'A' && upperCipher <='Z')
                        {
                            printf("%c", phrase[i] + key);
                        }else
                        {
                            int upperRemainder = 0;
                            upperRemainder = (upperCipher - 'Z') % 26;
                            printf("%c", (65 + upperRemainder - 1));
                        }
                    }
                }else
                {
                printf("%c", phrase[i]);
                }
            }
            printf("\n");
        }else
        {
            return 1;
        }
    }
return 0;
}

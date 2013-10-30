  #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include <stdio.h>
    #include <string.h>

            int cstring_cmp(const void *a, const void *b)
            {
                const char **ia = (const char **)a;
                const char **ib = (const char **)b;
                return strcasecmp(*ia, *ib);
                /* strcmp functions works exactly as expected from
                comparison function */
            }
Thanks in advance for your response, sorry for my English

            int main (int argc, char *argv [])

            {
            int number;
            char temp [4000];

            printf("input number: ");
            scanf("%d",&number);

            char* array_string [number];
            int i;
            for (i=0;i<number;i++) {
            scanf(" %[^\n]", temp);
            array_string [i] = (char*)malloc((strlen(temp)+1)*sizeof(char));
            strcpy(array_string[i], temp);
            }


            size_t large = sizeof(array_string) / sizeof(char *);
            qsort(array_string,large ,sizeof(char *) ,cstring_cmp );
            printf ("\n");
            printf ("the sorted array list is:\n");
            for (i=0;i<large;i++)
            printf("%s\n", array_string [i]);
                    return 0;
            }

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int printFromFile(){
    FILE *ifp;
    char *mode = "r";
    char filename[25]  = "Postnummeroppdatert.txt";

    ifp = fopen(filename, mode);

    char x[20];
    char y[20];
    char z[20];

    char postnummer[4];

    printf("Tast inn postnummer:\n");
    scanf("%99s", postnummer);

    while (fscanf(ifp, "%[^\t]\t%[^\t]\t%[^\n]\n]", x, y, z) !=EOF)
        if (strcmp(z,postnummer) == 0)
            printf("%s %s\n", x, y);



    fclose(ifp);

}

int main(){
    printFromFile(); 

    printf("Trykk Enter ...\n");
    getchar();
    getchar();

    return(0);
}
